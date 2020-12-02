from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from regularPlans.models import RegularPlan
from regularPlans.serializers import RegularPlanListSerializer, RegularPlanCreateSerializer, RegularPlanUpdateSerializer
from rest_framework.response import Response


# Create your views here.


class RegularPlanViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return RegularPlan.objects.get(pk=pk)
        except RegularPlan.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        regularPlans = RegularPlan.objects.all()
        if request.GET.get("publish", None) == "true":
            regularPlans = regularPlans.filter(publish=True)

        if "name_owner" in request.GET:
            regularPlans = regularPlans.filter(owner__name__icontains=request.GET.get("name_owner"))

        serializer = RegularPlanListSerializer(regularPlans, many=True)
        return Response(serializer.data)

    def retrieve(self, request, regualar_plan_id, *args, **kwargs):
        instance = self.get_object(regualar_plan_id)
        serializer = RegularPlanListSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = RegularPlanCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, regualar_plan_id, *args, **kwargs):
        instance = self.get_object(regualar_plan_id)
        serializer = RegularPlanUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, regualar_plan_id, *args, **kwargs):
        instance = self.get_object(regualar_plan_id)
        instance.delete()
        return Response({"detail": "RegularPlan deleted."}, status=status.HTTP_204_NO_CONTENT)