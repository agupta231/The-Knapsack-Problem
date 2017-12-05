from enum import Enum

class item_array(Enum):
    WEIGHT = 0
    VALUE = 1

def exhaustive(items, capacity):
    possibleSolutions = 2 ** len(items)

    max_value = -1
    optimal_items = []

    for i in range(possibleSolutions):
        decision_matrix = [int(d) for d in str(i)]

        current_weight = -1
        current_value = -1 
        
        for j in range(decision_matrix):
            if decision_matrix[j] == 1:
                current_weight += items[i][item_array.WEIGHT]
                current_value += items[i][item_array.VALUE]

        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            optimal_items = decision_matrix


def dynamic(): 
    pass
