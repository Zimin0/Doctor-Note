from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from medicine.models import Medicine
from medicine.forms import MedicineForm

@login_required
def display_medicines(request):
    """ Главная страница с выписанными лекарствами. """
    context = {}
    # medicines = Medicine.active_medicine_sorted.filter()
    medicines = request.user.medicines.all()
    context['medicines'] = medicines
    return render(request, 'medicine/medicine.html', context)

@login_required
def add_medicine(request):
    """ Добавление выписанного лекарства """
    if request.method == 'POST':
        print(request.POST)
        form = MedicineForm(request.POST)
        if form.is_valid():
            new_medicine = form.save(commit=False)
            new_medicine.patient = request.user
            new_medicine.save()
            return redirect('medicine:display_medicines')
        else:
            print(form.errors)
            return render(request, 'medicine/addMedicine.html', {'form':form, 'errors': form.errors})
    else:
        form = MedicineForm()
        return render(request, 'medicine/addMedicine.html', {'form':form})

@login_required
def edit_medicine(request, medicine_id):
    """ Изменение выписанного лекарства """
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine:display_medicines')
        else:
            print(form.errors)
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'medicine/editMedicine.html', {'form': form})
