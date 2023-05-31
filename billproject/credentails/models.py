from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Registers(models.Model):
    admn_no = models.IntegerField(default=0)
    sname = models.CharField(max_length=100)
    dob = models.DateField()
    aadharno = models.IntegerField(default=0)
    email_id = models.EmailField()
    phno = models.IntegerField(default=0)
    address = models.TextField()
    course = models.CharField(max_length=100)
    doj = models.DateField()
    duration = models.PositiveIntegerField(default=0)
    end_date = models.DateField(null=True, blank=True)
    mode_choices = [('online', 'Online'), ('offline', 'Offline'), ('recorded', 'Recorded'), ]
    mode = models.CharField(max_length=10, choices=mode_choices)
    course_fee = models.IntegerField(default=0)
    emi = models.IntegerField(default=0)
    permonth = models.IntegerField(null=True, blank=True)

def save(self, *args, **kwargs):
        doj = datetime.strptime(self.doj, '%Y-%m-%d').date()
        duration = self.duration

        end_date = doj + relativedelta(months=duration)
        self.end_date = end_date.strftime('%Y-%m-%d')
        super().save(*args, **kwargs)

def __str__(self):
        return f"Event {self.id}"


# Create your models here.
