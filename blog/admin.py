from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_posted", "likes")
    list_filter = ("date_posted",)
    ordering = ("-date_posted",)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)