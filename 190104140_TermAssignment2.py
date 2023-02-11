# Python code for Simulation of Random Restart Hill Climbing using 8-Queen Problem
import random

def generate_radom_state():
    new_state = list()
    for i in range(8):
        new_state.append(random.randint(1, 8))
    return new_state

def calculate_heuristic(state):
    # h3 heuristic value (number of atatcking pair) for 8-Queen Problem
    h_value = 0
    for i in range(1, 9):
        for j in range(i+1, 9):
            # Checking for attacking position face to face
            if (state[i-1] == state[j-1]):
                h_value += 1
            # Checking for attacking position diagonally
            if (abs(i - j) == abs(state[i-1] - state[j-1])):
                h_value += 1
    return h_value

def calculate_fitness(state):
    # Max value of fitness can be 28 (max number of attacking pair for 8-Queen)
    return 28 - calculate_heuristic(state)


input_state = input("Current state of board for 8-Queen : ")
state = list(map(int, input_state))
goal_fitness = int(input("Goal fitness (max 28) : "))

fitness = calculate_fitness(state)

f = open("intermediate_states.txt", "w") 

if(fitness == goal_fitness):
    print("Fitness of given state is same as Goal Fitness.")
else:
    print("Initial Fitness: ", fitness)
    flag = False
    while (1):
        for i in range(8):
            state[i] = random.randint(1, 8)
            new_fitness = calculate_fitness(state)
            print("\tCurrent State: ", state, "Fitness:", new_fitness)
            f.write("Current State" + str(state) + " Fitness: " + str(new_fitness) + "\n")

            if (new_fitness > fitness):
                fitness = new_fitness
            elif (new_fitness == fitness):
                print("Local Maxima Reached,\n\tFitness value: ", new_fitness)
                print("Restarting Randomly!\n")
                f.write("Local Maxima Reached, Restarting Randomly!\n\n")

                state = generate_radom_state()
                fitness = calculate_fitness(state)
                print("\tCurrent State: ", state, "Fitness:", fitness)
            
            if(fitness >= goal_fitness):
                flag = True
                print("Goal fitness found with state, ", state)
                break;
        if flag == True :
            break;
            
if (fitness == 28):
    print("\nGlobal Maxima Reached with state ", state)
