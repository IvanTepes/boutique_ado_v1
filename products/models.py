from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=False)
    name = models.CharField(max_length=254, blank=False)
    category = models.ForeignKey('Category', null=True, blank=False,
                                 on_delete=models.SET_NULL)
    brand = models.ForeignKey(
        'Brand', null=True, blank=False, on_delete=models.SET_NULL)
    memory = models.ForeignKey(
        'Memory', null=True, blank=True, on_delete=models.SET_NULL)
    key_features = models.ForeignKey(
        'KeyFeatures', null=True, blank=False, on_delete=models.SET_NULL)
    manufacturer_logo = models.ForeignKey(
        'Brand', related_name='manufacturer_logo',
        null=True, blank=True, on_delete=models.SET_NULL)
    processor_brand = models.ForeignKey(
        'Brand', related_name='processor_brand',
        null=True, blank=True, on_delete=models.SET_NULL)

    description = models.TextField()
    has_side_banner = models.BooleanField(default=False, null=True, blank=True)
    side_banner = models.ImageField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)
    has_logo = models.BooleanField(
            default=True, null=True, blank=False)
    brand_logo = models.ImageField(null=True, blank=False)
    has_side_banner = models.BooleanField(default=False, null=True, blank=True)
    side_banner = models.ImageField(null=True, blank=True)
    website = models.URLField(max_length=1024, null=True, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.friendly_name

    """ def get_friendly_name(self):
        return self.friendly_name """


class Memory(models.Model):

    class Meta:
        verbose_name_plural = 'Memorys'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class KeyFeatures(models.Model):

    class Meta:
        verbose_name_plural = 'Key Features'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    feature_1 = models.TextField()
    feature_2 = models.TextField()
    feature_3 = models.TextField()
    feature_4 = models.TextField()
    feature_5 = models.TextField()

    def __str__(self):
        return self.friendly_name

    """ def get_friendly_name(self):
        return self.friendly_name """
