from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.RegisterUser.as_view(), name='signup')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)