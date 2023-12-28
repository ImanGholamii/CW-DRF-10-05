from django.db import models
from accounts.models import MyUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    image = models.ImageField(verbose_name='ItemImage', upload_to='images/user_uploads', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class CustomerOrder(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="user_customer_orders")
    item = models.ManyToManyField(
        Item, related_name="item_customer_order")
    item_quantity = models.IntegerField()
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class SellRecord(models.Model):
    order = models.ForeignKey(
        CustomerOrder, on_delete=models.CASCADE)
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="user_sell_record")
    date = models.DateField()

    def __str__(self):
        return f'{self.date}'
