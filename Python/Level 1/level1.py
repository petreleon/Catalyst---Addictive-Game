import os
dir_path = os.path.dirname(os.path.realpath(__file__))
path_input = dir_path+'\\level1-0.in'
path_output = dir_path+'\\level1.out'
file_input = open(path_input, 'r')
file_output = open(path_output, 'w')
temp = file_input.readline().split()
temp = list(map(int, temp))
r, c, n = temp[0], temp[1], temp[2]


def transform(x):
    global c
    return [(x-1) // c+1, (x-1) % c+1]


positions = list(map(transform, temp[3:]))
#print(positions)

results = [item for sublist in positions for item in sublist]
#print(' '.join([str(elem) for elem in results]))
file_output.write(' '.join([str(elem) for elem in results]))
file_output.close()
file_input.close()
