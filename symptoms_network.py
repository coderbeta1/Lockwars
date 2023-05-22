class symptom:
    def __init__(self, ID,infectious, mortal, connections, connectionweights) -> None:
        self.name = ID
        self.infection = infectious
        self.mortality = mortal
        self.paths = connections 
        self.pathlengths = connectionweights
        return
def initialize_symptoms():
    nodes = (
        "rash",
        "appetite_loss",
        "fever",
        "weakness",
        "headaches",
        "dementia",
        "opportunistic_infection",
        "peripheral_neuropathy",
        "guillian_barre_syndrome",
        "weight_loss",
        "throat_inflammation",
        "lymph_node_enlargement",
        "sepsis",
        "vomiting",
        "pneumonia",
        "organ_failure",
        "diarrhea",
        "cachexia",
        "esophagal_candidiasis",
        "kaposi_sarcoma",
        "paralysis",
        "coma"
    )
    infectious_rates = (
        20,0,50,0,0,0,70,0,
        0,0,30,40,80,20,60,90,40,0,50,70,0,0
    )
    
    mortality_rates = (0,0,5,0,0,10,80,0,30,10,0,0,90,0,70,95,
                       5,20,5,80,50,90)
    symptom_list = [symptom(nodes[i],infectious_rates[i], mortality_rates[i],[],[]) for i in range(len(nodes))]
    cyan = ["rash","fever","weakness","headaches","appetite_loss"]
    blue = ["cachexia","diarrhea","vomiting","pneumonia","peripheral_neuropathy",
            "guillian_barre_syndrome","opportunistic_infection",
            "weight_loss",
            "throat_inflammation",
            "lymph_node_enlargement",
            "esophagal_candidiasis"
            ]
    green = [
        "coma","paralysis",
        "kaposi_sarcoma",
        "dementia",
        "organ_failure",
        "sepsis"
    ]
    cyan_symptoms = [x for x in symptom_list if x.name in cyan]
    blue_symptoms = [x for x in symptom_list if x.name in blue]
    green_symptoms = [x for x in symptom_list if x.name in green]

    connections = [
        ["opportunistic_infection","lymph_node_enlargement"],
        ["weight_loss","pneumonia"],
        ["opportunistic_infection","weight_loss","throat_inflammation","lymph_node_enlargement"],
        ["peripheral_neuropathy", "guillian_barre_syndrome"],
        ["vomiting","weight_loss"],
        [],
        ["dementia"],
        ["guillian_barre_syndrome"],
        ["cachexia"],
        ["kaposi_sarcoma"],
        ["pneumonia"],
        ["sepsis"],
        ["organ_failure"],
        ["diarrhea","esophagal_candidiasis"],
        ["organ_failure","lymph_node_enlargement"],
        ["paralysis"],
        ["esophagal_candidiasis","lymph_node_enlargement","opportunistic_infection"],
        ["paralysis"],
        ["kaposi_sarcoma"],
        [],
        ["coma"],
        []
    ]

    connections_weights = [
        [0.4,0.2],
        [0.4,0.4],
        [0.22,0.22,0.22,0.22],
        [0.4,0.4],
        [0.4,0.4],
        [],
        [0.9],
        [0.95],
        [0.9],
        [0.9],
        [0.5],
        [0.9],
        [0.9],
        [0.4,0.4],
        [0.4,0.4],
        [0.9],
        [0.3,0.3,0.3],
        [0.9],
        [0.9],
        [],
        [0.95],
        []
    ]
    for i in range(len(nodes)):
        symptom_list[i].paths = connections[i]
        symptom_list[i].pathlengths = connections_weights[i]

    return symptom_list



def mutate_pathwise(symptom_list : list[symptom], initial_symptoms : list[symptom] = [],initial_infection_rate = 0,initial_mortality_rate = 0) -> list:
    from numpy import random
    if len(initial_symptoms) == 0:
        initial_symptoms.append(random.choice(symptom_list[0:5]))
    else:
        last_symptom = initial_symptoms[-1]
        if len(last_symptom.paths) != 0:
            adjacent = [x for x in symptom_list if x.name in last_symptom.paths]
            prob = last_symptom.pathlengths + [1 - sum(last_symptom.pathlengths)]
            nextsymptom = random.choice(adjacent + [None],1, p = prob)[0]
            
            
            if nextsymptom != None:
                initial_symptoms.append(nextsymptom)
                initial_infection_rate += nextsymptom.infection
                initial_mortality_rate += nextsymptom.mortality
        else:
            return -1
    return initial_symptoms, initial_infection_rate, initial_mortality_rate

def mutate_graphwise(symptom_list : list[symptom],  initial_symptoms : list[symptom] = [],initial_infection_rate = 0,initial_mortality_rate = 0):
    from numpy import random
    if len(initial_symptoms) == 0:
        initial_symptoms.append(random.choice(symptom_list[0:5]))
    else:
        for symp in initial_symptoms:
            
            adjacent = [x for x in symptom_list if x.name in symp.paths]
            prob = symp.pathlengths + [1 - sum(symp.pathlengths)]
            nextsymptom = random.choice(adjacent + [None],1, p = prob)[0]
            if (nextsymptom != None) and not(nextsymptom in initial_symptoms):
                initial_symptoms.append(nextsymptom)
                initial_infection_rate += nextsymptom.infection
                initial_mortality_rate += nextsymptom.mortality



    return initial_symptoms, initial_mortality_rate, initial_mortality_rate

def doshit(n : int):
    data = initialize_symptoms()
    a = 0
    b = 0
    symps = []
    for i in range(n):

        shit = mutate_pathwise(data,symps,a,b)
        if shit == -1:
            break
        symps = shit[0]
        a = shit[1]
        b = shit[2]
        print([x.name for x in symps])
    return
#doshit(10)
def doshitdifferently(n : int):
    data = initialize_symptoms()
    a = 0
    b = 0
    symps = []
    for i in range(n):

        shit = mutate_pathwise(data,symps,a,b)
        if shit == -1:
            break
        symps = shit[0]
        a = shit[1]
        b = shit[2]
        print([x.name for x in symps])
    return
