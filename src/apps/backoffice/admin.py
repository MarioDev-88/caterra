from django.contrib import admin

from .models import Slider, Post, Video


class PostAdminManager(admin.ModelAdmin):
    exclude = ("slug",)


admin.site.register(Slider)
admin.site.register(Video)
admin.site.register(Post, PostAdminManager)
