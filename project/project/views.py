from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password



def signupPage(request):

    if request.method=="POST":
        username=request.POST.get("username")
        display_name=request.POST.get("display_name")
        email=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("confirm_password")
        user_type=request.POST.get("user_type")

        if pass1!=pass2:
            messages.error(request,"Password & Confirmpassword Not Match")

        else:
            user=customUser.objects.create_user(username=username,display_name=display_name,email=email,password=pass1,user_type=user_type)
            user.save()

            if user.user_type == "recruiter":
                user=recruiterProfile.objects.create(user=user)
                user.save()
            else:
                
                user=jobseekerProfile.objects.create(user=user)
                user.save()
            return redirect("loginPage")
    return render(request,"signup.html")



def loginPage(request):

    if request.method=="POST":

        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user!=None:
            login(request,user)
            return redirect("homePage")
        else:
            messages.error(request,"Invalid User")
    return render(request,"login.html")


def logoutPage(request):
    
    logout(request)
    return redirect("loginPage")



def dashboardPage(request):
    return render(request,"dashboard.html")

def homePage(request):
    return render(request,"homepage.html")


def addjobPage(request):

    user=request.user

    if request.method=="POST":
        jobTitle=request.POST.get("jobTitle")
        companyName=request.POST.get("companyName")
        description=request.POST.get("description")
        location=request.POST.get("location")

        job=addjob_model(jobTitle=jobTitle,companyName=companyName,description=description,location=location,creat_time=user,job_creator=user)
        job.save()
        return redirect("viewjobPage")

    return render(request,"Recruiter/addjob.html")


def viewjobPage(request):

    job=addjob_model.objects.all()
    return render(request,"viewjob.html",{"job":job})

def deletePage(request,id):
    job=addjob_model.objects.filter(id=id)
    job.delete()
    return redirect("viewjobPage")


def editPage(request,id):

    job=addjob_model.objects.filter(id=id)
   
    return render(request,"Recruiter/edit.html",{"job":job})


def updatePage(request,id):

    user=request.user

    if request.method=="POST":
        jobTitle=request.POST.get("jobTitle")
        companyName=request.POST.get("companyName")
        description=request.POST.get("description")
        location=request.POST.get("location")

        job=addjob_model(jobTitle=jobTitle,companyName=companyName,description=description,location=location,update_time=user,job_creator=user,id=id)
        job.save()
        return redirect("viewjobPage")




def profilePage(request):
    
    return render(request,"profile.html")


def editprofilePage(request):
    user=request.user
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        display_name=request.POST.get("display_name")
        profile_picture=request.FILES.get("profile_picture")
        skill=request.POST.get("skill")
        resume=request.FILES.get("resume")
        password=request.POST.get("password")

        if not check_password(password,user.password):
            messages.error(request,"password not match")
            return redirect("editprofilePage")
        

        if user.user_type == "jobseeker":
            jobProfile=user.jobseeker_Profile
            jobProfile.skill=skill
            jobProfile.resume=resume
            jobProfile.save()


        user.first_name=first_name
        user.last_name=last_name
        user.display_name=display_name
        user.profile_picture=profile_picture
        user.save()
        messages.success(request,"Profile Update Successfully")
        return redirect("profilePage")
    
    return render(request,"editprofile.html")

def changePassword(request):
    user=request.user
    if request.method=="POST":
        current_Password=request.POST.get("current_Password")
        new_Password=request.POST.get("new_Password")
        confirm_Password=request.POST.get("confirm_Password")

        if not check_password(current_Password, user.password):
            messages.error(request,"Password not match")
            return redirect("changePassword")
        
        if new_Password !=confirm_Password:
            messages.error(request,"new_Password & confirm_Password not match")
            return redirect("changePassword")
        
        else:
            user.set_password(new_Password)
            user.save()
            messages.success(request,"Password Change Successfully")
            return redirect("loginPage")
    return render(request,"changepassword.html")


def applyPage(request,id):

    
    job=get_object_or_404(addjob_model, id=id)
     
    if request.method=="POST":
        skills=request.POST.get("skills")
        salary=request.POST.get("salary")
        apply_resume=request.FILES.get("apply_resume")

        if skills and salary and apply_resume:
            user=request.user
            
            aplications=job_Apply_model.objects.create(job=job,aplicant=user,skills=skills,salary=salary,apply_resume=apply_resume)
            aplications.save()
            messages.success(request,"Apply Successfull")
            return redirect("profilePage")


    return render(request,"Jobseeker/applypage.html",{"job":job})

def createdjob(request):
    user=request.user
    job=addjob_model.objects.filter(job_creator=user)
    return render(request,"Recruiter/createjob.html",{"job":job})


def Apliedjob(request):
    user=request.user
    job=job_Apply_model.objects.filter(aplicant=user)
    return render(request,"Jobseeker/apliedjob.html",{"job":job})

def Aplicant_view(request,id):
    myjob=get_object_or_404(addjob_model,id=id)
    job=job_Apply_model.objects.filter(job=myjob)
    return render(request,"Recruiter/aplicant.html",{"job":job})