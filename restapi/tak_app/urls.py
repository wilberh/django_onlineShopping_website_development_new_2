"""tak_app URL Configuration

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



from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from api.api import v1_api

admin.autodiscover()

# api - uses "Tastypi" RESTful package
# restapi - uses Django RESTful package
urlpatterns = [
	url(r'^api/', include(v1_api.urls)),
	url(r'^restapi/', include('restapi.urls')),
    url(r'^admin/', admin.site.urls),
]


# urls (Django before 2.0) versus pattern (Django 2.0)
# OLD:  url(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
# NEW:  path('articles/<int:year>/', views.year_archive),



