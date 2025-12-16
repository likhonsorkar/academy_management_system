from django.shortcuts import render, get_object_or_404
from admission.models import *
from .forms import *
from core.utils import send_sms

# Admission Form View
def admission_create(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            admission = form.save()
            msg = f"{admission.name} আপনার এপ্লিকেশন আইডি {admission.admission_id}. দয়া করে পেমেন্ট সম্পন্ন করুন।"
            send_sms(admission.mobile, msg)
            return render(request, 'success.html', {'admission': admission})
    else:
        form = AdmissionForm()
    return render(request, 'admission_form.html', {'form': form})

# Payment Form View
def submit_payment(request, admission_id):
    admission = get_object_or_404(Admission, admission_id=admission_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.admission = admission
            payment.save()
            admission.status = 'PENDING'
            admission.save()
            msg = f"{admission.name} আপনার পেমেন্ট পেন্ডিং আছে। কিছুক্ষনের মধ্যে যাচাই করে জানানো হবে।"
            send_sms(admission.mobile, msg)
            return render(request, 'payment_success.html', {'admission': admission})
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form, 'admission': admission})

def find_admission_id(request):
    admission = None
    if request.method == 'POST':
        birth_date = request.POST.get('birth_date')
        birth_certificate_no = request.POST.get('birth_certificate_no')
        admission = Admission.objects.filter(birth_date=birth_date, birth_certificate_no=birth_certificate_no).first()
    return render(request, 'find_admission_id.html', {'admission': admission})

# Admission Status Check View
def check_status(request):
    status = None
    if request.method == 'POST':
        admission_id = request.POST.get('admission_id')
        birth_date = request.POST.get('birth_date')
        birth_certificate_no = request.POST.get('birth_certificate_no')
        admission = Admission.objects.filter(admission_id=admission_id, birth_date=birth_date, birth_certificate_no=birth_certificate_no).first()
        if admission:
            status = admission.status
    return render(request, 'check_status.html', {'status': status})
