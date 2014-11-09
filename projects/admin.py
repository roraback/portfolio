from django.contrib import admin
from projects.models import Image, Addendum, Project, Category

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class AddendumInline(admin.TabularInline):
    model = Addendum
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline, AddendumInline]

admin.site.register(Image)
admin.site.register(Addendum)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)