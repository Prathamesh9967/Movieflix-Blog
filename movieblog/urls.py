from django.contrib import admin
from django.urls import path , include
from movieblog import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , views.index , name='home'),
    path('contact/' , views.contact , name='contact'),
    path('search/' , views.search , name='search'),
    path('blog' , views.blog , name='post-list'),
    path('create/' , views.post_create , name='post-create'),
    path('post/<id>/' , views.post , name='post-detail'),
    path('post/<id>/update/' , views.post_update, name='post-update'),
    path('post/<id>/delete/' , views.post_delete , name='post-delete'),

    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
]