import numpy.random as rn,numpy
avgstock=4
def phase(x):               #x is progress so far
    if x<0.11:
        return 'Preclinical Phase'
    elif x<0.3:
        return 'Phase I'
    elif x<0.5:
        return 'Phase II'
    else:
        return 'Phase III'
def h(x):                               #x is funds
    return (5e-10*x)/(1+7e-8*x)         #returns progress per day
def choosevax(prog):
    cost=rn.randint(3000000,10000000,3)
    esttime=[int((1-prog)*avgstock/(h(cost[x]))) for x in range(3)]         #estimated time using diminishing returns
    low,r,risk=1,[0,0,0],[0,0,0]
    for i in range(3):
        r[i]=rn.randint(low,low+(3-i//2))*5
        low=r[i]/5
    arg=numpy.argsort(cost)
    for i in range(3):
        risk[arg[i]]=r[i]
    return [int(x*h(x)/avgstock) for x in cost],esttime,risk,[h(x)/avgstock for x in cost] #costperday,esttimeleftfor1stock,currentphase,riskfordiffmethods,progressperdayperstock
    #for progressperday, take progressperdayperstock*no.of stocks

def vaxevent(state,cost,risk,progpday,stock):
    
    stock=[int(input()) for i in range(3)]
    cost=sum([cost[i]*stock[i] for i in range(3)])
    progpday=[progpday[i]*stock[i] for i in range(3)]
    state['vaxxspeed']=progpday
    state['vaxxrisk']=risk
    state['vaxxcost']=cost
    return state
