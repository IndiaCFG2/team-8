from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),

    path('question/<int:ques_pk>/',views.question_detail,name="question_detail"),

    path('dashboard/add',views.create_policy,name='create-policy'),
    
]