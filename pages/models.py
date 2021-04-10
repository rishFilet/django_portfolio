from django.db import models

#Create your models here.


class IndustryExperience(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.role


class JobDescription(models.Model):
    WORK_TYPE = (
        ("Contract", "Contract"),
        ("Full Time", "Full Time"),
        ("Freelance", "Freelance"),
    )

    company_name = models.CharField(max_length=200)
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


class JobAccomplishment(models.Model):
    short_title = models.CharField(max_length=200, default='MISSING SHORT TITLE')
    description = models.TextField()
    project_id = models.CharField(max_length=200, blank=True)
    company = models.ForeignKey(
        JobDescription, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.short_title
