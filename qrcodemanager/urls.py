"""qrcodemanager URL Configuration

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
import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

urlpatterns = [
    path('', include('qrcodegen.urls')),
    path('admin/', admin.site.urls),
    # Support legacy links inside templates that point to .html files
    path('ativos.html', RedirectView.as_view(pattern_name='ativos', permanent=False)),
    path('inativos.html', RedirectView.as_view(pattern_name='inativos', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static('/assets/', document_root=os.path.join(settings.BASE_DIR, 'templates', 'assets'))

# Serve assets even when the page URL is nested (templates use relative paths)
urlpatterns += [
    re_path(r'^(?:.*/)?assets/(?P<path>.*)$',
            lambda request, path: settings.DEBUG and __import__('django.views.static').views.static.serve(
                request,
                path,
                document_root=os.path.join(settings.BASE_DIR, 'templates', 'assets')
            )),
]

# Enable /static/... via staticfiles finders in development
urlpatterns += staticfiles_urlpatterns()
