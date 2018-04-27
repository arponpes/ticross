from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'activiti-journals', views.ActivityJournalViewSet)
router.register(r'registrys', views.RegistryViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include((router.urls, 'api'), namespace='api')),
    re_path(r'^api-auth/', include('rest_framework.urls',
                                   namespace='rest_framework')),
]
