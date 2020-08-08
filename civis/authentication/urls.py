"""sankeerth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('detail/', views.detail, name="detail"),
    path('pie_chart/', views.pie_chart, name="pie_chart"),
    path('pie_chart1/', views.pie_chart1, name="pie_chart1"),
    path('pie_chart2/', views.pie_chart2, name="pie_chart2"),
    path('policys/', views.policys, name="policys"),
    path('feedback/', views.feedbackForm, name="feedbackForm"),
    
    
]