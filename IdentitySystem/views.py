from django.contrib.auth import logout
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from .models import IdentityCard, Person, Authority, Region, Department, Borough, User, WantedPoster, Commissariat
from .serializers import IdentityCardSerializer, PersonSerializer, AuthoritySerializer, RegionSerializer, \
    DepartmentSerializer, BoroughSerializer, UserSerializer, LoginSerializer, WantedPosterSerializer, \
    CommissariatSerializer


class AuthorityCardViewSet(viewsets.ModelViewSet):
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer


class CommissariatViewSet(viewsets.ModelViewSet):
    queryset = Commissariat.objects.all()
    serializer_class = CommissariatSerializer


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


class SearchIdentityCardViewSet(viewsets.ModelViewSet):
    serializer_class = IdentityCardSerializer

    def get_queryset(self):
        input_string = self.kwargs.get('input_string')
        identity_cards = self.search_by_name_or_surname(input_string)
        serializer = self.get_serializer(identity_cards, many=True)
        return Response(serializer.data)

    def search_by_name_or_surname(self, input_string):
        identity_cards = IdentityCard.objects.filter(
            Q(given_name__icontains=input_string) | Q(surname__icontains=input_string)
        )
        return identity_cards


class IdentityCardViewSet(viewsets.ModelViewSet):
    queryset = IdentityCard.objects.all()
    serializer_class = IdentityCardSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['gender', 'isActive', 'PostedDate']
    search_fields = ['surname', 'given_name']


class WantedPosterViewSet(viewsets.ModelViewSet):
    queryset = WantedPoster.objects.all()
    serializer_class = WantedPosterSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['gender', 'isActive', 'PostedDate']
    search_fields = ['surname', 'given_name']


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

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WantedPosterByCommissariatViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WantedPosterSerializer

    def get_queryset(self):
        commissariat_id = self.kwargs.get('commissariat_id')
        if commissariat_id is None:
            return Response({'msg': "Need commissariat Id"}, status=status.HTTP_400_BAD_REQUEST)
        return Commissariat.objects.filter(fk_authority_id=commissariat_id)


class PersonByPlaceOfBirthViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BoroughSerializer

    def get_queryset(self):
        place_of_birth = self.kwargs.get('place_of_birth')
        if place_of_birth is None:
            return Response({'msg': "Need Place of birth"}, status=status.HTTP_400_BAD_REQUEST)
        return Borough.objects.filter(place_of_birth_id=place_of_birth)


class PersonByIdentityCardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IdentityCardSerializer

    def get_queryset(self):
        try:
            identity_card = self.kwargs.get('identity_card_id')
            return Person.objects.filter(fk_identity_card_id=identity_card)
        except IdentityCard.DoesNotExist:
            return Response({'message': 'Identity card not found'}, status=status.HTTP_404_NOT_FOUND)


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthViewSet(GenericViewSet):
    serializer_class = LoginSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

        # Log in the user if credentials are valid
        # ...

        # Generate the JWT token for the user
        this_user = User.objects.filter(email=email).first()
        refresh = RefreshToken()
        refresh['user_id'] = this_user.id
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response({'token': token, 'message': 'Login successful'}, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def logout(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
