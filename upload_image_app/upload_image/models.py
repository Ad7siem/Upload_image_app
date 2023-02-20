from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from django.core.signing import Signer


class Images(models.Model):
    image = models.ImageField(upload_to="images/")
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    thumbnail_200 = ImageSpecField(source='image',
                                    processors=[ResizeToFit(200)],
                                    format='JPEG',
                                    options={'quality':100})
    thumbnail_400 = ImageSpecField(source='image',
                                    processors=[ResizeToFit(400)],
                                    format='JPEG',
                                    options={'quality':100})


class Account(models.Model):
    name_group = (
        ('B', 'Basic'),
        ('P', 'Premium'),
        ('E', 'Enterprise')
    )
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    group = models.CharField(max_length=20 ,choices=name_group)



