from django.contrib import admin
from projects.models import Image, Addendum, Project, Category, Video

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class AddendumInline(admin.TabularInline):
    model = Addendum
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline, AddendumInline, VideoInline]
    list_display = ('title', 'category', 'rank')
    exclude = ('slug',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'rank')

admin.site.register(Image)
admin.site.register(Addendum)
admin.site.register(Video)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)