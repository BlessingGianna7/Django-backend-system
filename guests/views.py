from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import GuestForm
from conservation.api_handler import APIHandler
from django.contrib import messages
import requests

@login_required
def add_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            try:
                guest_data = {
                    'name': form.cleaned_data['name'],
                    'visit_date': form.cleaned_data['visit_date'].isoformat(),
                    'guiders': [guider.id for guider in form.cleaned_data['guiders']]
                }
                APIHandler.post("/guests/", guest_data)
                messages.success(request, 'Guest added successfully!')
                return redirect('guest_list')
            except Exception as e:
                messages.error(request, f'Error adding guest: {str(e)}')
    else:
        form = GuestForm()
    return render(request, 'guests/add_guest.html', {'form': form})

@login_required
def guest_list(request):
    try:
        guests = APIHandler.get("/guests/")
        return render(request, 'guests/guest_list.html', {'guests': guests})
    except Exception as e:
        messages.error(request, f'Error fetching guests: {str(e)}')
        return render(request, 'guests/guest_list.html', {'guests': []})

@login_required
def edit_guest(request, guest_id):
    try:
        if request.method == "POST":
            form = GuestForm(request.POST)
            if form.is_valid():
                guest_data = {
                    'name': form.cleaned_data['name'],
                    'visit_date': form.cleaned_data['visit_date'].isoformat(),
                    'guiders': [guider.id for guider in form.cleaned_data['guiders']]
                }
                APIHandler.put(f"/guests/{guest_id}", guest_data)
                return redirect('guest_list')
        else:
            guest = APIHandler.get(f"/guests/{guest_id}")
            form = GuestForm(initial=guest)
        return render(request, 'guests/edit_guest.html', {'form': form, 'guest': guest})
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return redirect('guest_list')

@login_required
def delete_guest(request, guest_id):
    if request.method == 'POST':
        try:
            APIHandler.delete(f'/guests/{guest_id}/')
            messages.success(request, 'Guest deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting guest: {str(e)}')
    return redirect('guest_list')