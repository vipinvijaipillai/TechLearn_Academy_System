from django.contrib import admin
from . models import Course, Student, Trainer
# Register your models here.


class courseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'duration']
    list_display_links = ['course_name', 'duration']
    list_filter = ['course_name']
    search_fields = ['course_name']


class trainerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'expertise']
    list_display_links = ['full_name', 'email', 'expertise']
    search_fields = ['full_name', 'email', 'expertise']

class studentAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'enrolled_course', 'trainer']
    list_display_links = ['full_name', 'email', 'enrolled_course', 'trainer']
    list_display = ['full_name', 'email', 'enrolled_course', 'trainer']
    search_fields = ['full_name', 'email', 'enrolled_course', 'trainer']


admin.site.register(Course, courseAdmin)
admin.site.register(Trainer, trainerAdmin)
admin.site.register(Student, studentAdmin)
