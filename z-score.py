import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df['reading_time'].tolist()

population_mean = statistics.mean(data)
sd = statistics.stdev(data)
print("mean of population :", population_mean)
print("standard diviation of population :", sd)

def randomsetofmean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0, 100):
    setofmeans = randomsetofmean(30)
    meanlist.append(setofmeans)

sd = statistics.stdev(meanlist)    
mean = statistics.mean(meanlist)
print("standard diviation of sampling distribution", sd)
print("mean of sampling distribution", mean)
fig = ff.create_distplot([meanlist], ["reading_time"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.20], mode = "lines", name = 'MEAN'))
fig.show()

first_sd_start, first_sd_end = mean - sd, mean + sd
second_sd_start, second_sd_end = mean - (2*sd), mean + (2*sd)
third_sd_start, third_sd_end = mean - (3*sd), mean + (3*sd)

fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = 'MEAN'))
fig.add_trace(go.Scatter(x = [first_sd_start, first_sd_start], y = [0, 0.17], mode = "lines", name = 'MEAN of reading time'))
fig.add_trace(go.Scatter(x = [first_sd_end, first_sd_end], y = [0, 0.17], mode = "lines", name = 'MEAN of reading time'))
fig.add_trace(go.Scatter(x = [second_sd_start, second_sd_start], y = [0, 0.17], mode = "lines", name = 'standard diviation 2'))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end], y = [0, 0.17], mode = "lines", name = 'standard diviation 2 end'))
fig.add_trace(go.Scatter(x = [third_sd_start, third_sd_start], y = [0, 0.17], mode = "lines", name = 'standard diviation 3'))
fig.add_trace(go.Scatter(x = [third_sd_end, third_sd_end], y = [0, 0.17], mode = "lines", name = 'standard diviation 3 end'))

z_score = (population_mean - mean)/sd
print("the z score is ", z_score)