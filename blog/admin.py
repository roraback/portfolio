from django.contrib import admin
from blog.models import Article, BlogCategory, BlogTag

class BlogTagInline(admin.TabularInline):
    model = BlogTag
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    filter_vertical = ('tags',)
    list_display = ('title', 'category', 'posted', 'login_required', 'published')
    exclude = ('slug',)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank')
    exclude = ('slug',)

class BlogTagAdmin(admin.ModelAdmin):
    model = BlogTag
    list_display = ('title', 'rank')
    exclude = ('slug',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogTag, BlogTagAdmin)
