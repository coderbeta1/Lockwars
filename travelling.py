def initialize():
     mapp={'industrial':{'R':['hospital','park']}, 
    'appartment':{'R':['bungalow']}, 
    'bungalow':{'R':['appartment','govt'],'O':['research','coat'],'Y':['sports','research','shopping']}, 
    'govt':{'R':['coat','bungalow','school']}, 
    'amusement':{'R':['daily','school']}, 
    'school':{'R':['hospital','sports']}, 
    'daily':{'R':['amusement','research']}, 
    'research':{'R':['daily','slum','industrial'],'O':['airport','farming'],'Y':['sports','bungalow','shopping']}, 
    'slum':{'R':['airport','research']},
    'shopping':{'R':['airport','industrial'],'Y':['sports','research','bungalow']}, 
    'farming':{'R':['park','hospital'],'O':['research']}, 
    'hospital':{'R':['tour','farming','park','industrial','school']}, 
    'tour':{'R':['sports','hospital']}, 
    'coat':{'R':['sports','govt'],'O':['bungalow']}, 
    'sports':{'R':['coat','school'],'Y':['bungalow','research','shopping']},
    'park':{'R':['farming','hospital','industrial']},
    'airport':{'R':['slums','shopping'],'Y':['research']}
    }

def genpmap(mapp,key):
    nr = len(mapp[key]['R'])
    try :
        ny = len(mapp[key]['Y'])
        no = len(mapp[key]['O'])
    except KeyError:
        ny=0
        no=0

def updatetravel(mapp,state):
    l=['industrial', 'appartment', 'bungalow', 'govt', 'amusement', 'school', 'daily', 'research', 'shopping', 'farming', 'hospital', 'tour', 'coat', 'sports','park','airport']
    for i in l:
        if state[i]['infected']!=0:
            guh=np.random.choice([1,0],p=[state[i]['infected']/(state[i]['pop']*state['pop'])*0.05,1-state[i]['infected']/(state[i]['pop']*state['pop'])*0.05])
            if guh == 1:
                pmap=genpmap(mapp,i)
                npmap={}
                for j in pmap:
                    if state[j]['infected']==0:
                        npmap[j]=pmap[j]
                state[i][np.random.choce(list(npmap.keys()),p=list(npmap.values()))]=1
    return state