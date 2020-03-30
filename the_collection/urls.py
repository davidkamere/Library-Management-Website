from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'the_collection'
urlpatterns = [
    # Landing Page
    url(r'^$', views.index, name='index'),
    # search
    url(r'^search/$', views.search_posts, name='search-posts'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
