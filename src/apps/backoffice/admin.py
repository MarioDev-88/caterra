from django.contrib import admin

from .models import Slider, Post, Video, Propiedad, Image


class PostAdminManager(admin.ModelAdmin):
    exclude = ("slug",)


admin.site.register(Slider)
admin.site.register(Video)
admin.site.register(Propiedad)
admin.site.register(Image)
admin.site.register(Post, PostAdminManager)
