import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
#Creating a list of sum of 2 dice, rolled 1000 times
dice_result = []
for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_result.append(dice1 + dice2)
mean=sum(dice_result)/1000
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)

print(mean)
print(median)
print(mode)
print(std_deviation)
#fig=ff.create_distplot([dice_result],["Result"],show_hist=False)
#fig.show()