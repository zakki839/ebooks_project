"""
URL configuration for ebooks_project project.

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
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

# Include the i18n path for translations
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# Add i18n_patterns for other paths
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('ebooks_app.urls')),  # The empty path here routes to your main app
    path('blogs/', include('ebooks_blogs.urls')),  # Example of another app
)


