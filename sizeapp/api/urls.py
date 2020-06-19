from django.urls import path
from sizeapp.api.views import ImageUploadView

app_name = 'account'
urlpatterns = [
  path('add_image', ImageUploadView.as_view()),
]