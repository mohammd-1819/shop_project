from django.db import models
from account.models import User


class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Color(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='products')
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to='img/products')
    size = models.ManyToManyField(Size, blank=True, related_name='products')
    color = models.ManyToManyField(Color, blank=True, related_name='products')
    has_color = models.BooleanField(default=False)
    has_size = models.BooleanField(default=False)
    availibility = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
