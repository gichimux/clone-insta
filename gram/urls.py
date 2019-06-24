from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^posts/',views.home,name='home'),
    url(r'^new/insta_post$', views.new_image, name='new_image'),
    url(r'^profile/(?P<username>[-_\w.]+)/$',views.profile,name='profile'),
    url(r'^profile/(?P<username>[-_\w.]+)/edit/$',views.edit_profile_info,name='edit_profile'),
    url(r'^$',views.registration,name='registration')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)