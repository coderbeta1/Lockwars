class transmission:
    def __init__(self, ID, connections, connectionweights,infectiousness, visit = False) -> None:
        self.name = ID
        self.paths = connections 
        self.pathlengths = connectionweights
        self.speed = infectiousness
        self.visited = visit
        return

def initialize_transmissions():
    reds = ["vector","droplets","contact","fecal"]
    yellows = ["zoonotic","surfaces"]
    greens = ["vertical","bodyfluids"]
    allofem = reds + yellows + greens
    transmissions = [transmission(i,[],[],0) for i in allofem]
    connections = [
        ["zoonotic","fecal","contact","droplets"],
        ["surfaces","bfluids","contact","fecal","vector"],
        ["surfaces","fecal","droplets","vector"],
        ["bfluids","contact","droplets","vector","zoonotic"],
        ["vector","fecal"],
        ["droplets","contact"],
        ["bfluids"],
        ["fecal","vertical"]
    ]

    speeds = [15]*4 + [10]*2 + [5]*2

    for a,b in enumerate(transmissions):
        b.paths = connections[a]
        b.speed = speeds[a]
    reds2,greens2,yellows2 = [x for x in transmissions if x.name in reds],[x for x in transmissions if x.name in greens],[x for x in transmissions if x.name in yellows]
    return {"all of em" : transmissions, "reds" : reds2, "yellows" : yellows2, "greens" : greens2}

def mutate_transmissions(transmissions_list = [],initial_infection_rate = 0):
    from numpy import random
    transmissiondict = initialize_transmissions()
    name_list = [x.name for x in transmissions_list]
    trans = transmissiondict["all of em"]
    reds = transmissiondict["reds"]
    yellows = transmissiondict["yellows"]
    greens = transmissiondict["greens"]
    if len(transmissions_list) == 0:
        transmissions_list.append(random.choice([x for x in trans if x in reds]))
    else:
        last = transmissions_list[-1]
        choices = [x for x in trans if x.name in last.paths]
        redtored = [x for x in choices if last in reds and x in reds]
        choices2 = [ x for x in choices if x not in redtored]
        prob = [0.3/len(choices2) for i in choices2] + [0.15/len(redtored) for i in redtored]
        chosen = random.choice(choices2 + redtored + [None], p = prob + [1-sum(prob)])
        if chosen != None and chosen.name not in name_list:
            transmissions_list.append(chosen)
            initial_infection_rate += chosen.speed
    
    return  transmissions_list , initial_infection_rate

def dostuff(n : int): 
    vectors = []
    a = 0
    for i in range(20):
        vectors,a = mutate_transmissions(vectors,a)
        print([x.name for x in vectors], a)
