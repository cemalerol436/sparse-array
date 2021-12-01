
# These two arrays below are given lists.

queries = ["aba", "xzxb", "ab"]
strings = ["aba", "baba", "aba", "xzxb"]

sum = []

#Loop to find the same word in string list.

for qword in queries:
    total = 0

    for stword in strings:
        if qword == stword:
            total += 1

    sum.append(total)

print(sum)
