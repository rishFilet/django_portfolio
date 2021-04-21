from django.shortcuts import render
from pages.models import CVSectionHeader, CardHeaders, Accomplishment, Description

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def cv_page(request):
    section_headers = CVSectionHeader.objects.all()
    card_headers_unsorted = CardHeaders.objects.all()
    desc = Description.objects.all()
    accomp = Accomplishment.objects.all()

    # This is a sort of the card headers based on the year and then month of the first entry in the headers
    desc_dict = {}
    for each_header in card_headers_unsorted:
        desc_dict[each_header] = []
    for k, v in desc_dict.items():
        for each_desc in desc:
            if str(each_desc.job_role) == k.role:
                desc_dict[k].append(each_desc)

    sort_dict = {}
    for each_section in section_headers:
        sort_dict[each_section] = []
    for k, v in sort_dict.items():
        for each_header in card_headers_unsorted:
            if str(each_header.section) == k.section_name:
                sort_dict[k].append(each_header)

    card_headers = []
    for k, v in sort_dict.items():
        if len(v) != 0:
            cursor = v[0]
            if len(desc_dict[cursor]) > 0:
                for index in range(1, len(v)):
                    if desc_dict[v[index]][0].year_ended > desc_dict[cursor][0].year_ended:
                        v[index], v[0] = v[0], v[index]
                    elif desc_dict[v[index]][0].year_ended == desc_dict[cursor][0].year_ended:
                        if desc_dict[v[index]][0].month_ended > desc_dict[cursor][0].month_ended:
                            v[index], v[0] = v[0], v[index]
            card_headers.extend(v)


    context = {
        'sh': section_headers,
        'ch': card_headers,
        'desc': desc,
        'accomp': accomp,

    }
    return render(request, 'cv.html', context)

def volunteer_page(request):
    return render(request, 'volunteering.html')
