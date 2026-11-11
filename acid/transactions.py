from collections import defaultdict
from datetime import timedelta


def find_duplicate_transactions(transactions):
    groups = defaultdict(list)

    for transaction in transactions:
        key = (
            transaction["accountNumber"],
            transaction["amount"],
            transaction["transactionType"],
        )
        groups[key].append(transaction)

    duplicates = []
    window = timedelta(minutes=5)

    for matching_transactions in groups.values():
        matching_transactions.sort(key=lambda item: item["time"])

        previous_time = None
        for transaction in matching_transactions:
            current_time = transaction["time"]
            if previous_time is not None and current_time - previous_time <= window:
                duplicates.append(transaction)
            previous_time = current_time
    duplicates.sort(key=lambda item: item["time"])
    return duplicates
