''' 
    A game that tracks coins moving through time.
'''

def initializeCoinPurse():
    '''
    Create a Purse to hold a set of coins

    Returns a Purse object (set)

    '''

    # Reset the economy. 
    # All money starts at the CentralBank.
    # Time starts at zero.
    purseAndrew={}
    purseTraci={}
    purseCentralBank={1,2,3,4,5,6,7,8,9,10,11,12}
    t=0

def nextStep(delta_t=1):
    #doEvent(purseCentralBank,)
    # Increase time by one
    t += delta_t
    # Govt buys 1 unit from Andrew 
    purseAndrew += purseCentralBank.pop
    print("Andrew @ t = {0}: {1}".format(t, purseAndrew))
    print("CentralBank @ t = {0}: {1}".format(t, purseCentralBank))


if __name__ == "__main__":
    # Begin regular loop of the economy
    nextStep()
    nextStep()
    nextStep()
    nextStep()


# All Coins = 1,2,3,4,5,6,7,8,9,10,11,12
purseAndrew = {1,2,3,4,5}
purseTraci = set(range(6,10))
purseCentralBank = 

print(purseAndrew)
print(purseTraci)