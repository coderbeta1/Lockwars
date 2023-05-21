from numpy import random
import math
import matplotlib.pyplot as plt

def sir_sim(population : int,  beta : float, gamma : float, day : int, initialinfectionrate = 0.01):
    S = population
    I = initialinfectionrate
    R = 0
    for i in range(day):
        ds_dt = -1 * beta * S * I / population
        di_dt = (beta * I * S / population) - gamma * I
        dr_dt = gamma * I

        S += ds_dt
        I += di_dt
        R += dr_dt
    
    return (S, I, R)

def sir_sim_sampling(population : int, beta:float, gamma:float, day: int, initialinfectionrate = 0.01):
    data = sir_sim(population, beta, gamma,day,initialinfectionrate)
    S,I,R = data[0], data[1], data[2]
    sus = random.choice([1,0], population, p = [S/population, 1.0 - S/population])
    inf = random.choice([1,0], population, p = [I/population, 1.0 - I/population])
    rec = population - sum(sus) - sum(inf)
    return sum(sus), sum(inf), rec
