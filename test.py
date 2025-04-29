from index import *
from temp import *
from binary_search_2 import *
import random
import time

a = set()

length = 10000

while len(a) < length:
    a.add(random.randint(-3*length, 3*length))

a = sorted(list(a))

start_normal = time.time()

for i in a:
    find(a, i)

end_normal = time.time()

start_binary_search = time.time()

for i in a:
    binary_search(a,i)

end_binary_search = time.time()


start_binary_search_2 = time.time()

for i in a:
    binary_search_2(a,i)

end_binary_search_2 = time.time()


normal_diff = (end_normal - start_normal) / length

binary_diff = (end_binary_search - start_binary_search) / length

binary_diff_2 = (end_binary_search_2 - start_binary_search_2) / length

print(normal_diff)

print(binary_diff)

print(binary_diff_2)