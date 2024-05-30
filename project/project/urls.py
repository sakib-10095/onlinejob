"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from project import views  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage, name="loginPage"),
    path('logoutPage/', views.logoutPage, name="logoutPage"),
    path('signupPage/', views.signupPage, name="signupPage"),
    path('dashboardPage/', views.dashboardPage, name="dashboardPage"),
    path('homePage/', views.homePage, name="homePage"),
    path('addjobPage/', views.addjobPage, name="addjobPage"),
    path('viewjobPage/', views.viewjobPage, name="viewjobPage"),
    path('deletePage/<str:id>', views.deletePage, name="deletePage"),
    path('editPage/<str:id>', views.editPage, name="editPage"),
    path('updatePage/<str:id>', views.updatePage, name="updatePage"),
    path('profilePage/', views.profilePage, name="profilePage"),
    path('editprofilePage/', views.editprofilePage, name="editprofilePage"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)