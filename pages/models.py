from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime as dt

#Create your models here.
class CVSectionHeader(models.Model):
    section_name = models.CharField(max_length=200, blank=True, unique=True)
    section_image = models.FileField(upload_to='cv_icons', blank=True, null=True)


    def __str__(self):
        return self.section_name

class CardHeaders(models.Model):
    role = models.CharField(max_length=200, verbose_name="Role / Certification")
    role_id = models.CharField(max_length=200, unique=True, null=True, verbose_name="Role / Certification id")
    section = models.ForeignKey(CVSectionHeader, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.role

class Description(models.Model):
    WORK_TYPE = (
        ("Contract", "Contract"),
        ("Full Time", "Full Time"),
        ("Freelance", "Freelance"),
    )

    logos = models.FileField(upload_to='cv_logos', blank=True, null=True, default='')
    company_name = models.CharField(max_length=200, verbose_name='Company / Institution / Organisation')
    company_link = models.URLField(max_length=500, null=True, verbose_name='Website')
    work_type = models.CharField(
        max_length=20, choices=WORK_TYPE, default='Contract', blank=True)
    month_started = models.IntegerField(
        default=0, verbose_name="Month Started (enter 0 if not available)")
    year_started = models.IntegerField(
        default=0, verbose_name="Year Started (enter 0 if not available)")
    month_ended = models.IntegerField(
        default=0, verbose_name="Month Ended (enter 0 if not available)")
    year_ended = models.IntegerField(
        default=0, verbose_name="Year Ended (enter 0 if not available)")
    work_location = models.CharField(max_length=200, verbose_name='Location', blank=True)
    job_role = models.ForeignKey(
        CardHeaders, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Role / Certification")


    def __str__(self):
        return self.company_name

    def clean(self):
        current_year = dt.today().year
        current_month = dt.today().month
        month_check_list = {
            'month_started': self.month_started, 'month_ended': self.month_ended}
        year_check_list = {'year_started': self.year_started,
                           'year_ended': self.year_ended}
        for k, v in month_check_list.items():
            if v > 12 or v < 0:
                raise ValidationError(
                    {f'{k}': "Month should be a number between 1 and 12 inclusive, 0 to display no month and year"})
        for k, v in year_check_list.items():
            if v != 0:
                if v > current_year or v < 1987:
                    raise ValidationError(
                        {f'{k}': "Year cannot be more than today or earlier than your birth"})
        if self.year_started == self.year_ended:
            if self.month_ended < self.month_started:
                raise ValidationError(
                    {'month_ended': "End month cannot be earlier than start month"})
            if self.year_started == current_year:
                if self.month_ended > current_month or self.month_started > current_month:
                    raise ValidationError(
                        {'month_ended': f"Months cannot be more than current month value of {current_month}"})
        if v != 0:
            if self.year_ended < self.year_started:
                raise ValidationError(
                    {'year_ended': "Year ended cannot be earlier than year started"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-year_ended', '-month_ended', '-year_started','-month_started']
class Accomplishment(models.Model):
    short_title = models.CharField(
        max_length=200, default='MISSING SHORT TITLE')
    include_title = models.CharField(max_length=200, choices=[('Yes', 'yes'), ('No', 'no')], default='yes', null=True, verbose_name='Show short title?')
    description = models.TextField()
    project_id = models.CharField(max_length=200, blank=True)
    company = models.ForeignKey(Description, on_delete=models.CASCADE, null=True, verbose_name='Company / Institution / Organisation')

    def __str__(self):
        return self.short_title
