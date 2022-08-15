from rest_framework import serializers
from .models import Databases, Frameworks, Languages, Projects, Comments, Tools 



class ProjectSerializer(serializers.ModelSerializer):

  # languages = serializers.ReadOnlyField('languages.language')

  class Meta:
    model = Projects
    fields = ('id','name', 'details', 'date', 'languages', 'frameworks', 'tools', 'database', 'image')


class LanguagesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Languages
    fields = ('id','language')


class FrameworksSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Frameworks
    fields = ('id','framework')

class ToolsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Tools
    fields = ('id','tool')

class DatabasesSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Databases
    fields = ('id','database')


class CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comments
    fields = ('name', 'email',  'comment', 'design_rating', 'content_rating', 'user_rating', 'date', 'project')

