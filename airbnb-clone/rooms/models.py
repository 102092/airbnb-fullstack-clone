from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# from users import models as user_models


# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    # db에는 생성되지 않는, 추상화된 객체를 생성

    """ Abstract Item """

    name = models.CharField(max_length=140)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """RoomType Object Definition"""

    pass

    class Meta:
        verbose_name_plural = "Room Type"
        ordering = ["created"]


class Amenity(AbstractItem):

    """Amenity Object Definition"""

    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """Facility Model Definition"""

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """HouseRull Model Definition"""

    pass

    class Meta:
        verbose_name_plural = "Houser Rule"


class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)
    pass


class Room(core_models.TimeStampedModel):

    """ Room model definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()  # 0~24hours
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # "" 을 통해, 매개변수를 좀 더 유연하게 줄 수 있음!!
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    # 클래스내애서 무언가를 get할 때 사용? string으로
    def __str__(self):
        return self.name
