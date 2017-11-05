
import re

class PapayaWhip:
    pass





def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def create_file(filename='rules.txt'):
    rules = []
    with open(filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            rules.append(build_match_and_apply_functions(pattern, search, replace))
    return rules

def plural(noun, rules):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('No matching rule for {0}'.format(noun))

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
    print( plural(input('Type a noun to pluralize: '), create_file()))