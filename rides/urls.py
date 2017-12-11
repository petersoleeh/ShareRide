from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^accounts/profile/',views.profile,name='profile'),
    url(r'^rider/',views.rider,name='rider'),
    url(r'^car/update/',views.update_car,name='update-car'),
    url(r'^car/new/',views.new_car,name='new-car')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
