from django.contrib import admin
from django.urls import path
from loanWeb import views

urlpatterns = [
    path("",views.index,name='loanWeb'),
    path("index",views.index,name='loanWeb'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("blog",views.blog,name='blog')

]

