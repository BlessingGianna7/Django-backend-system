@login_required
def edit_animal(request, animal_id):
    try:
        if request.method == 'POST':
            form = AnimalForm(request.POST)
            if form.is_valid():
                animal_data = {
                    'name': form.cleaned_data['name'],
                    'species': form.cleaned_data['species'],
                    'age': form.cleaned_data['age'],
                    'guider_ids': [guider.id for guider in form.cleaned_data['guiders']]
                }
                APIHandler.put(f"/animals/{animal_id}/", animal_data)
                messages.success(request, 'Animal updated successfully!')
                return redirect('animal_list')
        else:
            animal = APIHandler.get(f"/animals/{animal_id}/")
            form = AnimalForm(initial=animal)
        return render(request, 'animals/edit_animal.html', {'form': form, 'animal': animal})
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return redirect('animal_list')

@login_required
def delete_animal(request, animal_id):
    if request.method == 'POST':
        try:
            APIHandler.delete(f'/animals/{animal_id}/')
            messages.success(request, 'Animal deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting animal: {str(e)}')
    return redirect('animal_list')