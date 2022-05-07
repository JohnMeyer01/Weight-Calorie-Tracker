from matplotlib import pyplot as plt
import pandas as pd

# Pulls data from Excel
log = pd.read_csv('weight_log.csv')

# Creates relationship between day and calorie count
fig, ax1 = plt.subplots()
ax1.plot(log.Day, log.Calories,'r', label='Calories')

# Creates twin plot between weight and day
ax2 = ax1.twinx()
ax2.plot(log.Day, log.Weight,'b', label='Weight')

# Creates title and legend
plt.title('BodyWeight Relative to Calories Consumed', fontdict={'fontweight':'bold', 'fontsize': 12})
plt.legend()

plt.show()

# Pulls data from Excel
log = pd.read_csv('weight_log.csv')

def avgDaytoDay(log, start, end):
    return ((sum(log.Weight[start:end]))/(end-start))

# Sums the last weeks weight and divides by 7 to find the average weight from the last week of data-points
y = ((sum(log.Weight[-7:]))/7)

# Sums the week previous and divides to find the average weight from the week before
# a =((sum(log.Weight[14:21]))/7)
a = avgDaytoDay(log, 14, 21)

# Finds the difference between the two weeks
b = (y-a)

print(b)

# if/than/else statement that affirms the user to either eat more or continue at maintenance
if (b) < 1:
    print("Eat 100 more calories")
else:
    print("Continue current caloric intake")


