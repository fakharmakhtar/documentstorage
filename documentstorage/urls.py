"""
URL configuration for documentstorage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from rest_framework.routers import DefaultRouter

from documents.views import DocumentViewSet, FolderViewSet, TopicViewSet, DocumentView

router = DefaultRouter()
router.register(r'topics', TopicViewSet, basename='topic')
router.register(r'documents', DocumentViewSet, basename='documents')
router.register(r'folders', FolderViewSet, basename='folder')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("data/<str:file_name>/", DocumentView.as_view())
]

urlpatterns += router.urls
