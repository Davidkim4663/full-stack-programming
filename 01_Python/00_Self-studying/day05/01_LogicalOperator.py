            #  Logical chart
# p     q    p v q  p ^ q   p -> q    p<->q   ~p
# T     T      T      T       T         F     F    
# T     F      T      F       F         T     F
# F     T      T      F       T         F     T
# F     F      F      F       T         F     T

# Not Operator
x = 10
under_20 = x < 20
print("under_20: ", under_20)
print("not_under_20:", not under_20)

# AndOperator
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)