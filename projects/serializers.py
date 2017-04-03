from django.contrib.auth.models import User, Group
from projects.models import Project, Category, Addendum, Image
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class AddendumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Addendum
        fields = ('title', 'description', 'attachment', 'attachment_description', 'rank')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('title', 'image', 'caption', 'rank')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    addendum_set = AddendumSerializer(many=True)
    image_set = ImageSerializer(many=True)
    class Meta:
        model = Project
        depth = 1

class ProjectPreviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'thumbnail', 'rank', 'slug', 'id')

class CategorySerializer(serializers.ModelSerializer):
    project_set = ProjectPreviewSerializer(many=True)

    class Meta:
        model = Category
        fields = ('title', 'rank', 'project_set')
