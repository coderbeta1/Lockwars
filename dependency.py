import matplotlib.pyplot as plt
import random

def calculate_economy(number_of_infected, infection_rate, mortality_rate):
    if number_of_infected == 0 and infection_rate == 0 and mortality_rate == 0:
        return 2000000
    else:
        # Introduce random values from normal distributions with mean 0 and standard deviation 1
        infected_disturbance = random.normalvariate(6, 0.25)
        infection_rate_disturbance = random.normalvariate(0, 1)
        mortality_rate_disturbance = random.normalvariate(6, 0.25)

        # Modify the coefficients with the random disturbances
        B1 =  (infected_disturbance)*0.2
        B2 =  (infection_rate_disturbance)*0
        B3 =  (mortality_rate_disturbance)*10000

        economy = 2000000 - B1 * number_of_infected - B2 * infection_rate - B3 * mortality_rate
        return max(0, economy)

def calculate_public_distress(number_of_infected, infection_rate, mortality_rate):
    if number_of_infected == 0 and infection_rate == 0 and mortality_rate == 0:
        return 0
    else:
        # Introduce random values from normal distributions with mean 0 and standard deviation 1
        infected_disturbance = random.normalvariate(6, 0.3)
        infection_rate_disturbance = random.normalvariate(6, 0.3)
        mortality_rate_disturbance = random.normalvariate(6, 0.3)

        # Modify the coefficients with the random disturbances
        C1 = ( infected_disturbance)/12000000
        C2 = ( infection_rate_disturbance)/500
        C3 = ( mortality_rate_disturbance)/250

        public_distress = C1 * number_of_infected + C2 * infection_rate + C3 * mortality_rate
        return min(1, public_distress)

while True:
    # Example usage
    number_of_infected = int(input("Number of Infected: "))
    infection_rate = int(input("Infection: "))
    mortality_rate = int(input("Mortality: "))

    economy = calculate_economy(number_of_infected, infection_rate, mortality_rate)
    public_distress = calculate_public_distress(number_of_infected, infection_rate, mortality_rate)

    print("Economy:", economy)
    print("Public Distress:", public_distress)
    print()
