import csv
import math
import random

#Variabel
n_populasi = 10
n_tournament = 5
n_kromosom = 15
p_c = 0.7
p_m = 0.3
saham = []

#Membuka file csv yang berisikan data-data saham perusahaan
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        saham.append(int(row['Terakhir']))


#populasi awal
def generatePop(n_populasi, n_kromosom):
    pop = []
    for i in range(n_populasi):
        krom = []
        for y in range(n_kromosom):
            krom.append((random.randint(-100, 100)) / 100)
        pop.append(krom)
    return pop


#decode kromosom
def mod(x):
    return round((x - math.floor(x / 1) * 1), 2)


def decodeKrom(krom=[]):
    while len(krom) < 11:
        krom.insert(0, mod(krom[0] + krom[1]))
    while len(krom) >= 12:
        krom[1] = mod(krom[0] + krom[1])
        krom.pop(0)
    return krom


#Fitness
def fitness(krom=[]):
    fitness = 0
    for i in range(len(saham) - 11, 1, -1):
        prediksi = krom[0]
        for y in range(10):
            prediksi += krom[y + 1] * saham[i + y + 1]
        temp = saham[i] - prediksi
        fitness += temp * temp
    fitness = fitness / (len(saham) - 12)
    fitness = 1 / fitness
    return fitness


def fitness_all(pop=[]):
    fitness_all = []
    for i in range(len(pop)):
        fitness_all.append(fitness(pop[i]))
    return fitness_all
