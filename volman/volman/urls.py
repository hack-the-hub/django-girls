"""volman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

import charity.views
import volunteer.views

urlpatterns = [
    url(r'^charities/organisations$', charity.views.OrganisationList.as_view()),
    url(r'^charities/organisations/(?P<charity_id>[0-9]+)$', charity.views.OrganisationDetail.as_view(), name='organisation-detail'),

    url(r'^charities/clients$', charity.views.ClientList.as_view()),
    url(r'^charities/clients/(?P<pk>[0-9]+)$', charity.views.ClientDetail.as_view(), name='client-detail'),

    url(r'^charities/clients/(?P<code>[a-z\-]+)/organisations$', charity.views.OrganisationsByClient.as_view()),

    url(r'^charities/services$', charity.views.ServiceList.as_view()),
    url(r'^charities/services/(?P<pk>[0-9]+)$', charity.views.ServiceDetail.as_view(), name='service-detail'),
    url(r'^charities/classifications$', charity.views.ClassificationList.as_view()),
    url(r'^charities/classifications/(?P<pk>[0-9]+)$', charity.views.ClassificationDetail.as_view(), name='classification-detail'),

    url(r'^volunteers$', volunteer.views.ProfileList.as_view()),
    url(r'^volunteers/(?P<pk>[0-9]+)$', volunteer.views.ProfileDetail.as_view(),
        name='profile-detail'),

    # Additionally, we include login URLs for the browsable API.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)



