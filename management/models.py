import uuid
from django.db import models
from django.contrib.auth.models import User


class AbstractDatedObject(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='+', null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='+', null=True, blank=True)

    class Meta:
        abstract = True


class AbstractSimpleObject(AbstractDatedObject):
    object_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=40, null=False, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta(AbstractDatedObject.Meta):
        abstract = True
        ordering = [
            'name'
        ]

    def __str__(self):
        return "{0}".format(self.name)


class ProductType(AbstractSimpleObject):
    pass


class RepostApp(AbstractSimpleObject):
    pass


class Product(AbstractDatedObject):
    object_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=False)
    is_posted_to_other = models.BooleanField(default=False)
    need_repost = models.ManyToManyField(RepostApp, blank=True)

    name = models.CharField(max_length=255)
    type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(blank=True, null=True)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    # location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name='products')

    class Meta(AbstractDatedObject.Meta):
        indexes = [
            models.Index(fields=['name', 'price']),
        ]

    def __str__(self):
        return "{0}".format(self.name)


