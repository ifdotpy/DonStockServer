"""DonStockServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from REST.views import check_token, LogoutSessionView, add_shop, append_shops, get_all_shops_for_user

urlpatterns = [
                  url(r'^api/admin/', admin.site.urls),
                  url(r'^api/', include('REST.urls')),

                  url(r'^api/login/', include('rest_social_auth.urls_jwt')),
                  url(r'^api/login/', include('rest_social_auth.urls_token')),
                  url(r'^api/login/', include('rest_social_auth.urls_session')),
                  url(r'^api/logout/session/$', LogoutSessionView.as_view(), name='logout_session'),
                  url(r'^api/auth/', include('rest_framework_social_oauth2.urls')),
                  url(r'^api/check/', check_token),
                  url(r'^api/add_shop/', add_shop),
                  url(r'^api/append_shops/', append_shops),
                  url(r'^api/my-shops/', get_all_shops_for_user),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
