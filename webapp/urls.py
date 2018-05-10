from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', login_required(views.ProjectListView.as_view()), name='projects_list'),
    re_path(r'^project/(?P<pk>\d+)/detail/', login_required(views.ProjectDetail.as_view()), name='project_detail'),
    re_path(r'^project/new/$', login_required(views.ProjectCreate.as_view()), name='project_new'),
    re_path(r'^project/(?P<pk>\d+)/edit/$', login_required(views.ProjectUpdate.as_view()), name='project_edit'),
    re_path(r'^project/(?P<pk>\d+)/remove/$', login_required(views.ProjectDelete.as_view()), name='project_remove'),
    re_path(r'^project/(?P<pk>\d+)/start/$', views.project_start, name='project_start'),
    re_path(r'^project/(?P<pk>\d+)/detener/$', views.project_stop,name='project_stop'),


]
