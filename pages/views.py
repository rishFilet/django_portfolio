from django.shortcuts import render
from pages.models import IndustryExperience, JobAccomplishment, JobDescription

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def cv_page(request):
    industry_exp = IndustryExperience.objects.all()
    job_desc = JobDescription.objects.all()
    job_acc = JobAccomplishment.objects.all()
    context = {
        'ie' : industry_exp,
        'jd' : job_desc,
        'ja' : job_acc,

    }
    return render(request, 'cv.html', context)

def volunteer_page(request):
    return render(request, 'volunteering.html')