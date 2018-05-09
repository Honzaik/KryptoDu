import hashlib
import time
from sys import argv

DELKA = 8

if(len(argv) > 1):
    DELKA = int(argv[1])

start = time.time()

prefix = "JanOupicky"


counter = 0

seznam = dict()

h = hashlib.sha256((prefix + str(counter)).encode("utf-8")).hexdigest()

while(h[:DELKA] not in seznam):
    seznam[h[:DELKA]] = str(counter)
    counter += 1
    h = hashlib.sha256((prefix + str(counter)).encode("utf-8")).hexdigest()
    if(counter % 1000000 == 0):
        print(counter)

print(DELKA)
print(h[:DELKA])
print(seznam[h[:DELKA]])
print(str(counter))
print(str(time.time() - start) + " s")