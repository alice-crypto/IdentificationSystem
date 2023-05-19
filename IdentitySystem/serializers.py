from abc import ABC
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import IdentityCard, Person, Authority, Region, Department, Borough, User
from rest_framework import serializers


class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = '__all__'


class BoroughSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borough
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    boroughs = BoroughSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = '__all__'


class IdentityCardSerializer(serializers.ModelSerializer):
    authorities = AuthoritySerializer(many=True, read_only=True)

    class Meta:
        model = IdentityCard
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    fk_identity_card = IdentityCardSerializer()
    place_of_birth = BoroughSerializer(many=True, read_only=True)
    photo = serializers.FileField(required=False)

    class Meta:
        model = Person
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'phone']
        extra_kwargs = {
            'username': {'required': False},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'phone': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        return RefreshToken(validated_data['refresh'])

    def update(self, instance, validated_data):
        pass


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = User.objects.filter(email=email).first()

            if user:
                if not user.check_password(password):
                    raise serializers.ValidationError('Invalid password')
            else:
                raise serializers.ValidationError('Invalid email')

        else:
            raise serializers.ValidationError('Email and password are required')

        attrs['user'] = user
        return attrs
