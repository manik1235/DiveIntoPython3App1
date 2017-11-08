'''
Allows you to keep doubling a list, using more and more memory, until you exit or run out of memeory
'''

a_list = [1]
continuedoubling = False
while not continuedoubling:
    a_list.extend(a_list)
    #print(a_list)
    print(len(a_list))
    continuedoubling = input('Continue Doubling? ')
    print (continuedoubling)
