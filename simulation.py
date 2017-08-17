
import sys
import PsServer



val1 = input("Please enter how many servers you want to switch on(from 3 to 10): ")
val2 = input("Please enter how many requests you want to test: ")
val3 = input("input a seed: ")
try:
    n = int(val1)
    r = int(val2)
    s = int(val3)
except ValueError:
    print("sorry, your input is not an integer...")
    sys.exit(1)

if n < 3 or n > 10:
    print("sorry, your input is incorrect...")
    sys.exit(1)
if r<=0 :
    print("sorry, wrong requests number...")
    sys.exit(1)


ps = PsServer.PS_server(n, r, s)
ps.status_update()
##print("mean response time: ", mean_response_time)
ps.log()









