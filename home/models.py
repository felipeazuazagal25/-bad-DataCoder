# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FileUpload(models.Model):
    test = models.CharField(max_length=16)
    rubric = models.FileField(upload_to='rubrics/')
    zip_file = models.FileField(upload_to='tests/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
