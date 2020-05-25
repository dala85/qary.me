"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.debug import default_urlconf
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from qary_app import views
from users import views as user_views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', default_urlconf),
    url(r'question/', views.home_view, name='question'),
    url(r'answer/', views.reply, name='answer'),
    url(r'^team/$', views.team, name='team'),
    url(r'^nlpia/$', views.nlpia, name='nlpia'),
    url(r'^post/', include('qary_post.urls')),
    url('register/', user_views.register, name='register'),
    url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url('profile/', user_views.profile, name='profile'),
    url('basic/<int:pk>/', views.API_objects_details.as_view(), name='basic')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
