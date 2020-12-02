from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from regularPlans.models import RegularPlan


class RegularPlanListSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegularPlan
        fields = (
            "id",
            "name",
            "tar_included",
            "subscription",
            "cycle",
            "type",
            "offer_iva",
            "off_peak_price",
            "peak_price",
            "unit",
            "valid",
            "publish",
            "vat",
            "owner"
        )


class RegularPlanCreateSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if not data.get("name", None):
            raise serializers.ValidationError({"name": "Required."})

        if data.get("cycle", None).upper() != "D" and data.get("cycle", None).upper() != "W":
            raise serializers.ValidationError({"cycle": 'Cycle must be "D" or "W".'})

        if data.get("type", None).upper() != "TS" and data.get("type", None).upper() != "TB" and data.get("type", None).upper() != "TT":
            raise serializers.ValidationError({"type": 'Type must be "TS", "TB" or "TT".'})

        if data.get("unit", None).upper() != "KH" and data.get("unit", None).upper() != "MN":
            raise serializers.ValidationError({"unit": 'Cycle must be "KH" or "MN".'})

        if data.get("owner") is None and data.get("publish") is False:
            raise serializers.ValidationError({"owner": "The owner can only be null if publish is equal to true."})

        if data.get("vat") < 1 or data.get("vat") > 100:
            raise serializers.ValidationError({"vat": "Vat must be between 1 and 100."})

        return data

    class Meta:
        model = RegularPlan
        fields = (
            "id",
            "name",
            "tar_included",
            "subscription",
            "cycle",
            "type",
            "offer_iva",
            "off_peak_price",
            "peak_price",
            "unit",
            "valid",
            "publish",
            "vat",
            "owner"
        )

    @transaction.atomic
    def create(self, validated_data):
        regularPlan = RegularPlan(
            name=validated_data['name'],
            tar_included=validated_data['tar_included'],
            subscription=validated_data['subscription'],
            cycle=validated_data['cycle'].upper(),
            type=validated_data['type'].upper(),
            offer_iva=validated_data['offer_iva'],
            off_peak_price=validated_data['off_peak_price'],
            peak_price=validated_data['peak_price'],
            unit=validated_data['unit'].upper(),
            valid=validated_data['valid'],
            publish=validated_data['publish'],
            vat=validated_data['vat'],
            owner=validated_data['owner']
        )

        regularPlan.save()
        return regularPlan


class RegularPlanUpdateSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if not data.get("name", None):
            raise serializers.ValidationError({"name": "Required."})

        if data.get("cycle", None).upper() != "D" and data.get("cycle", None).upper() != "W":
            raise serializers.ValidationError({"cycle": "Cycle must be 'D' or 'W'."})

        if data.get("type", None).upper() != "TS" and data.get("type", None).upper() != "TB" and data.get("type",
                                                                                                          None).upper() != "TT":
            raise serializers.ValidationError({"type": "Type must be 'TS', 'TB' or 'TT'."})

        if data.get("unit", None).upper() != "KH" and data.get("unit", None).upper() != "MN":
            raise serializers.ValidationError({"unit": "Cycle must be 'KH' or 'MN'."})

        if data.get("owner") is None and data.get("owner") is False:
            raise serializers.ValidationError({"owner": "The owner can only be null if publish is equal to true."})

        if data.get("vat") < 1 or data.get("vat") > 100:
            raise serializers.ValidationError({"vat": "Vat must be between 1 and 100."})

        return data

    class Meta:
        model = RegularPlan
        fields = (
            "id",
            "name",
            "tar_included",
            "subscription",
            "cycle",
            "type",
            "offer_iva",
            "off_peak_price",
            "peak_price",
            "unit",
            "valid",
            "publish",
            "vat",
            "owner"
        )

    @transaction.atomic
    def update(self, instance, validated_data):

        instance.name=validated_data['name']
        instance.tar_included=validated_data['tar_included']
        instance.subscription=validated_data['subscription']
        instance.cycle=validated_data['cycle']
        instance.type=validated_data['type']
        instance.offer_iva=validated_data['offer_iva']
        instance.off_peak_price=validated_data['off_peak_price']
        instance.peak_price=validated_data['peak_price']
        instance.unit=validated_data['unit']
        instance.valid=validated_data['valid']
        instance.publish=validated_data['publish']
        instance.vat=validated_data['vat']
        instance.owner=validated_data['owner']
        instance.save()

        return validated_data