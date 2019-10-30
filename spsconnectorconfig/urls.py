"""spsconnectorconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

# import views
from pages.views import home_view, contact_view
from userinfo.views import userinfo_detail_view, userinfo_create_view
from configurator.views import (
                    instance_view, 
                    mqtt_config_view, 
                    sql_config_view, 
                    base_view,
                    #InstanceView,
                )

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('create/', userinfo_create_view),
    path('userinfo/', userinfo_detail_view),
    path('admin/', admin.site.urls),
    path('configurator/mqtt/', mqtt_config_view),
    path('configurator/sql/', sql_config_view),
    path('configurator/instance/', instance_view),
    # as_view() turn the class based view into a function based view
    #path('configurator/instanceGENERIC/', InstanceView.as_view()),
    path('configurator/', base_view),
]

