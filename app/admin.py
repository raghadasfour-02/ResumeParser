from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeParserAdmin(admin.ModelAdmin):
    pass