from django.contrib import admin
from projects.models import Image, Addendum, Project, Category

admin.site.register(Image)
admin.site.register(Addendum)
admin.site.register(Project)
admin.site.register(Category)