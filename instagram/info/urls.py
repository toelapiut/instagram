from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^search/',views.search_results,name="searched_user"),
    url(r'^photo/(\d+)',views.image_reviews,name ='photo_comment'),
    url(r'^update/',views.image_update,name ='image_update'),
    url(r'^profile/(\d+)',views.user_profile,name ='profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)