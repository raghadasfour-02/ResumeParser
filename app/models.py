from django.db import models
from django import forms
from django.forms import ClearableFileInput

class Resume(models.Model):
    resume=models.FileField('Upload Resume', upload_to='resume/')
    name=models.CharField('Name', max_length=255, null=True, blank=True)
    email=models.CharField('Email', max_length=255, null=True, blank=True)
    phone_number=models.CharField('Phone Number',  max_length=255, null=True, blank=True)
    education= models.CharField('Education', max_length=255, null=True, blank=True)
    skills=models.CharField('Skills', max_length=1000, null=True, blank=True)
    company_name=models.CharField('Company Name', max_length=1000, null=True, blank=True)
    university_name=models.CharField('University/College Name', max_length=1000, null=True, blank=True)
    experience=models.CharField('Experience', max_length=1000, null=True, blank=True)
    uploaded_on=models.DateTimeField('Uploaded On', auto_now_add=True)

class UploadResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume']
        widgets = {
            'resume': ClearableFileInput(attrs={'multiple': True}),
        }