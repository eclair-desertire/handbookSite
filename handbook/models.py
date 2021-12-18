from django.conf import settings
from django.db import models
from django.utils import timezone

COMPANY_TYPES_CHOICES=(
    ("IS","Internet Shop"),
    ("SM","SuperMarket"),
    ("SP","Shopping center"),
    ("FR","Furniture Shop"),
    ("DF","DEFAULT")
)
COMPANY_RATE_CHOICES=(
    ("VB","1"),
    ("R","2"),
    ("G","3"),
    ("B","4"),
    ("D","5")
)


# Create your models here.
class Company(models.Model):
    company_name=models.CharField(max_length=40,blank=True)
    company_about=models.TextField(blank=True)
    company_phone=models.CharField(max_length=30,blank=True)
    comapny_category=models.CharField(max_length=40,choices=COMPANY_TYPES_CHOICES,default="DF")
    company_email=models.EmailField(blank=True)
    company_logo=models.ImageField(blank=True)
    published_date=models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.company_name

class Rate(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    rate=models.CharField(max_length=20,choices=COMPANY_RATE_CHOICES)
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.company