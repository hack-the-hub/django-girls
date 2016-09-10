from django.conf import settings
from django.db import models


class Organisation(models.Model):
    """An entity which offers charitable services"""
    charity_id = models.CharField(max_length=50, help_text="Charity ID",
                    unique=True, default='')
    name = models.CharField(max_length=50, help_text="Name of the Organisation")
    registered = models.DateField(help_text="Date Charity was registered")
    address = models.TextField(help_text="Public address")
    website = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    mission = models.TextField(default='')
    clients = models.ManyToManyField('Client')
    services = models.ManyToManyField('Service')
    classifications = models.ManyToManyField('Classification')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    """Reference table of the types of client an organisation is trying to help"""
    code = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Service(models.Model):
    """Reference table of the types of people an organisation is trying to help"""
    code = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Classification(models.Model):
    """Reference table of Organisation classifications"""
    code = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Owners(models.Model):
    """Users with permissions to edit the properties and attributes of
    an Organisation"""

    organisation = models.ForeignKey(Organisation)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)


class Followers(models.Model):
    """List of users that have chosen to follow an Organisation"""
    organisation = models.ForeignKey(Organisation)
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("organisation", "volunteer"), )