from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/%y/%m/%d')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def geturl(self):
        return reverse('Product.shop', args=[self.id])


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL)
    product_price = models.DecimalField(max_digits=10, decimal_places=0)
    product_count = models.PositiveBigIntegerField()
    product_cost = models.DecimalField(max_digits=10, decimal_places=0)
    # cost for sum all of Orders

    def __str__(self):
        return self.order


class Invoice(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL)
    invoice_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order


class Transaction(models.Model):
    STATUS_CHOICES = {
        ('pending', 'pending'),
        ('failed', 'failed'),
        ('completed', 'completed')
    }
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.invoice
