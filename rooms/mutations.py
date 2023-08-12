from django.db import transaction
import strawberry
from strawberry.types import Info
import typing
from enum import Enum
from categories.models import Category
from .models import Room, Amenity


@strawberry.enum
class RoomKindChoices(Enum):
    ENTIRE_PLACE = "ENTIRE_PLACE"
    PRIVATE_ROOM = "PRIVATE_ROOM"
    SHARED_ROOM = "SHARED_ROOM"


def add_room(
    info: Info,
    name: str,
    country: typing.Optional[str] = "KOREA",
    city: typing.Optional[str] = "SEOUL",
    price: typing.Optional[int] = 100,
    address: typing.Optional[str] = "Gangnam",
    rooms: int = 1,
    toilets: int = 1,
    description: typing.Optional[str] = "Nice place",
    pet_friendly: bool = True,
    kind: RoomKindChoices = RoomKindChoices.ENTIRE_PLACE,
    amenities: typing.List[int] = [1],
    category: int = 1,
):
    try:
        category = Category.objects.get(pk=category)
        if category.kind == Category.CategoryKindChoices.EXPERIENCE:
            raise Exception("Experience category is not allowed")
    except Category.DoesNotExist:
        raise Exception("Category does not exist")

    try:
        with transaction.atomic():
            room = Room.objects.create(
                name=name,
                country=country,
                city=city,
                price=price,
                address=address,
                rooms=rooms,
                toilets=toilets,
                description=description,
                pet_friendly=pet_friendly,
                kind=kind.value,
                owner=info.context.request.user,
                category=category,
            )
            for amenity_pk in amenities:
                amenity = Amenity.objects.get(pk=amenity_pk)
                room.amenities.add(amenity)
            room.save()
            return room
    except Exception:
        raise Exception("Can't create room")
