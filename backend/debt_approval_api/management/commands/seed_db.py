#!/usr/bin/env python
from debt_approval_api.models import Contract, DebtRequest, Item, Manufacturer
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        debt_request_1 = DebtRequest(name="debt request 1")
        debt_request_2 = DebtRequest(name="debt request 2")
        debt_request_1.save()
        debt_request_2.save()

        contract_1 = Contract(name="contract 1", debt_request=debt_request_1)
        contract_2 = Contract(name="contract 2", debt_request=debt_request_2)
        contract_1.save()
        contract_2.save()

        manufacturer_1 = Manufacturer(name="manufacturer 1")
        manufacturer_2 = Manufacturer(name="manufacturer 2")
        manufacturer_1.save()
        manufacturer_2.save()

        item_1 = Item(
            name="item 1",
            debt_request=debt_request_1,
            manufacturer=manufacturer_1,
        )
        item_2 = Item(
            name="item 2",
            debt_request=debt_request_1,
            manufacturer=manufacturer_2,
        )
        item_3 = Item(
            name="item 3",
            debt_request=debt_request_1,
            manufacturer=manufacturer_2,
        )
        item_4 = Item(
            name="item 3",
            debt_request=debt_request_2,
            manufacturer=manufacturer_2,
        )
        item_1.save()
        item_2.save()
        item_3.save()
        item_4.save()
