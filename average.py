import csv
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
import pandas as pd
import statistics

from scipy.__config__ import show

df = pd.read_csv("temp.csv")
data = df["temp"].to_list()
#population_mean = statistics.mean(data)
#population_stdev = statistics.stdev(data)
#print("Mean", population_mean)
#print("St deviation", population_stdev)

#To find mean and stdev for 100 data points 
#dataset = []
#for i in range(0,100):
#    random_index = random.randint(0,len(data))
#    value = data[random_index]
#    dataset.append(value) 
#
#mean = statistics.mean(dataset)
#stdev = statistics.stdev(dataset)
#print("The mean of semple data is ", mean)
#print("The standard deviation of semple data is ", stdev)

#To get the mean of the given data samples pass the no of data points you want as counter
def random_set_of_mean(counter) :
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, (len(data)-1))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 

#To plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["temp"], show_hist=False)
    fig.show()

#To get th emean of 100 data points 1000 times and plot the graoh
#Pass the no. of time you want the mean of data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of samplign data is ", mean)

setup()

population_mean = statistics.mean(data)
print("Population mean is ", population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    standard_deviation = statistics.stdev(mean_list)
    print("Standard deviation of samplign data is ", standard_deviation)

standard_deviation()