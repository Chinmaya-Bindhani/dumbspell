from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import DuplicateCheckRequestSerializer
from .transactions import find_duplicate_transactions


@api_view(["POST"])
def check_duplicates(request):
    serializer = DuplicateCheckRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    duplicates = find_duplicate_transactions(serializer.validated_data["transactions"])
    return Response(
        {
            "duplicateCount": len(duplicates),
            "duplicates": [
                {
                    "accountNumber": item["accountNumber"],
                    "amount": str(item["amount"]),
                    "transactionType": item["transactionType"],
                    "time": item["time"].isoformat(),
                }
                for item in duplicates
            ],
        },
        status=status.HTTP_200_OK,
    )
