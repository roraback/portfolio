from django.db import models
from datetime import date
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    body = RichTextUploadingField()
    created = models.DateField(auto_now_add=True)
    posted = models.DateField(default=date.today, db_index=True)
    category = models.ForeignKey('BlogCategory')
    tags = models.ManyToManyField('BlogTag')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    login_required = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["posted"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

class BlogCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    rank = models.IntegerField(blank=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogCategory, self).save(*args, **kwargs)

class BlogTag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    rank = models.IntegerField(blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogTag, self).save(*args, **kwargs)
