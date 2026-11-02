from random import random, randint, choices, randrange, seed
import numpy as np

GENERATIONS = 500
POPULATION_SIZE = 100
INDIVIDUAL_LENGTH = 25
CROSSOVER_PROB = 0.8
MUTATION_PROB = 0.1
MUTATION_FLIP_PROB = 1 / INDIVIDUAL_LENGTH

EXPERIMENT_COUNT = 10


def create_individual(length):
    return [randint(0, 1) for _ in range(length)]


def create_population(size):
    return [create_individual(INDIVIDUAL_LENGTH) for _ in range(size)]


def selection(population, fitnesses):
    return choices(population, fitnesses, k=POPULATION_SIZE)


# 1-point crossover
def cross(individual1, individual2):
    point = randrange(INDIVIDUAL_LENGTH)
    offspring1 = individual1[:point] + individual2[point:]
    offspring2 = individual1[:point] + individual2[point:]
    return offspring1, offspring2


def crossover(population):
    offspring = []
    for p1, p2 in zip(population[0::2], population[1::2]):
        o1, o2 = p1[:], p2[:]
        if random() < CROSSOVER_PROB:
            o1, o2 = cross(p1[:], p2[:])
        offspring.append(o1)
        offspring.append(o2)
    return offspring


def mutate(individual):
    for i in range(INDIVIDUAL_LENGTH):
        if random() < MUTATION_FLIP_PROB:
            individual[i] = 1 - individual[i]
    return individual[:]


def mutation(population):
    offspring = []
    for individual in population:
        if random() < MUTATION_PROB:
            offspring.append(mutate(individual))
        else:
            offspring.append(individual)
    return offspring[:]


def one_max_fitness(individual):
    return sum(individual)


def alternating_fitness(individual):
    fitness = 0
    for i in range(len(individual) - 1):
        fitness += individual[i] != individual[i + 1]
    return fitness


def evolutionary_algorithm(fitness):
    logs = []
    population = create_population(POPULATION_SIZE)
    for gen in range(GENERATIONS):
        fits = list(map(fitness, population))
        logs.append((gen, max(fits), sum(fits) / 100, gen * POPULATION_SIZE))
        mating_pool = selection(population, fits)
        offspring = crossover(mating_pool)
        offspring = mutation(offspring)
        population = offspring[:]
    return population, logs


if __name__ == "__main__":
    logs = []
    best = [0] * INDIVIDUAL_LENGTH

    # f = one_max_fitness
    f = alternating_fitness
    for i in range(EXPERIMENT_COUNT):
        seed(i)
        pop, log = evolutionary_algorithm(f)
        best = max([*pop, best], key=f)
        logs.append(log)
    evals = []
    best_fit = []
    for log in logs:
        evals.append([l[3] for l in log])
        best_fit.append([l[1] for l in log])

    evals = np.array(evals)
    best_fit = np.array(best_fit)
    import matplotlib.pyplot as plt

    print(f"Best: {best}, fitness: {f(best)}")
    title = f"Crossover: {CROSSOVER_PROB}, Mutation: {MUTATION_PROB}, Flip: {round(MUTATION_FLIP_PROB, 4)}"
    fig = plt.figure(num=title.replace(".", ""))
    plt.plot(evals[0, :], np.median(best_fit, axis=0), label="Median")
    plt.plot(evals[0, :], np.max(best_fit, axis=0), label="Best individual")
    plt.fill_between(
        evals[0, :],
        np.percentile(best_fit, q=25, axis=0),
        np.percentile(best_fit, q=75, axis=0),
        alpha=0.2,
    )
    plt.title(title)
    plt.legend()
    plt.show()
