from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Comments
from .serializer import ProjectSerializer, CommentsSerializer


class ProjectList(APIView):
  def get(self, request, format=None):
    all_projects = Projects.get_all()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)

class ProjectByDatabase(APIView):
  def get(self, request,database, format=None):
    all_projects = Projects.filter_database()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)

class ProjectByTools(APIView):
  def get(self, request, tools, format=None):
    all_projects = Projects.filter_tools()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)

class ProjectByLanguages(APIView):
  def get(self, request,languages, format=None):
    all_projects = Projects.filter_languages()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)

class ProjectByFrameworks(APIView):
  def get(self, request, framework,format=None):
    all_projects = Projects.filter_framework()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)



class CommentsList(APIView):
  def get(self, request, format=None):
    all_comments = Comments.get_all()
    serializers = CommentsSerializer(all_comments, many=True)
    return Response(serializers.data)
