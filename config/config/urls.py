"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from ajax_select import urls as ajax_select_urls

from django.conf.urls.static import static
from apps.Almacen.views import*
from apps.Almacen.urls import*
from bootstrap_customizer import urls as bootstrap_customizer_urls
from rest_framework import serializers, viewsets, routers

admin.autodiscover()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path(r'adminactions/', include('adminactions.urls')),
    #path('', include('admin_favorite.urls')),
    path('datawizard/', include('data_wizard.urls')),
    path('router/', include(router.urls)),
    path(r'admin/', include('massadmin.urls')),
    #path('admin_tools_stats/', include('admin_tools_stats.urls')), 
    path('', include('apps.Almacen.urls')),
    path('admin/', admin.site.urls),
    path('bootstrap_customizer/', include(bootstrap_customizer_urls)),
    path('api-auth/', include('rest_framework.urls')),
    path(r'ajax_select/', include(ajax_select_urls)),
    #url(r'advanced_filters/', include('advanced_filters.urls')),
   


    

 ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
