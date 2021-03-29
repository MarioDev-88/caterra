import uuid

from django.db import models

from apps.users.models import User


class Order(models.Model):

    ORDER_STATUS = [
        ("DELIVERED","DELIVERED"),
        ("SENT", "SENT"),
        ("PAIDOUT", "PAIDOUT"),
        ("PENDING", "PENDING")
    ]

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    info_name = models.CharField("Cliente", max_length=255)
    info_business_name = models.CharField("Nombre de la empresa", max_length=255)
    info_address_1 = models.CharField("Dirección", max_length=255)
    info_address_2 = models.CharField("Colonia", max_length=255)
    info_country = models.CharField("País", max_length=255)
    info_state = models.CharField("Estado", max_length=255)
    info_city = models.CharField("Ciudad", max_length=255)
    info_cp = models.CharField("CP", max_length=10)
    info_email = models.EmailField("Email", max_length=255)
    info_phone = models.CharField("Teléfono", max_length=50)
    info_comments = models.TextField("Comentarios")
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField("Estado del pedido", max_length=255, choices=ORDER_STATUS)

    def __str__(self):
        return str(self.order_id)


class OrderItem(models.Model):
    product_id = models.CharField("Admin ID", max_length=20)
    qty = models.IntegerField("Cantidad")
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)

    def __str__(self):
        return self.product_id
