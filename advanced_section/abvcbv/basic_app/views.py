from django.shortcuts import render
from basic_app import models
from django.views.generic import View,TemplateView,ListView,DetailView


# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    template_name='basic_app/school_list.html'
class SchoolDetailView(DetailView):
    context_object_name='school_details'
    model= models.School
    template_name='basic_app/school_details.html'
