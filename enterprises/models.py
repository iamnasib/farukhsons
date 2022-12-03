from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill 
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    business_title = models.CharField(max_length=200, blank=True, null=True)
    business_tagline=models.CharField(max_length=200, blank=True, null=True)
    business_address = models.TextField(max_length=500, blank=True, null=True)
    business_email = models.EmailField(blank=True, null=True)
    business_phone = models.CharField(max_length=10, blank=True, null=True)
    business_gst = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class WorkImages(models.Model):
    img = ProcessedImageField(upload_to='images/', help_text="img",
                                     verbose_name="img",
                                     processors=[ResizeToFill(300, 300)],
                                     format='JPEG',
                                     options={'quality': 80})
    title = models.CharField(max_length=200,blank=True,null=True)
    display_on_home = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Invoice(models.Model):
    invoice_number = models.IntegerField(blank=True,null=True)
    invoice_date = models.DateField(blank=True,null=True)
    invoice_order_number=models.CharField(max_length=200, blank=True, null=True)
    invoice_order_number_2=models.CharField(max_length=200, blank=True, null=True)
    invoice_to = models.CharField(max_length=200, blank=True, null=True)
    invoice_heading= models.TextField()
    invoice_json = models.TextField()
    def __str__(self):
        return str(self.invoice_number) + " | " + str(self.invoice_date)