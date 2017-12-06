from enum import Enum 

# items array format:
# [[weight1, value1], [weight2, value2] ... [weightn, valuen]]

def exhaustive(items, capacity):
    possibleSolutions = 2 ** len(items)

    max_value = -1
    optimal_items = []

    for i in range(possibleSolutions):
        decision_matrix = [int(d) for d in str(bin(i)[2:]).zfill(len(items))]

        current_weight = 0 
        current_value = 0 
        
        for j in range(len(decision_matrix)):
            if decision_matrix[j] == 1:
                current_weight += items[j][0]
                current_value += items[j][1]

        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            optimal_items = decision_matrix

    print(max_value)
    print(optimal_items)


def dynamic(items, capacity): 
    memoization_table = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]
    keep_table = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        current_item = i - 1

        for j in range(capacity + 1):
            if j - items[current_item][0] >= 0:
                if items[current_item][1] + memoization_table[i - 1][j - items[current_item][0]] > memoization_table[i - 1][j]:
                    memoization_table[i][j] = items[current_item][1] + memoization_table[i - 1][j - items[current_item][0]]
                    keep_table[i][j] = 1
                else:
                    memoization_table[i][j] = memoization_table[i - 1][j]

                # memoization_table[i][j] = max(memoization_table[i - 1][j], items[current_item][1] + memoization_table[i - 1][j - items[current_item][0]])

            else:
                memoization_table[i][j] = memoization_table[i - 1][j]

    i = len(items)
    j = capacity
    optimal_items = [0 for x in range(len(items))]

    while i > 0 and j > 0:
        if memoization_table[i][j] != memoization_table[i - 1][j]:
            optimal_items[i - 1] = 1
            j -= items[i - 1][0]

        i -= 1

    for row in memoization_table:
        print(row) 

    for row in keep_table:
        print(row)

    print(optimal_items)

init_items_arr = [[3, 25],
                  [2, 20],
                  [1, 15],
                  [4, 40],
                  [5, 50]]

exhaustive(init_items_arr, 6)
dynamic(init_items_arr, 6)
