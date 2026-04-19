from django.contrib import admin

from .models import User, Post, Candidate, Vote

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Candidate)
admin.site.register(Vote)
# Register your models here.
