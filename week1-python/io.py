import sys
if len(sys.argv) == 1:
    sys.argv.append("waww.txt")
f = open(sys.argv[1], "r")

all_words = list()
for line in f:
    line = line.strip().lower()
    words = line.split()
    all_words += words

# print all_words

all_words.sort()

# print all_words

counter = 0
out_file = open("waww_new.txt", "a")
for line in open(sys.argv[1], "r"):
    line = line.strip()
    words = line.split()
    line_list = list()
    for word in words:
        line_list.append(all_words[counter])
        counter += 1
    print " ".join(line_list)
    out_file.write(" ".join(line_list) + "\n")
out_file.close()
