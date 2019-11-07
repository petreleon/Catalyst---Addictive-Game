import os
dir_path = os.path.dirname(os.path.realpath(__file__))
path_input = dir_path+'\\level2-3.in'
path_output = dir_path+'\\level2.out'
file_input = open(path_input, 'r')
file_output = open(path_output, 'w')
temp = file_input.readline().split()
temp = list(map(int, temp))
r, c, n = temp[0], temp[1], temp[2]
N = 2

temp = temp[3:]
subList = [temp[n:n+N] for n in range(0, len(temp), N)]
#print(subList)


def keyfunction(a):
    return a[1]


def transform(x):
    global c
    return [[(x[0]-1) // c+1, (x[0]-1) % c+1], x[1]]


subList = sorted(subList, key=keyfunction)

coordonatesList = list(map(transform, subList))
coordonatesList = [coordonatesList[n:n+N]
                   for n in range(0, len(coordonatesList), N)]
#print(coordonatesList)


def getManhattan(x):
    return abs(x[0][0][0]-x[1][0][0])+abs(x[0][0][1]-x[1][0][1])


results = list(map(getManhattan, coordonatesList))
"""
def transform(x):
    global c
    return [(x-1) // c+1, (x-1) % c+1]


positions = list(map(transform, temp[3:]))
#print(positions)

results = [item for sublist in positions for item in sublist]
#print(' '.join([str(elem) for elem in results]))
"""
file_output.write(' '.join([str(elem) for elem in results]))

file_output.close()
file_input.close()
