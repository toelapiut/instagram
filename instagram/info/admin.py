from django.contrib import admin

# Register your models here.
from .models import Thread,Article,Comment

admin.site.register(Thread)
admin.site.register(Article)
admin.site.register(Comment)