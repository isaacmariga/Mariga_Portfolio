from django.urls import path, include
from . import views, api_views



urlpatterns = [
  path('', views.welcome,name = 'test'),
  path('api/all_projects/', api_views.ProjectList.as_view())

]
