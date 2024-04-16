p = [0, 1, 2, 3, 4, 5]
q = [i for i in p if i % 2 == 0]
# q = [0, 2, 4]
q = [3 * i for i in p if i % 2 == 0]
# q = [0, 6, 12]
def square_num(num):
    return num * num
q = [square_num(x) for x in p if x % 2 == 1] # and if x != 5]
# q = [1, 9, 25]

print(p[0::2][1])
# start at 0, we don't have an end value so end at 4 (last step reached when stepping by two before going out of bounds), step by two
# list is now 0, 2, 4
# picks the 1 index of the new list
# returns 2 or outputs 2

# p[1] = 1
q = 3
print(q in p) # IS q in p? NOT "what index is q in p"
# returns true or prints true