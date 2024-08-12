
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^",include("api_v1.urls")),
    path('accounts/', include('django.contrib.auth.urls')), # new
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
