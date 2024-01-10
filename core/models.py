from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from ckeditor_uploader.fields import RichTextUploadingField

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING = (
    (1,  "★☆☆☆☆"),
    (2,  "★★☆☆☆"),
    (3,  "★★★☆☆"),
    (4,  "★★★★☆"),
    (5,  "★★★★★"),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20,
                         prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="Room")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
class Tags(models.Model):
    pass

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20,
                         prefix="ven", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="Fyp Home")
    address = models.CharField(max_length=100, default="123 Main Street.")
    contact1 = models.CharField(max_length=100, default="+123 (456) 789")
    contact2 = models.CharField(max_length=100, default="+123 (456) 789")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name_plural = "Vendors"


    def __str__(self):
        return self.title
    

class Residence(models.Model):
    Rid = ShortUUIDField(unique=True, length=10,
                         max_length=20, alphabet="abcdefgh12345")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category")
    vendor = models.ForeignKey(
        Vendor, on_delete=models.SET_NULL, null=True, related_name="Residence")
    title = models.CharField(max_length=100, default="FYP home")
    image = models.ImageField(
        upload_to=user_directory_path, default="Residence.jpg")
    description = RichTextUploadingField(null=True, blank=True, default="This is the Redidence")
    policies = RichTextUploadingField(null=True, blank=True, default="This is the Redidence")
    features = RichTextUploadingField(null=True, blank=True, default="This is the Redidence")
    facilities = RichTextUploadingField(null=True, blank=True, default="This is the Redidence")

    price = models.DecimalField(
        max_digits=99999999999999, decimal_places=2, default="000")
    old_price = models.DecimalField(
        max_digits=99999999999999, decimal_places=2, default="000")
    address = models.CharField(max_length=100, default="123 Main Street.")
    # specifications = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    type = models.CharField(
        max_length=100, default="Not couple friendly", null=True, blank=True)

    Residence_status = models.CharField(
        choices=STATUS, max_length=10, default="in_review")
    
    
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10,
                        prefix="sku", alphabet="1234567890")
    
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Residences"

    def Residence_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_precentage(self):
        new_price = (100 - (self.price / self.old_price) * 100)
        return new_price


class ResidenceImages(models.Model):
    images = models.ImageField(
        upload_to="Residence-images", default="Residence.jpg")
    Residence = models.ForeignKey(
        Residence, related_name="R_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Residence Images"

class ResidenceReviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Residence = models.ForeignKey(
        Residence, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Residence Reviews"


    def __str__(self):
        return self.Residence.title

    def get_rating(self):
        return self.rating

class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Residence = models.ForeignKey(Residence, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "wishlists"

    def __str__(self):
        return self.Residence.title


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    mobile1 = models.CharField(max_length=300, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"
