from django.db import models
import uuid

class Admission(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Payment Pending'),
        ('ACCEPTED', 'Accepted'),
        ('CANCELLED', 'Cancelled'),
    )

    admission_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, verbose_name='নাম')
    birth_date = models.DateField(verbose_name='জন্ম তারিখ')
    birth_certificate_no = models.CharField(max_length=50, verbose_name='জন্ম নিবন্ধন নম্বর')
    gender = models.CharField(max_length=10, choices=(('Male','পুরুষ'),('Female','মহিলা')), verbose_name='লিঙ্গ')

    father_name = models.CharField(max_length=100, verbose_name='পিতার নাম')
    mother_name = models.CharField(max_length=100, verbose_name='মাতার নাম')
    guardian_name = models.CharField(max_length=100, verbose_name='অভিভাবকের নাম')

    mobile = models.CharField(max_length=15, verbose_name='মোবাইল')
    admission_class = models.CharField(max_length=20, verbose_name='ভর্তি শ্রেণি')

    previous_class = models.CharField(max_length=20, blank=True, null=True, verbose_name='পূর্ববর্তী শ্রেণি')
    previous_institute = models.CharField(max_length=200, blank=True, null=True, verbose_name='পূর্ববর্তী প্রতিষ্ঠান')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING', verbose_name='অবস্থা')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='তৈরি তারিখ')

    def __str__(self):
        return str(self.admission_id)


class Payment(models.Model):
    admission = models.OneToOneField(Admission, on_delete=models.CASCADE, verbose_name='ভর্তি')
    bkash_trxid = models.CharField(max_length=50, verbose_name='bKash TrxID')
    bkash_number = models.CharField(max_length=20, verbose_name='bKash Number')
    amount = models.IntegerField(verbose_name='Amount')
    verified = models.BooleanField(default=False, verbose_name='যাচাই হয়েছে')

    def __str__(self):
        return self.bkash_trxid