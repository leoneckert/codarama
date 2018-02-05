import sys, os
import random

print random.random() # 0 and 1

a = [2, 3, 46, 7, 8]
print random.choice(a)
print random.sample(a, 3)

print "\n TODAY WE LEARNED ALL THIS:"
for f in os.listdir("."):
    print ">>>> ", f

print "  "

print "  "
print sys.argv # return a list with arguments
