from rest_framework import serializers
from .models import IdentityCard, Person, Authority, Region, Department, Borough


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

    class Meta:
        model = Person
        fields = '__all__'
