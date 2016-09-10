from rest_framework import serializers
from .models import Classification, Client, Organisation, Service


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ServiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class ClassificationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Classification
        fields = '__all__'


class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    clients = ClientSerializer(required=False, many=True)
    services = ServiceSerializer(required=False, many=True)
    classifications = ClassificationSerializer(required=False, many=True)

    url = serializers.HyperlinkedIdentityField(
        view_name='organisation-detail',
        lookup_field='charity_id'
    )

    class Meta:
        model = Organisation
        fields = '__all__'

