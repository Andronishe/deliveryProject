from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# class Customer(models.Model):
#     name = models.CharField(max_length=40, verbose_name='имя')
#     telephone = models.CharField(max_length=20, verbose_name='телефон')
#     email = models.EmailField(max_length=50, verbose_name='email')
#     address = models.CharField(max_length=40, verbose_name='адрес')


class Courier(models.Model):
    name = models.CharField(max_length=40, verbose_name='имя')
    telephone = models.CharField(max_length=20, verbose_name='телефон')
    delivery_type = models.CharField(max_length=40, verbose_name='имя')


class Order(models.Model):
    date_get = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courier = models.ManyToManyField(Courier, through="DeliveryList")


class DeliveryList(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date_arrived = models.DateTimeField(verbose_name='дата доставки')
    payment_method = models.CharField(max_length=10)


class Product(models.Model):
    name = models.CharField(max_length=40, verbose_name='товар')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name='фото')
    price = models.IntegerField(verbose_name='цена')
    order = models.ManyToManyField(Order, through="OrdersProducts")
    favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})


class OrdersProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='кол-во')




