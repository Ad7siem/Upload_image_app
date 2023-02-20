from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload_images, name='upload-images'),
    path('upload_image', views.upload_images, name='u-i'),
    path('my_images', views.my_images, name='my-images'),
    path('show_image/<image_id>/<height>', views.show_image, name='show-image'),
]
