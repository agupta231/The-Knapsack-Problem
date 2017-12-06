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

    return optimal_items


def dynamic(items, capacity): 
    memoization_table = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        current_item = i - 1

        for j in range(capacity + 1):
            if j - items[current_item][0] >= 0:
                if items[current_item][1] + memoization_table[i - 1][j - items[current_item][0]] > memoization_table[i - 1][j]:
                    memoization_table[i][j] = items[current_item][1] + memoization_table[i - 1][j - items[current_item][0]]
                else:
                    memoization_table[i][j] = memoization_table[i - 1][j]

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

    return optimal_items


def greedy(items, capacity):
    complete_array = []
    
    for i in range(len(items)):
        complete_array.append([i, items[i][0], items[i][1], items[i][1] / items[i][0]])
    
    complete_array = sorted(complete_array, key=lambda x: x[3])

    remaining_space = capacity
    optimal_items = [0 for x in range(len(items))]
    i = len(complete_array) - 1

    while remaining_space > 0 and i >= 0:
        if remaining_space - complete_array[i][1] >= 0:
            optimal_items[complete_array[i][0]] = 1
            remaining_space -= complete_array[i][1]

        i-= 1

    return optimal_items


def UI():
    program_active = True

    while program_active:
        user_choice = input("Would you like to (l)oad a file or (q)uit?")
        
        if user_choice == "l":
            try:
                fn = input("Input the name of the input file (default=input-1.txt): ")

                if fn == "":
                    fn = "input-1.txt" 

                capacity = None
                weight_arr = None
                value_arr = None
                items_arr = []

                with open(fn, "r") as fh:
                    line_count = 0

                    for line in fh:
                        if line_count == 0:
                           capacity = int(line)
                        elif line_count == 1:
                            weight_arr = line.split(",")
                        elif line_count == 2:
                            value_arr = line.split(",")

                        line_count += 1

                for i in range(len(weight_arr)):
                    items_arr.append([int(weight_arr[i]), int(value_arr[i])])

                print(capacity)
                print(items_arr)

                e_result = exhaustive(items_arr, capacity)
                d_result = dynamic(items_arr, capacity)
                g_result = greedy(items_arr, capacity)

                e_sol = decision_to_subset(items_arr, e_result)
                d_sol = decision_to_subset(items_arr, d_result)
                g_sol = decision_to_subset(items_arr, g_result)

                print("Exhaustive search solution:     " + str(e_sol[0]) + 
                        " optimal subset: " + str(e_sol[1]))
                print("Dynamic search solution:        " + str(d_sol[0]) + 
                        " optimal subset: " + str(d_sol[1]))
                print("Chosen(greedy) search solution: " + str(g_sol[0]) + 
                        " optimal subset: " + str(g_sol[1]))

                program_active = False

            except IOError:
                print("Error: file not found")

        elif user_choice == "q":
            print("Oki, doki. Have a great day!")
            program_active = False
            break

        else:
            print("Choice not recognized: Please enter either 'l' or 'q'")


def decision_to_subset(items, decision):
    subset = []
    solution = 0
    
    for i in range(len(decision)):
        if decision[i] == 1:
            subset.append(items[i])
            solution += items[i][1]

    return (solution, subset)

UI()
