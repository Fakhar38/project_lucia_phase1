from django.db import models
import uuid
import os
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from phone_field import PhoneField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractUser


def image_file_path(instance, filename):
    """
        returns the filepath to upload the image to
    """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    filepath = os.path.join('user_profile_pic/', filename)
    return filepath


class User(AbstractUser):
    """
    User model for the users of this system
    """
    age = models.DateField(blank=True, null=True,
                           help_text='YYYY-MM-DD')
    country = CountryField(blank=True, null=True)
    phone = PhoneField(blank=True, help_text='Contact Number')
    thumbnail = ProcessedImageField(
        default='default_user_thumb.jpg',
        upload_to=image_file_path,
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 100},
    )
