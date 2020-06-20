from django.urls import path
from sizeapp.api import views

#app_name = 'sizeapp'
urlpatterns = [
    path('add_image/', views.ImageUploadView.as_view()),
    path('list/', views.ListView.as_view()),
    path('detail/<int:id>', views.DetailView.as_view()),
]