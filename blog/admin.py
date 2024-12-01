from django.contrib import admin
from .models import Category, Post, Announcement, Feedback

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Announcement)
admin.site.register(Feedback)
