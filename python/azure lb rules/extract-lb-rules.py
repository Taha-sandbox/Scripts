
import re

f = open("preprod.txt", "r")
lines = f.readlines()

count = -1
name = []
port = []
for line in lines:
    count += 1
    if count % 4 == 0:
        name = name + [line.strip()]
    if count % 4 == 1:
        port = port + [line.strip()]

x = 0
for x in range(len(port)):
    port[x] = port[x][port[x].index("/") + 1: port[x].index(")")]
print(port)

for x in range(len(port)):
    print("{\n  name  = \"%s\" \
    \n  protocol = \"Tcp\" \n  frontend_port = %s  \n  backend_port  = %s \
    \n  probe_index   = 0 \n }," % (name[x], port[x], port[x]))