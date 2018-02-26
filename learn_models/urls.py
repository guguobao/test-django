"""learn_models URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url ,patterns
from django.contrib import admin
from people import views
from users import urls as auth_urls
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',views.index),
    url(r'^add/$',views.add),
    url(r'^test/$',views.test),
    url(r'^index2/$',views.index2,name='index2'),
    url(r'^accounts/', include(auth_urls),name='accounts'),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', views.ajax_dict, name='ajax-dict'),
    url(r'^Ajax/',views.Ajax,name='Ajax'),
    url(r'^queryapi',views.queryapi,name='queryapi')
    #url(r'^accounts/$', include('people.users.urls'))
]

# urlpatterns = patterns('',
    
#     url(r'^accounts/', include('users.urls')),
    
# )
