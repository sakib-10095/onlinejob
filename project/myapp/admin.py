from django.contrib import admin
from myapp.models import *


class customUser_display(admin.ModelAdmin):

    list_display=['display_name','email','user_type']
    

admin.site.register(customUser,customUser_display)
admin.site.register(addjob_model)
admin.site.register(recruiterProfile)
admin.site.register(jobseekerProfile)
admin.site.register(job_Apply_model)



