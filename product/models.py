from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name_plural="Categories"
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=56)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products", blank=True, null=True)
    price = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} > {self.category} > {self.price}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='product/')

    def __str__(self):
        return self.product.name


class Attribute(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name


class AttributeUnit(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    unit = models.ForeignKey(AttributeUnit, on_delete=models.CASCADE, related_name='value', blank=True, null=True)
    value = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes', blank=True, null=True)

    def __str__(self):
        return f'{self.attribute.name} > {self.value} > {self.product}'
