from django.contrib import admin
from configurator.models import MQTTConfig 
from configurator.models import SQLConfig

# Register your models here.
admin.site.register(MQTTConfig)
admin.site.register(SQLConfig)