from django.contrib import admin

from course.models import Course


# Register your models here.
@admin.register(Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner',)
