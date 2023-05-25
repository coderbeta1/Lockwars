import numpy.random as rn,numpy
avgstock=6
state={'vaxxspeed':0,'vaxxrisk':0,'vaxxcost':0,'vaxxprog':0.3}      #remove when integrating
def phase(x):               #x is progress so far
    if x<0.11:
        return 'PRECLINICAL PHASE'
    elif x<0.3:
        return 'PHASE I'
    elif x<0.5:
        return 'PHASE II'
    else:
        return 'PHASE III'
def h(x):                               #x is funds
    return (5e-10*x)/(1+7e-8*x)         #returns progress per day
def choosevax(prog):
    cost=rn.randint(3000000,10000000,3)
    esttime=[int((1-prog)*avgstock/(h(cost[x]))) for x in range(3)]         #estimated time using diminishing returns
    low,r,risk=1,[0,0,0],[0,0,0]
    for i in range(3):
        r[i]=rn.randint(low,low+(3-i//2))*5
        low=r[i]/5
    arg=numpy.argsort(cost)[::-1]
    for i in range(3):
        risk[arg[i]]=r[i]
    return [int(x*h(x)/avgstock) for x in cost],esttime,risk,[h(x)/avgstock for x in cost] #costperday,esttimeleftfor1stock,riskfordiffmethods,progressperdayperstock
    #for progressperday, take progressperdayperstock*no.of stocks

def vaxevent(state,cost,risk,progpday,stock):
    
    cost=sum([cost[i]*stock[i] for i in range(3)])
    progpday=[progpday[i]*stock[i] for i in range(3)]
    state['vaxxspeed']=progpday
    state['vaxxrisk']=risk
    state['vaxxcost']=cost
    return state

def actualevent(state):
    cost,time,risk,progpday=choosevax(state['vaxxprog'])
    ph=phase(state['vaxxprog'])
    print(f"It's time to choose how you allocate funds to vaccine research. There are three branches working on the same vaccine. \
    They all have different speeds as well as chances to not make progress.\nThe Vaccine is Currently in {ph}\n\t\tBranch1\tBranch2\tBranch3\
    \nCost per stock per day\t{cost[0]}\t{cost[1]}\t{cost[2]}\nTime taken for one stock\t{time[0]}\t{time[1]}\t{time[2]}\nRisk\t\
    {risk[0]}\t{risk[1]}\t{risk[2]}\nProgress per day per stock\t{progpday[0]}\t{progpday[1]}\t{progpday[2]}\n\nChoose the no of stocks for each branch-")
    stock=[int(input('Branch{i}: ')) for i in range(1,4)]
    return vaxevent(state, cost, risk, progpday, stock)
actualevent(state)      #remove when integrating
