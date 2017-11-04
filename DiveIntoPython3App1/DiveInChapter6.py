
#import re

def create_tupleoffunctions(returnvaluemultiplier1, returnvaluemultiplier2):
    '''
    Accepts two values, and returns a touple of functions (,) 
    function1 takes a number (inputvalue) and multiplies it by returnvaluemultiplier1
    function2 takes a number (inputvalue) and adds it to returnvaluemultipliers2
    both return the result
    '''
    def function1(inputvalue):
        return inputvalue * returnvaluemultiplier1
    def function2(inputvalue):
        return inputvalue + returnvaluemultiplier2
    return (function1, function2)


def begintuplefunction():
    multiplierfunction, adderfunction = create_tupleoffunctions(3, 8.2)

    print('Multiplier function: ', multiplierfunction(4))
    print('Adder function: ', adderfunction(5))

if __name__ == "__main__":
    begintuplefunction()

#def build_match_and_apply_functions(pattern, search, replace):
#    def matches_rule(word):
#        return re.search(pattern, word)
#    def apply_rule(word):
#        return re.sub(search, replace, word)
#    return (matches_rule, apply_rule)

#h=build_match_and_apply_functions(1,2,3)


#def match_sxz(noun):
#    return re.search('[sxz]$', noun)

#def apply_sxz(noun):
#    return re.sub('$', 'es', noun)

#def match_h(noun):
#    return re.search('[^aeioudgkprt]h$', noun)

#def apply_h(noun):
#    return re.sub('$', 'es', noun)

#def match_y(noun):
#    return re.search('[^aeiou]y$', noun)
        
#def apply_y(noun):
#    return re.sub('y$', 'ies', noun)

#def match_default(noun):
#    return True

#def apply_default(noun):
#    return noun + 's'

#rules = ((match_sxz, apply_sxz),
#         (match_h, apply_h),
#         (match_y, apply_y),
#         (match_default, apply_default)
#         )

#def plural(noun):           
#    for matches_rule, apply_rule in rules:
#        if matches_rule(noun):
#            return apply_rule(noun)

#