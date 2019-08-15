"""metrodeclaracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views




from declaracion.views import (
    CreateView,
    UpdateView,
    ListView,
    DeclaracionPDF,
    DeclaracionHTML,
    DeclaracionPNG,
)


urlpatterns = [
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^nueva$', CreateView.as_view(), name='create'),
    url(r'^d/(?P<pk>\d+)$', UpdateView.as_view(), name='update'),
    url(r'^d/(?P<pk>\d+)/html$', DeclaracionHTML.as_view(), name='html'),
    url(r'^d/(?P<pk>\d+)/pdf$', DeclaracionPDF.as_view(), name='pdf'),
    url(r'^d/(?P<pk>\d+)/png$', DeclaracionPNG.as_view(), name='png'),
    url( r'^login/$',auth_views.LoginView.as_view() , name="login"),
    url(r'^logout/$', auth_views.LogoutView, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
]
