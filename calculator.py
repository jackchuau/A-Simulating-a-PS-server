
import PsServer

def Mean(n, s):
    sum_value = 0
    for r in range(1000, 3001):
        ps = PsServer.PS_server(n, r, s)
        ps.status_update()
        sum_value += ps.calculator()
    print(sum_value/2000)
    return sum_value/2000


for n in range(3, 11):
    s = 100
    dataset = []
    for _ in range(15):
        s += 100
        dataset.append(Mean(n, s))
        
    t = sum(dataset)/len(dataset)

    sum_up = 0
    for i in range(len(dataset)):
        sum_up += (t - dataset[i])**2

    S = (sum_up/(len(dataset)-1))**0.5
    print('Number of the servers: ', n)
    print('mean: ', t)
    print('deviation: ', S)
    print()
