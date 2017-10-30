''' 
    A game that tracks coins moving through time.
'''

def initializeCoinPurse():
    '''
    Create a Purse to hold a set of coins

    Returns a dictionary of Purses tuple (set, t)

    '''

    # Reset the economy. 
    # All money starts at the CentralBank.
    # Time starts at zero.
    purseAndrew = {}
    purseTraci = {}
    purseCentralBank = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    t=0

    return ({2:purseAndrew, 1:purseTraci, 0:purseCentralBank}, t)

def nextStep(economy, delta_t=1):
    purses, current_t = economy
    
    
    # Increase time by one
    current_t += delta_t
    # Govt buys 1 unit from Andrew 
    purses.get[2] += purses.get[2].pop # trying to reference parts of the dictionary. I think it's wrong
    print("Andrew @ t = {0}: {1}".format(t, purseAndrew))
    print("CentralBank @ t = {0}: {1}".format(t, purseCentralBank))


if __name__ == "__main__":
    # Initialize the purses and stuff
    economy = initializeCoinPurse()
    
    # Begin regular loop of the economy

    nextStep(economy)
    nextStep()
    nextStep()
    nextStep()


## All Coins = 1,2,3,4,5,6,7,8,9,10,11,12
#purseAndrew = {1,2,3,4,5}
#purseTraci = set(range(6,10))
#purseCentralBank = 

#print(purseAndrew)
#print(purseTraci)