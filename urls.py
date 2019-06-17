"""lawhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from LawyersHub import views
from django.contrib.auth.views import (password_reset, password_reset_done,
                                       password_reset_complete, password_reset_confirm)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.index, name="index"),
                  url(r'^home/$', views.home, name="home"),
                  url(r'^contactin/$', views.contactin, name='contactin'),
                  url(r'^contactout/$', views.contactout, name='contactout'),
                  url(r'^Login/$', views.Login, name='Login'),
                  url(r'^signup/$', views.signup, name='signup'),
                  url(r'^profile/$', views.lawyer_profile, name='profile'),
                  url(r'^lawyer_signup/$', views.lawyer_signup, name="lawyer_signup"),
                  url(r'^talk_to_lawyer/$', views.talk, name='talk_to_lawyer'),
                  url(r'^lawyers/$', views.lawyers, name="lawyers"),
                  url(r'^family/$', views.family, name="family"),
                  url(r'^property/$', views.property, name="property"),
                  url(r'^criminal/$', views.criminal, name="criminal"),
                  url(r'^civil/$', views.civil, name="civil"),
                  url(r'^labour/$', views.labour, name="labour"),
                  url(r'^taxation/$', views.tax, name="tax"),
                  url(r'^reset-password/$', password_reset, name="reset_password"),
                  url(r'^reset-password/done/$', password_reset_done, name="password_reset_done"),
                  url(r'^reset-password/complete/$', password_reset_complete, name="password_reset_complete"),
                  url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                      password_reset_confirm, name="password_reset_confirm"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
