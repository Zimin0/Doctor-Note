from django.shortcuts import render, redirect, get_object_or_404
from medicine.forms import MedicineForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET

from .models import Medicine

@login_required
def display_medicines(request):
    """ Главная страница с выписанными лекарствами. """
    context = {}
    medicines = Medicine.active_medicine_sorted.filter(patient=request.user)
    context['medicines'] = medicines
    return render(request, 'medicine/medicine.html', context)

@login_required
def add_medicine(request):
    """ Добавление выписанного лекарства """
    if request.method == 'POST':
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

@csrf_exempt
@require_POST
def update_medicine(request, medicine_id, action):
    if request.method == 'POST':
        try:
            medicine = Medicine.objects.get(id=medicine_id)
            if action == 'increment' and medicine.today < medicine.amount_per_day:
                medicine.today += 1
            elif action == 'decrement' and medicine.today > 0:
                medicine.today -= 1
            medicine.save()
            return JsonResponse({'success': True, 'new_today': medicine.today, 'amount_per_day': medicine.amount_per_day})
        except Medicine.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Medicine not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
