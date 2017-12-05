from enum import Enum 

# items array format:
# [[weight1, value1], [weight2, value2] ... [weightn, valuen]]

def exhaustive(items, capacity):
    possibleSolutions = 2 ** len(items)

    max_value = -1
    optimal_items = []

    for i in range(possibleSolutions):
        decision_matrix = [int(d) for d in str(bin(i)[2:]).zfill(len(items))]

        current_weight = -1
        current_value = -1 
        
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
    pass


init_items_arr = [[3, 25],
                  [2, 20],
                  [1, 15],
                  [4, 40],
                  [5, 50]]

exhaustive(init_items_arr, 6)
