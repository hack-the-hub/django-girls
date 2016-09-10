from rest_framework import serializers
from .models import Organisation


class OrganisationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Organisation
        fields = '__all__'