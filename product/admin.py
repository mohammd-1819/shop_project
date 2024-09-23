from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


@admin.register(models.ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user')


admin.site.register(models.Category)
admin.site.register(models.Color)
admin.site.register(models.Size)
