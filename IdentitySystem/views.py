from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import IdentityCard, Person, Authority, Region, Department, Borough
from .serializers import IdentityCardSerializer, PersonSerializer, AuthoritySerializer, RegionSerializer, \
    DepartmentSerializer, BoroughSerializer


class AuthorityCardViewSet(viewsets.ModelViewSet):
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentByRegionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        region_id = self.kwargs.get('region_id')
        if region_id is None:
            return Response({'msg': "Need region Id"}, status=status.HTTP_400_BAD_REQUEST)
        return Department.objects.filter(fk_region_id=region_id)


class BoroughViewSet(viewsets.ModelViewSet):
    queryset = Borough.objects.all()
    serializer_class = BoroughSerializer


class BoroughByDepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BoroughSerializer

    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        if department_id is None:
            return Response({'msg': "Need department Id"}, status=status.HTTP_400_BAD_REQUEST)
        return Borough.objects.filter(fk_department_id=department_id)


class IdentityCardViewSet(viewsets.ModelViewSet):
    queryset = IdentityCard.objects.all()
    serializer_class = IdentityCardSerializer


class IdentityCardByAuthorityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IdentityCardSerializer

    def get_queryset(self):
        authority_id = self.kwargs.get('authority_id')
        if authority_id is None:
            return Response({'msg': "Need authority Id"}, status=status.HTTP_400_BAD_REQUEST)
        return IdentityCard.objects.filter(fk_authority_id=authority_id)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
