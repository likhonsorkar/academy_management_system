from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from .models import Admission, Payment
from core.utils import send_sms

@receiver(post_save, sender=Admission)
def auto_cancel_pending(sender, instance, created, **kwargs):
    """
    Automatically cancel admission if payment not verified in 24 hours.
    Only runs for newly created Admissions (created=True)
    """
    if created and instance.status == 'PENDING':
        now = timezone.now()
        expiration_time = instance.created_at + timedelta(hours=24)
        if now > expiration_time:
            instance.status = 'CANCELLED'
            instance.save()

@receiver(post_save, sender=Payment)
def payment_verified_sms(sender, instance, created, **kwargs):
    """
    Payment verified হলে SMS পাঠাবে
    """
    if instance.verified:   # verified=True হলে
        admission = instance.admission

        # Admission status update
        if admission.status != 'ACCEPTED':
            admission.status = 'ACCEPTED'
            admission.save(update_fields=['status'])

            # SMS message
            msg = (
                f"প্রিয় {admission.name}, "
                f"আপনার পেমেন্ট যাচাই হয়েছে এবং আবেদন গৃহীত হয়েছে।"
            )
            send_sms(admission.mobile, msg)

