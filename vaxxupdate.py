#to be run on daily tick


def vaxupdate(state):
    totalcost=sum(cost)
    for i in range(3):
        if vaccine.rn.randint(1,101)<risk[i]:
            pass
        else:
            state['vaxxprog']+=progpday[i]
    state['eco']-=state['vaxxcost']
    return state
