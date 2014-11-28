from django.db import models
from django.template.defaultfilters import slugify

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images", default="img/default.jpg")
    thumbnail = models.ImageField(upload_to="images", default="img/defaultThumb.jpg", blank=True, null=True)
    caption = models.TextField()
    rank = models.IntegerField()
    project = models.ForeignKey('Project')
    
    class Meta:
        ordering = ["rank"]

    def __unicode__(self):
        return self.title

class Addendum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    attachment = models.FileField(upload_to="addenda", blank=True, null=True)
    attachment_description = models.CharField(max_length=100, blank=True, null=True)
    project = models.ForeignKey('Project')
    rank = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "addenda"
        ordering = ["rank"]

    def __unicode__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    challenges = models.TextField(blank=True, null=True)
    solutions = models.TextField(blank=True, null=True)
    has_video = models.BooleanField(default=True)
    video_embed_code = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="projects", default="img/defaultThumb.jpg", blank=True, null=True)
    main_image = models.ImageField(upload_to="projects", default="img/default.jpg", blank=True, null=True)
    category = models.ForeignKey('Category')
    rank = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    
    class Meta:
        ordering = ["rank"]

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category) + '-' + slugify(self.title)
        super(Project, self).save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=30)
    rank = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ["rank"]

    def __unicode__(self):
        return self.title