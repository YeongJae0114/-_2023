from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','img','content','created_at', 'view_count', 'writer')


admin.site.register(Comment)

# Register your models here.
