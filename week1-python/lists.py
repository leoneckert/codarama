my_list = [1, 3, 5, 6, 7, -3]
my_list = list([3, 4, 5])

my_list = list()

my_list.append(7)
my_list.append(1)
print my_list

print my_list[1]

print len(my_list)

b = [8]

print my_list + b

c = my_list + b

print c
c.append(3)
print c

c.insert(1, 1000)
print c

#slicing
print c[1:]
print c[1:3]
print c[-1]
print c[:-1]
print type(c[-1])
print type(c[:-1])

c.sort(reverse=True)
print c


last_element = c.pop()
print last_element
print c

print "last_element: ", last_element, " rest: ", c


print 7 in c


g = range(0,40)
print g
print ""

g = range(0, 40, 3)
print g
print ""

g = range(100, 40, -5)
print g


f = ["bread", "elephants", "muffins"]

print " & ".join(f)
