from django import forms
from medicine.models import Medicine

class MedicineForm(forms.ModelForm):
    end_date = forms.DateField(input_formats=['%d/%m/%Y', '%d.%m.%Y','%d-%m-%Y', '%Y-%m-%d'])

    class Meta:
        model = Medicine
        fields = ['title', 'end_date', 'amount_per_day', 'dosage', 'comments', 'is_ended']