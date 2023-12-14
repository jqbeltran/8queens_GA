import random

def generate_queens(n):
    numbers = list(range(0, n))
    random.shuffle(numbers)
    return numbers

def fitness(queens_pos):
    temp = queens_pos.copy()
    num_conflicts = 0
    for i in range (1, len(queens_pos)):
        pos_row = len(temp) - 1
        pos_col = temp.pop()
        actual_row = 0
        for actual_col in temp:
            if actual_col == pos_col:
                num_conflicts += 1
            i, j = actual_row + 1, actual_col + 1
            while i < 8 and j < 8:
                if i == pos_row and j == pos_col:
                    num_conflicts += 1
                i += 1
                j += 1
            i, j = actual_row + 1, actual_col - 1
            while i < 8 and j >= 0:
                if i == pos_row and j == pos_col:
                    num_conflicts += 1
                i += 1
                j -= 1
            actual_row = actual_row + 1
    return num_conflicts

def selection(population):
    return sorted(population, key=lambda x: fitness(x))[:2]

def crossover(parent_1, parent_2):
    # Child 1
    point_1 = random.randint(0, len(parent_1) - 1)
    point_2 = random.randint(point_1, len(parent_1) - 1)
    child_1 = parent_1[point_1:point_2 + 1]
    for gen in parent_2:
        if gen not in child_1:
            child_1.append(gen)
    
    # Child 2
    point_1_2 = random.randint(0, len(parent_2) - 1)
    point_2_2 = random.randint(point_1_2, len(parent_2) - 1)
    child_2 = parent_2[point_1_2:point_2_2 + 1]
    for gen in parent_1:
        if gen not in child_2:
            child_2.append(gen)

    return child_1, child_2

def mutation(queens_pos, mutation_rate):
    queens_pos_mut = queens_pos.copy()
    if random.random() < mutation_rate:
        pos_1 = random.choice(range(0, len(queens_pos)))
        pos_2 = random.choice(range(0, len(queens_pos)))
        while (pos_1 == pos_2):
            pos_2 = random.choice(range(0, len(queens_pos)))
        temp = queens_pos_mut[pos_1]
        queens_pos_mut[pos_1] = queens_pos_mut[pos_2]
        queens_pos_mut[pos_2] = temp
    return queens_pos_mut

number_queens = 8
mutation_rate = 0.5
num_generations = 10
len_population = 10

population = [generate_queens(number_queens) for _ in range(len_population)]

for generation in range(num_generations):
    population = sorted(population, key=lambda x: fitness(x))
    if fitness(population[0]) == 0:
        print("Generación ", generation, ". La solución fue encontrada.")
        break
    parents = selection(population)
    children = crossover(parents[0], parents[1])
    population = population[:len_population - 1] + [mutation(children[0], mutation_rate), mutation(children[1], mutation_rate)]

solution = population[0]
print("Posible solución:", solution)