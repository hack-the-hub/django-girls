from .models import Classification, Client, Organisation, Service
from .serializers import ClassificationSerializer, ClientSerializer, OrganisationSerializer, ServiceSerializer
from rest_framework import generics


class OrganisationList(generics.ListCreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer


class OrganisationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    lookup_field = "charity_id"


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrganisationsByClient(generics.ListAPIView):
    serializer_class = OrganisationSerializer

    def get_queryset(self):
        client = self.kwargs['code']
        return Organisation.objects.filter(clients__code=client)


class ClassificationList(generics.ListCreateAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ClassificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


