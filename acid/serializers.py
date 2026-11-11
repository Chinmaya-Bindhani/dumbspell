from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    accountNumber = serializers.CharField(max_length=64, allow_blank=False)
    amount = serializers.DecimalField(max_digits=12, decimal_places=2, min_value=0)
    transactionType = serializers.ChoiceField(choices=("DEBIT", "CREDIT"))
    time = serializers.DateTimeField()


class DuplicateCheckRequestSerializer(serializers.Serializer):
    transactions = TransactionSerializer(many=True, allow_empty=True)
