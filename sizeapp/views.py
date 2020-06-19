from django.shortcuts import render
from sizeapp import models
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView, DetailView
'''
class CreateImageView(CreateView):
	model = models.Images
	fields = ['name', 'image']

class DetailImageView(DetailView):
	model = models.Images
	template_name = 'sizeapp/image_detail.html'

class IndexView(TemplateView):
	template_name = 'sizeapp/index.html'
'''