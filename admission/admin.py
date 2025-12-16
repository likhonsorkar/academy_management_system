from django.contrib import admin
from .models import Admission, Payment
from core.utils import send_sms

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('admission_id', 'name', 'admission_class', 'status', 'created_at')
    list_filter = ('status', 'admission_class')
    actions = ['approve_admission']

    def approve_admission(self, request, queryset):
        queryset.update(status='ACCEPTED')
        self.message_user(request, "Selected admissions have been approved.")
    approve_admission.short_description = "Approve selected admissions"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('admission', 'bkash_trxid', 'verified')
    actions = ['verify_payment']

    def verify_payment(self, request, queryset):
        for payment in queryset:
            payment.verified = True
            payment.save()
            
            admission = payment.admission
            admission.status = 'ACCEPTED'
            admission.save()
            
            
        self.message_user(request, "Selected payments verified and admissions accepted.")
    verify_payment.short_description = "Verify selected payments"

