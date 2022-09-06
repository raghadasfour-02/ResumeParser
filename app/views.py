from django.shortcuts import render, redirect
from pyresparser import ResumeParser
from .models import Resume, UploadResumeModelForm
from django.contrib import messages
from django.conf import settings
from django.db import IntegrityError
import os

def homepage(request):
    if request.method == 'POST':
        Resume.objects.all().delete()
        file_form = UploadResumeModelForm(request.POST, request.FILES)
        files = request.FILES.getlist('resume')
        resumes_data = []
        if file_form.is_valid():
            for file in files:
                try:
                    # Step 1: File is saved
                    resume = Resume(resume=file)
                    resume.save()
                    
                    # Step 2: Information is extracted from file
                    parser = ResumeParser(os.path.join(settings.MEDIA_ROOT, resume.resume.name))
                    data = parser.get_extracted_data()
                    resumes_data.append(data)
                    resume.name=data.get('name')
                    resume.email=data.get('email')
                    resume.phone_number=data.get('phone_number')
                    if data.get('degree') is not None:
                        resume.education=', '.join(data.get('degree'))
                    else:
                        resume.education= None
                    resume.company_names=data.get('company_names')
                    resume.university_name=data.get('university_name')
                    if data.get('skills') is not None:
                        resume.skills=', '.join(data.get('skills'))
                    else:
                        resume.skills=None
                    if data.get('experience') is not None:
                        resume.experience=', '.join(data.get('experience'))
                    else:
                        resume.experience=None
                    resume.save()
                except IntegrityError:
                    messages.warning(request, 'Duplicate resume found:', file.name)
                    return redirect('homepage')
            resume = Resume.objects.all()
            messages.success(request, 'Resume has been successfully uploaded.')
            context = {
                'resume': resume,
            }
            return render(request, 'base.html', context)
    else:
        form = UploadResumeModelForm()
    return render(request, 'base.html', {'form': form})