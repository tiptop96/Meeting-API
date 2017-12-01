from django.contrib import admin
from api.models import Meeting, When, Location
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class LocationInline(admin.StackedInline):
    model = Location
    verbose_name_plural = 'Location'
    fk_name = 'meeting'

class WhenInline(admin.StackedInline):
    model = When
    verbose_name_plural = 'When'
    fk_name = 'meeting'

class AjaxedAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        location_array = form.cleaned_data.get('adress').split(",")
        obj.location.country = location_array[-1]
        if len(location_array) > 3:
            obj.location.province = location_array[2]
        else:
            obj.location.province = "Province Undef"
        obj.location.city = location_array[1]
        obj.location.street = location_array[0]
        super(AjaxedAdmin, self).save_model(request, obj, form, change)

    #Security for only allowing editing of your objects
    def get_queryset(self, request):
        queryset = super(AjaxedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(owner=request.user)
    #Adding when to the Meeting objects in admin
    inlines = (WhenInline,LocationInline)
    #Seeting upp JS for adress field
    class Media:
        js = (
            'js/geo-fetch.js',
        )

admin.site.register(Meeting, AjaxedAdmin)

# Register your models here.
