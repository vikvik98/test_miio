from django.db import models
from owner.models import Owner

# Create your models here.



class RegularPlan(models.Model):
    CYCLE_CHOICES = (
        ("D", "Daily"),
        ("W", "Weekly")
    )

    TYPE_CHOICES = (
        ("TS", "simple"),
        ("TB", "bi-time"),
        ("TT", "tri-time")
    )

    UNIT_CHOICES = (
        ("KH", "KWH"),
        ("MN", "MIN")
    )

    name = models.CharField("Name of regular plan", max_length=200)
    tar_included = models.BooleanField("Tax included?", default=False)
    subscription = models.FloatField("it’s the monthly subscription for the user", default=0.0)
    cycle = models.CharField("if it’s daily or weekly", choices=CYCLE_CHOICES, max_length=1)
    type = models.CharField("if it’s daily or weekly", choices=TYPE_CHOICES, max_length=2)
    offer_iva = models.BooleanField("Tax included?", default=False)
    off_peak_price = models.FloatField("off peak price", default=0.0)
    peak_price = models.FloatField("peak price", default=0.0)
    unit = models.CharField("kwh or min", choices=UNIT_CHOICES, max_length=2)
    valid = models.BooleanField("Is valid?", default=True)
    publish = models.BooleanField("Published?", default=False)
    vat = models.IntegerField("can be from 1 to 100", default=1)
    owner = models.ForeignKey(Owner, on_delete=models.PROTECT, null=True)