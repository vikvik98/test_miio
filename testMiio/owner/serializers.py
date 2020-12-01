from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from owner.models import Owner
from regularPlans.serializers import RegularPlanListSerializer


class OwnerListSerializer(serializers.ModelSerializer):
    regular_plans = serializers.SerializerMethodField()

    class Meta:
        model = Owner
        fields = (
            "id",
            "name",
            "regular_plans"
        )

    def get_regular_plans(self, obj):
        return RegularPlanListSerializer(obj.regularplan_set.all(), many=True).data


class OwnerCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    def validate(self, data):

        if not data.get("email", None):
            raise serializers.ValidationError({"email": "Required."})

        if User.objects.filter(email=data['email']):
            raise serializers.ValidationError({"email": "This email is already registered in our database."})

        return data

    class Meta:
        model = Owner
        fields = (
            "id",
            "name",
            "email",
            "password"
        )

    @transaction.atomic
    def create(self, validated_data):
        user = User(
            email=validated_data['email'].lower(),
            username=validated_data['email'].lower()
        )
        user.set_password(validated_data['password'])
        user.save()

        owner = Owner(
            name=validated_data['name'],
            user_django=user
        )

        owner.save()
        return owner


class OwnerUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = Owner
        fields = (
            "id",
            "name",
            "email",
            "password"
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        user = User.objects.get(id=instance.user_django.pk)
        user.email = validated_data['email'].lower()
        user.username = validated_data['email'].lower()
        user.set_password(validated_data['password'])
        user.save()

        instance.name=validated_data['name']
        instance.user_django=user
        instance.save()

        return validated_data