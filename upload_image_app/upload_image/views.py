from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ImageForm
from .models import Images, Account


def home(request):
    return render(request, 'home.html', {})


def upload_images(request):
    submitted = False
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return HttpResponseRedirect('my_images?submitted=True')
    else:
        form = ImageForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'upload.html', 
        {
            'form': form,
            'submitted': submitted,
        })


def my_images(request):
    if request.user.is_authenticated:
        images_list = Images.objects.filter(user=request.user)
        user_group = 'Enterprise'
        if Account.objects.filter(user=request.user).exists():
            text = Account.objects.get(user=request.user.id)
            name_group = text.group
        else:
            name_group = ""
        return render(request, 'my_images.html', 
            {
                'images_list': images_list,
                'user_group': user_group,
                'name_group': name_group,
            })
    else:
        return render(request, 'my_images.html', {})


def show_image(request, image_id, height):
    image = Images.objects.get(pk=image_id)
    return render(request, 'show_image.html',
        {
            'image': image,
            'height': height,
            })


