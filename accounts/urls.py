from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views as local_views
from . import api_views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
	url(r'^create_user/$', api_views.UserCreate.as_view()),
	url(r'^login/$', local_views.get_auth_token),
	url(r'^reset_password/$', local_views.set_password),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
