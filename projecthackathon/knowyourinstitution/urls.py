from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('home',views.dash,name='home'),
    path('logout',views.logout,name='logout'),
    path('review',views.review,name='review'),
    path('search',views.search,name='search'),
    path('review/<id>',views.show, name="showcollege")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
