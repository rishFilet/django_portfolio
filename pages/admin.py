from django.contrib import admin
from pages.models import IndustryExperience, JobDescription, JobAccomplishment
# Register your models here.


class IEAdmin(admin.ModelAdmin):
    pass

class JDAdmin(admin.ModelAdmin):
    pass

class JAAdmin(admin.ModelAdmin):
    pass

admin.site.register(IndustryExperience, IEAdmin)
admin.site.register(JobDescription, JDAdmin)
admin.site.register(JobAccomplishment, JAAdmin)