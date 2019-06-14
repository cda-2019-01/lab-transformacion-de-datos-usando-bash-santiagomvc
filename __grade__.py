import glob
import doctest

result = doctest.testfile('__grade__.txt', report = False, verbose = False)
a,b = result
print('\n>>>>  ', result, ' <<<<\n')
open('__grade__', 'w').write(str(round(float(b-a) / float(b) * 5.0 , 1)))




