from django.db import models
from django.db.models.signals import pre_save

from ecommerce_product.slug_generate import unique_slug_generator


# ///////////////////////////// Category Products \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class CategoryProducts(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def category_product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_product_pre_save_receiver, CategoryProducts)


# ///////////////////////////// Store Products \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class StoreProductsManager(models.Manager):
    pass


class StoreProducts(models.Model):
    LABEL_CHOICES = (
        ('sale', 'sale'),
        ('new', 'new'),
    )
    category = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to='StoreProducts/%y/%m/%d')
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)  # discount 40% to price
    label = models.CharField(choices=LABEL_CHOICES, max_length=20)
    slug = models.SlugField(blank=True, unique=True)
    description_short = models.CharField(max_length=200)
    description_long = models.TextField()
    is_active = models.BooleanField(default=True)
    available_count = models.IntegerField(default=1)

    objects = StoreProductsManager()

    def __str__(self):
        return f'{self.title}|{self.id}'


def store_product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(store_product_pre_save_receiver, StoreProducts)