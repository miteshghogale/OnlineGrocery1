from django.db import models


STATUS_CHOICE = (
    ('pending', 'Pending'),
    ('delivered', 'Delivered'),
    ('cancelled, Cancelled'),
    ('On_the_way', 'On the way'),
)




class OrderDetails(models.Model):
    user = models.IntegerField(default=True)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    qty = models.PositiveIntegerField(default=1)
    price = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='pending',)