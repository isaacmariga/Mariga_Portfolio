from rest_framework import serializers
from .models import Projects, Comments


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ('name', 'details', 'date', 'languages', 'frameworks', 'tools', 'database', 'image')


class CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comments
    fields = ('name', 'email',  'comment', 'design_rating', 'content_rating', 'user_rating', 'date', 'project')

