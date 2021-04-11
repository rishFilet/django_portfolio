from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime as dt

#Create your models here.


class IndustryExperience(models.Model):
    role = models.CharField(max_length=200)
    role_id = models.CharField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.role


class JobDescription(models.Model):
    WORK_TYPE = (
        ("Contract", "Contract"),
        ("Full Time", "Full Time"),
        ("Freelance", "Freelance"),
    )

    company_name = models.CharField(max_length=200)
    company_link = models.URLField(max_length=500, null=True)
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPE, default='Contract')
    month_started = models.IntegerField()
    year_started = models.IntegerField()
    month_ended = models.IntegerField()
    year_ended = models.IntegerField()
    work_location = models.CharField(max_length=200)
    job_role = models.ForeignKey(
        IndustryExperience, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.company_name

    def clean(self):
        current_year = dt.today().year
        current_month = dt.today().month
        month_check_list = {'month_started': self.month_started,'month_ended':self.month_ended}
        year_check_list = {'year_started': self.year_started, 'year_ended' : self.year_ended}
        for k,v in month_check_list.items():
            if v > 12 or v < 1:
                raise ValidationError({f'{k}':"Month should be a number between 1 and 12 inclusive"})
        for k,v in year_check_list.items():
            if v > current_year or v < 1987:
                raise ValidationError(
                    {f'{k}': "Year cannot be more than today or earlier than your birth"})
        if self.year_started == self.year_ended:
            if self.month_ended < self.month_started:
                raise ValidationError({'month_ended':"End month cannot be earlier than start month"})
            if self.year_started == current_year:
                if self.month_ended > current_month or self.month_started > current_month:
                    raise ValidationError(
                        {'month_ended': f"Months cannot be more than current month value of {current_month}"})
        if self.year_ended < self.year_started:
            raise ValidationError({'year_ended':"Year ended cannot be earlier than year started"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

class JobAccomplishment(models.Model):
    short_title = models.CharField(max_length=200, default='MISSING SHORT TITLE')
    description = models.TextField()
    project_id = models.CharField(max_length=200, blank=True)
    company = models.ForeignKey(
        JobDescription, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.short_title
