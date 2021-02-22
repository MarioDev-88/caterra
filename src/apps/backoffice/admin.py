from django.contrib import admin

from .models import Slider, MonthOffer, Post, Video


class PostAdminManager(admin.ModelAdmin):
    exclude = ("slug",)


admin.site.register(Slider)
admin.site.register(MonthOffer)
admin.site.register(Video)
admin.site.register(Post, PostAdminManager)
