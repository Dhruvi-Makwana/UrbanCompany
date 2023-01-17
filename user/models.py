from django.db import models

# Create your models here.
from django.db import models


from django.contrib.auth.models import AbstractUser


USER = "user"
MERCHANT = "merchant"

USER_ROLE_CHOICE = ((USER, "user"), (MERCHANT, "merchant"))

SKIN_CARE_FOR_WOMEN = "skin care for women"
PAINTING = "Painting"
AC_REPAIR = "A/C or 2Applicences Repair"
HAIR_STUDIO = "Hair Studio"
NAIL_STUDIO = "Nail Studio For Women"
KITCHEN_CLEANING = "Kitchen Cleaning"
PLUMBERS = "Plumbers"
MAN_SALOON = "saloon for man"

CATEGORY_CHOICE = (
    (SKIN_CARE_FOR_WOMEN, "skin care for women"),
    (PAINTING, "Painting"),
    (AC_REPAIR, "AC or Applicences Repair"),
    (HAIR_STUDIO, "Hair Studio"),
    (NAIL_STUDIO, "Nail Studio For Women"),
    (KITCHEN_CLEANING, "Kitchen Cleaning"),
    (PLUMBERS, "Plumbers"),
    (MAN_SALOON, "saloon for man"),
)

SUN = "SUN"
MON = "MON"
TUE = "TUE"
WED = "WED"
THU = "THU"
FRI = "FRI"
SAT = "SAT"
WEEKCODE_CHOICE = (
    (SUN, "SUN"),
    (MON, "MON"),
    (TUE, "TUE"),
    (WED, "WED"),
    (THU, "THU"),
    (FRI, "FRI"),
    (SAT, "SAT"),
)


class Address(models.Model):
    address_line1 = models.TextField(max_length=200)
    city_name = models.CharField(max_length=50)
    state_name = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)
    def __str__(self):
        return f"{self.address_line1}"


class Category(models.Model):
    category = models.CharField(
        choices=CATEGORY_CHOICE, blank=True, null=True, max_length=50
    )
    photo = models.ImageField(
        upload_to="profile/", height_field=None, width_field=None, max_length=100
    )
    is_deleted = models.BooleanField(default=False)


class Store(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    latitude = models.DecimalField(max_length=20, max_digits=17, decimal_places=8)
    longitude = models.DecimalField(max_length=20, max_digits=17, decimal_places=8)
    add_prefix = models.TextField(max_length=100)
    merchant_address = models.ForeignKey(
    Address, on_delete=models.CASCADE, related_name="merchant_address"
    )
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name="categorychoice")
    image = models.ImageField(
        upload_to="profile/", height_field=None, width_field=None, max_length=100
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    mobile_number = models.CharField(max_length=10)
    role = models.CharField(
        choices=USER_ROLE_CHOICE, blank=True, max_length=30, default=USER
    )

    store_name = models.ManyToManyField(Store, related_name="user",blank=True)
    user_address = models.ForeignKey(
        Address, blank=True, null=True, on_delete=models.CASCADE
    )
    user_profile = models.ImageField(
        upload_to="user_profile/",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return f"{self.username}"


class SetWeekDays(models.Model):
    code = models.CharField(choices=WEEKCODE_CHOICE, max_length=20)
    name = models.CharField(max_length=20)
    store_name = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="store_name",
    )
    start_time = models.TimeField(blank=True, null=True,default='10:00')
    end_time = models.TimeField(blank=True, null=True,default='18:00')

    def __str__(self):
        return f"{self.name} ,{self.code}"
