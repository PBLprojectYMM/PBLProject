from django.contrib import admin
from home.models import vaccine_pincode
from django.conf.locale.es import formats as es_formats
# Register your models here.
# admin.site.register(Contact)
admin.site.register(vaccine_pincode)

es_formats.DATE_FORMAT = "dd-MM-YYYY"
