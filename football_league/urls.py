"""football_league URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("football_league.apps.public.urls")),
    path("account/", include("football_league.apps.accounts.urls"))
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
    # path("account/profile/", views.ProfileView.as_view(), name="profile"),
    # Django auth
    # path(
    #     "account/login/",
    #     auth_views.LoginView.as_view(template_name="account/login.html"),
    #     name="login",
    # ),
    # path(
    #     "account/logout/",
    #     auth_views.LogoutView.as_view(),
    #     name="logout",
    # ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
