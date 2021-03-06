from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.gis import admin
from django.conf import settings
from django.contrib.auth.views import login, logout

from disasterinfosite import views

urlpatterns = [
   url(r'^admin/', include(admin.site.urls)),
   url(r'^accounts/login/$',  login),
   url(r'^accounts/logout/$', logout),
   url(r'^accounts/create_user/$', views.create_user),
   url(r'^accounts/update_profile/$', views.update_profile),
   url(r'^i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(url(r'^$', views.app_view, name='index'))
urlpatterns += i18n_patterns(url(r'^accounts/login/$',  login))
urlpatterns += i18n_patterns(url(r'^accounts/logout/$', logout))
urlpatterns += i18n_patterns(url(r'^accounts/create_user/$', views.create_user))
urlpatterns += i18n_patterns(url(r'^accounts/update_profile/$', views.update_profile))

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
