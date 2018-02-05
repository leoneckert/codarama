a = ["lemon", "lennon", "lenin", "leon"]

for word in a:
    print word

for i in range(0,1000):
    print "this is loop number" + str(i)

names = ["Juan Jose", "Mathura", "Chino", "Jenjenjen", "Yuli", "Aaron", "Aaron", "Jason"]

for name in names:
    # if name.startswith("J") or name.endswith("n"):
    if not name.startswith("J"):
        print "This is a friend of mine whose name starts with J:", name
