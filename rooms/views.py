from django.db import transaction
from rest_framework import generics, status
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from rest_framework.response import Response

from .models import Amenity, Room
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer
from categories.models import Category


class Amenities(generics.ListCreateAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer


class AmenityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer


class Rooms(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer

    def perform_create(self, serializer):
        category_pk = serializer.validated_data.get("category")
        if not category_pk:
            raise ParseError("Category is required.")

        try:
            category = Category.objects.get(pk=category_pk)
            if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                raise ParseError("The category kind should be 'rooms'")
        except Category.DoesNotExist:
            raise ParseError("Category not found")

        amenities = self.request.data.get("amenities", [])
        with transaction.atomic():
            room = serializer.save(owner=self.request.user, category=category)
            room.amenities.set(amenities)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise NotAuthenticated()
        return super().post(request, *args, **kwargs)


class RoomDetail(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomDetailSerializer
