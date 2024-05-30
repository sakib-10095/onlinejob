from django.db import models
from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),
        ('jobseeker','Jobseeker')
    ]
    display_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    user_type=models.CharField(choices=USER,max_length=100)
    profile_picture=models.ImageField(upload_to="media/profile_pic",null=True)


    def __str__(self):
        return self.display_name
    
class addjob_model(models.Model):
    jobTitle=models.CharField(max_length=100,null=True)
    companyName=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=100,null=True)
    location=models.CharField(max_length=100,null=True)
    job_creator=models.ForeignKey(customUser,on_delete=models.CASCADE,null=True)
    creat_time=models.TimeField(auto_now_add=True,null=True)
    update_time=models.TimeField(auto_now=True,null=True)

    def __str__(self):
        return self.jobTitle
    
class recruiterProfile(models.Model):
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,null=True,related_name="recruiter_Profile")

    def __str__(self):
        return self.user.display_name


class jobseekerProfile(models.Model):
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,null=True,related_name="jobseeker_Profile")
    resume=models.FileField(upload_to="media/resume",null=True)
    skill=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.user.display_name
    

