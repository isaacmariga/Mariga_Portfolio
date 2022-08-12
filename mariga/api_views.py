from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects
from .serializer import ProjectSerializer


class ProjectList(APIView):
  def get(self, request, format=None):
    all_projects = Projects.get_all()
    serializers = ProjectSerializer(all_projects, many=True)
    return Response(serializers.data)
