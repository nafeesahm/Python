

fname = input("Enter file name : ")
num_word = 0

with open(fname , 'r') as f:
    for line in f:
        words = line.split()
        num_word = num_word  + len(words)
        print(num_word)
