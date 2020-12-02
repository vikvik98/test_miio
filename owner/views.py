from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, status
from owner.models import Owner
from owner.serializers import OwnerListSerializer, OwnerCreateSerializer, OwnerUpdateSerializer
from rest_framework.response import Response


# Create your views here.


class OwnerViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Owner.objects.get(pk=pk)
        except Owner.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        owners = Owner.objects.all()
        serializer = OwnerListSerializer(owners, many=True)
        return Response(serializer.data)

    def retrieve(self, request, owner_id, *args, **kwargs):
        instance = self.get_object(owner_id)
        serializer = OwnerListSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        serializer = OwnerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, owner_id, *args, **kwargs):
        instance = self.get_object(owner_id)
        serializer = OwnerUpdateSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, owner_id, *args, **kwargs):
        instance = self.get_object(owner_id)
        instance.user_django.delete()
        instance.delete()
        return Response({"detail": "Owner deleted."}, status=status.HTTP_204_NO_CONTENT)
