L = list(range(10))
L2 = [str(c) for c in L]
print "{} {}".format(type(L[0]),type(L2[0]))

L3 = [True,"2",3.0,4]
print [type(item) for item in L3]