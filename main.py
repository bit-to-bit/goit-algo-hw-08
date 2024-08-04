"""Calculate min cables connection cost"""

import heapq
import random

NUMBER_OF_ITEMS = 5
MAX_LENGTH = NUMBER_OF_ITEMS * 2

if __name__ == "__main__":
    cables = [random.randint(1, MAX_LENGTH) for _ in range(NUMBER_OF_ITEMS)]
    print(f"Набір кабелів: {cables}")
    heapq.heapify(cables)
    connection_order = [heapq.heappop(cables) for _ in range(len(cables))]
    amount = 0
    j = 0
    for i in connection_order:
        if j > 1:
            amount += amount
        amount += i
        j += 1
    print(f"Порядок з'єднання кабелів: {connection_order}")
    print(f"Загальна мінімальна сума витрат: {amount}")
