"""
URL configuration for expproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_views.homepage, name="homepage"),
    path("reviews/<int:review_id>/", main_views.review_page, name="review_page"),
    path("services/", main_views.services, name="services"),
    path("booking/", main_views.booking, name="booking"),
    path("reviews/", main_views.reviews, name="reviews"),
    path("contacts/", main_views.contacts, name="contacts"),
    path("submit_review/", main_views.submit_review, name="submit_review"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path("accounts/", include("django.contrib.auth.urls"))]

handler404 = "main.views.handler404"
