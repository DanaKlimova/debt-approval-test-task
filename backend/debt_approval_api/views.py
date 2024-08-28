from django.http import Http404, JsonResponse

from .models import Contract, Item


def get_manufacturers(request, contract_id):
    try:
        # Fetch contract with related debt_request in one query
        contract = Contract.objects.select_related("debt_request").get(id=contract_id)
    except Contract.DoesNotExist:
        raise Http404

    # Fetch unique manufacturer IDs directly from the database
    manufacturer_ids = Item.objects.filter(
        debt_request=contract.debt_request
    ).values_list("manufacturer_id", flat=True).distinct()

    return JsonResponse({"manufacturer_ids": list(manufacturer_ids)})


"""
Queries:
(0.001) SELECT "debt_approval_api_contract"."id", "debt_approval_api_contract"."created_at", "debt_approval_api_contract"."name", "debt_approval_api_contract"."debt_request_id", "debt_approval_api_debtrequest"."id", "debt_approval_api_debtrequest"."created_at", "debt_approval_api_debtrequest"."name" 
        FROM "debt_approval_api_contract" 
        INNER JOIN "debt_approval_api_debtrequest" ON ("debt_approval_api_contract"."debt_request_id" = "debt_approval_api_debtrequest"."id") 
        WHERE "debt_approval_api_contract"."id" = 1 LIMIT 21; args=(1,); alias=default
(0.000) SELECT DISTINCT "debt_approval_api_item"."manufacturer_id" 
        FROM "debt_approval_api_item" 
        WHERE "debt_approval_api_item"."debt_request_id" = 1; args=(1,); alias=default
"""
