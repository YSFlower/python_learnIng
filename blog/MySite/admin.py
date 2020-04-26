from django.contrib import admin
from .models import Banner, Category, Tag, Tui, Article, Link

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')

    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    # list_editable = ['title', 'user']

    # fk_fields 设置显示外键字段
    # fk_fields = ['category']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display =  ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')