from django.contrib import admin
from myapp.models import *


class customUser_display(admin.ModelAdmin):

    list_display=['display_name','email','user_type']
    

admin.site.register(customUser,customUser_display)
