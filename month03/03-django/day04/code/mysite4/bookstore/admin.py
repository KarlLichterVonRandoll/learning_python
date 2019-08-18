from django.contrib import admin

# Register your models here.

from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price']
    list_display_links = ['id', 'title']
    list_filter = ["pub"]
    search_fields = ['title', 'pub']
    list_editable = ['market_price']


admin.site.register(models.Book, BookAdmin)  # 将Book类注册为可管理页面


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email', 'wife']
    list_display_links = ['name']
    list_filter = ["name"]
    search_fields = ['name']
    list_editable = ['email']


admin.site.register(models.Author, AuthorAdmin)  # 将Book类注册为可管理页面


class WifeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    list_display_links = ['name']
    list_filter = ["name"]
    search_fields = ['name']


admin.site.register(models.Wife, WifeAdmin)  # 将Book类注册为可管理页面
