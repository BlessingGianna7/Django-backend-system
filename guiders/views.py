from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from conservation.api_handler import APIHandler

@login_required
def guider_list(request):
    try:
        guiders = APIHandler.get("/guiders/")
        return render(request, 'guiders/guider_list.html', {'guiders': guiders})
    except Exception as e:
        messages.error(request, f'Error fetching guiders: {str(e)}')
        return render(request, 'guiders/guider_list.html', {'guiders': []})

@login_required
def add_guider(request):
    if request.method == 'POST':
        try:
            guider_data = {
                'name': request.POST.get('name'),
                'age': int(request.POST.get('age')),
                'service_hours': int(request.POST.get('service_hours'))
            }
            APIHandler.post("/guiders/", guider_data)
            messages.success(request, 'Guider added successfully!')
            return HttpResponseRedirect(reverse('guider_list'))
        except Exception as e:
            messages.error(request, f'Error adding guider: {str(e)}')
            return render(request, 'guiders/add_guider.html')
    return render(request, 'guiders/add_guider.html')

@login_required
def edit_guider(request, guider_id):
    try:
        if request.method == 'POST':
            # Handle form submission
            guider_data = {
                'name': request.POST.get('name'),
                'age': int(request.POST.get('age')),
                'service_hours': int(request.POST.get('service_hours'))
            }
            print(f"Updating guider {guider_id} with data: {guider_data}") 
            APIHandler.put(f'/guiders/{guider_id}/', guider_data)
            messages.success(request, 'Guider updated successfully!')
            return HttpResponseRedirect(reverse('guider_list'))
        else:
          
            print(f"Fetching guider {guider_id} for edit form")  
            guider = APIHandler.get(f'/guiders/{guider_id}/')
            print(f"Fetched guider data: {guider}")  
            return render(request, 'guiders/edit_guider.html', {'guider': guider})
    except Exception as e:
        print(f"Error in edit_guider: {str(e)}")  
        messages.error(request, f'Error updating guider: {str(e)}')
        return HttpResponseRedirect(reverse('guider_list'))

@login_required
def delete_guider(request, guider_id):
    try:
        if request.method == 'POST':
            APIHandler.delete(f'/guiders/{guider_id}')
            messages.success(request, 'Guider deleted successfully!')
            return HttpResponseRedirect(reverse('guider_list'))
        else:
            # If it's not a POST request, redirect to list view
            return HttpResponseRedirect(reverse('guider_list'))
    except Exception as e:
        messages.error(request, f'Error deleting guider: {str(e)}')
        return HttpResponseRedirect(reverse('guider_list'))