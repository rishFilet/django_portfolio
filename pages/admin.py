from django.contrib import admin
from pages.models import CardHeaders, Description, Accomplishment, CVSectionHeader
# Register your models here.

class SHAdmin(admin.ModelAdmin):
    pass
class CHAdmin(admin.ModelAdmin):
    pass

class DescAdmin(admin.ModelAdmin):
    pass

class AccompAdmin(admin.ModelAdmin):
    pass

admin.site.register(CVSectionHeader, SHAdmin)
admin.site.register(CardHeaders, CHAdmin)
admin.site.register(Description, DescAdmin)
admin.site.register(Accomplishment, AccompAdmin)