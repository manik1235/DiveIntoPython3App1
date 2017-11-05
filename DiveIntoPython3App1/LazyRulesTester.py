import LazyRulesClass
r1 = LazyRulesClass.LazyRules()
r2 = LazyRulesClass.LazyRules()
print (r1.rules_filename)
print (r2.rules_filename)
r2.rules_filename = 'r2-override.txt'
print (r2.rules_filename)
print (r1.rules_filename)
print (r2.__class__.rules_filename)
r2.__class__.rules_filename = 'papayawhip.txt'
print(r1.rules_filename)
print(r2.rules_filename)

