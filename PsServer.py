# this program will simulate a PS server

import random
import time
from math import *
import functions
from tabulate import tabulate




class PS_server:
    def __init__(self, n, r, s):
        self.n = n # switched on servers
        self.m = 10 # total servers
        self.seed = s
        self.start_t = 1 # time point when the first job arrives
        # power budget is 2000 Watts
        self.r = r # r requests(jobs) in this simulation
        self.p = 2000/self.n
        self.f = 1.25 + 0.31 * (self.p/200 - 1)
        self.log_info = [] # record each status of the simulation
        # in this simulation, i assume there are 50 requests(number can be changed)
        self.inter_arrival_time = self.get_inter_arrival_time()
        self.service_time = self.get_service_time()
        self.arrival_time = self.get_arrival_time()
##        self.service_time = [2.1, 3.3, 1.1, 0.5, 1.7]
##        self.arrival_time = [1, 2, 3, 5, 15]
        self.C = len(self.service_time)
        self.each_response_time = []

        
    def status_update(self):
        # take one server to do the simulation
        # assume first request arrived at t = 1, stage changes
        t = self.start_t
        # status = [t, event, next_arrival_time, next_departure_time, job_list]
        status = [0, None, self.arrival_time[0], inf, []] # initial status
        del self.arrival_time[0]
        while True:
            record = ''
            for i in status:
                record += str(i)
                record += "~"
            self.log_info.append(record)
            if status[2] < status[3]:
                t = status[2]
                status = self.arrival(status, t)
            elif status[2] > status[3]:
                t = status[3]
                status = self.departure(status, t)
            else:
                break


    def arrival(self, status, t):
        last_t = status[0]
        status[0] = t
        event = 'arrival'
        status[1] = event
        # if no more inter arrival time left
        if not len(self.arrival_time):
            next_arrival_time = inf
        else:
            next_arrival_time = self.arrival_time[0]
            del self.arrival_time[0]
        status[2] = next_arrival_time
        job_list = status[4]
        # if there were jobs in the server, we need to update
        service_left = []
        if job_list:
            inter_t = t - last_t
            service_received = inter_t/len(job_list)
            # modify the remaining service time for each job
            for i in range(len(job_list)):
                job_list[i][1] -= service_received
                job_list[i][1] = float("{0:.3f}".format(job_list[i][1]))
                service_left.append(job_list[i][1])
        job_list.append([float("{0:.3f}".format(t)), float("{0:.3f}".format(self.service_time[0]))])
        service_left.append(job_list[-1][1])
        min_service_left = min(service_left)
        del self.service_time[0]
        next_departure_time = t + min_service_left*len(job_list)
        next_departure_time = float("{0:.3f}".format(next_departure_time))
        status[3] = next_departure_time
        status[4] = job_list                    
        return status


    def departure(self, status, t):
        last_t = status[0]
        status[0] = t
        event = 'departure'
        status[1] = event
        job_list = status[4]
        job_id = 0
        inter_t = t - last_t
        service_received = inter_t/len(job_list)
        service_left = []
        for i in range(len(job_list)):
            job_list[i][1] -= service_received
            job_list[i][1] = float("{0:.3f}".format(job_list[i][1]))
            if job_list[i][1] == 0:
                job_arrival_time = job_list[i][0]
                job_response_time = t - job_arrival_time
                self.each_response_time.append(job_response_time)
                job_list[i] = None
            else:
                service_left.append(job_list[i][1])
        for j in range(job_list.count(None)):
            job_list.remove(None)
        if service_left:
            min_service_left = min(service_left)
            next_departure_time = t + min_service_left*len(job_list)
        else:
            next_departure_time = inf
        status[3] = next_departure_time
        status[4] = job_list 
        return status


    

    def inter_arrival_time_generator(self):
        # a1 is exponentially distributed with a mean arrival rate 7.2 requests/s
        # a2 is uniformly distributed in the interval [0.75, 1.17]
        # random.expovariate(lambd): Exponential distribution.       
        a1 = random.expovariate(7.2)
        a2 = random.uniform(0.75, 1.17)
        return float("{0:.3f}".format(a1*a2))


    def get_inter_arrival_time(self):
        # simulation generates 49 inter arrival times, meanwhile there will be 50 service time 
        times = []
        random.seed(self.seed)
        for _ in range(self.r - 1):
            times.append(self.inter_arrival_time_generator())
        return times
            

    def service_time_generator(self):
        t = functions.ICDF(random.random())
        return float("{0:.3f}".format(t/self.f))


    def get_service_time(self):
        total_service_times = []
        single_server_times = []
        random.seed(self.seed)
        for _ in range(self.r):
            total_service_times.append(self.service_time_generator())
        i = 0
        while i<len(total_service_times):
            single_server_times.append(total_service_times[i])
            i += self.n
        return single_server_times


    def get_arrival_time(self):
        start_t = self.start_t
        arrival = start_t
        arrival_time = [arrival]
        for i in self.inter_arrival_time:
            arrival += i
            arrival_time.append(arrival)
        single_server_arrival_time = []
        i = 0
        while i<len(arrival_time):
            single_server_arrival_time.append(arrival_time[i])
            i += self.n
        return single_server_arrival_time
    
        


    def log(self):
        headers = ['time', 'event', 'next arrival time', 'next departure time', 'job list']
        output = []
        for i in self.log_info:
            output.append(i.split("~")[:-1])
        table = tabulate(output, headers)
        mean_response_time = self.calculator()
        input_info1 = 'number of servers switched on: ' + str(self.n) + '\n'
        input_info2 = 'number of jobs: ' + str(self.r) + '\n'
        input_info3 = 'seed: ' + str(self.seed) + '\n'
        s = 'mean response time is: ' + str(mean_response_time) + '\n\n'
        f = open('log.txt', 'a')
        f.write(input_info1 + input_info2 + input_info3)
        f.write(table)
        f.write('\n')
        f.write(s)
        f.close()


    def calculator(self):
        start_t = self.start_t
        C = self.C
        finish_t = float(self.log_info[-1].split('~')[0])
        T = finish_t - start_t
        X0 = C/T
        total_response_time = sum(self.each_response_time)
        # N is number of jobs
##        N = len(self.each_response_time)
##        print(N == C)
        mean_response_time = total_response_time/C
        return float("{0:3f}".format(mean_response_time))
        

    


    

        


