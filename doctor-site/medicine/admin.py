from django.contrib import admin
from medicine.models import Medicine

class MedicineAdmin(admin.ModelAdmin):
    list_display = ['title', 'dosage', 'end_date', 'amount_per_day', 'is_ended']
    

admin.site.register(Medicine, MedicineAdmin)
