# =============================
# forms.py (admission/forms.py)
# =============================
from django import forms
from .models import Admission, Payment

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ['name', 'birth_date', 'birth_certificate_no', 'gender',
                  'father_name', 'mother_name', 'guardian_name', 'mobile',
                  'admission_class', 'previous_class', 'previous_institute']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full border p-2 rounded'}),
            'gender': forms.Select(attrs={'class': 'w-full border p-2 rounded'}),
            'admission_class': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'previous_class': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'previous_institute': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'name': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'father_name': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'mother_name': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'guardian_name': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'mobile': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'birth_certificate_no': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['bkash_trxid', 'bkash_number', 'amount']
        widgets = {
            'bkash_trxid': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'bkash_number': forms.TextInput(attrs={'class': 'w-full border p-2 rounded'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full border p-2 rounded'}),
        }