"""
URL configuration for argentinaencombo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views as core_views
from cuyo import views as cuyo_views
from django.conf import settings

urlpatterns = [
    path('',core_views.home, name="home"),
    path('destinos', core_views.destinos, name="destinos"),
    path('buenos_aires',core_views.buenos_aires, name="buenos_aires"),
    path('consulta_clima', core_views.consulta_clima, name="consulta_clima"),
    path('centro', core_views.centro, name="centro"),
    path('cuyo', cuyo_views.cuyo, name="cuyo"),
    path('noreste', core_views.noreste, name="noreste"),
    path('noroeste', core_views.noroeste, name="noroeste"),
    path('patagonia', core_views.patagonia, name="patagonia"),
    path('imperdibles', core_views.imperdibles, name="imperdibles"),
    path('tips', core_views.tips, name="tips"),
    path('contacto', core_views.contacto, name="contacto"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)