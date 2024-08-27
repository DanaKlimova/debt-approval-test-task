from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DebtRequest(TimeStampMixin):
    name = models.CharField(max_length=200)


class Contract(TimeStampMixin):
    name = models.CharField(max_length=200)
    debt_request = models.OneToOneField(
        DebtRequest,
        on_delete=models.DO_NOTHING,
        related_name="contract",
    )


class Manufacturer(TimeStampMixin):
    name = models.CharField(max_length=200)


class Item(TimeStampMixin):
    name = models.CharField(max_length=200)
    debt_request = models.ForeignKey(
        DebtRequest,
        on_delete=models.DO_NOTHING,
        related_name="items",
    )
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
