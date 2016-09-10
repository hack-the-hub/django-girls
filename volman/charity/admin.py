from django.contrib import admin

from .models import Classification, Client, Organisation, Service, Followers

admin.site.register(Classification)
admin.site.register(Client)
admin.site.register(Organisation)
admin.site.register(Service)
admin.site.register(Followers)