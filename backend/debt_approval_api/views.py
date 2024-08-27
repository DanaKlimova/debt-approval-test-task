from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse

from .models import Contract


def get_manufacturers(request, contract_id):
    # TODO: optimize the query
    try:
        contract = Contract.objects.get(id=contract_id)
    except ObjectDoesNotExist:
        raise Http404

    items = contract.debt_request.items.all()
    manufacturer_ids = {item.manufacturer.id for item in items}
    return JsonResponse({"manufacturer_ids": list(manufacturer_ids)})
