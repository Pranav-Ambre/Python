seconds=4000
hours = int (seconds /3600)
minutes = int ((seconds % 3600) / 60)
seconds = seconds % 60
print("Hours=", hours)
print("Minutes=", minutes)
print("Seconds=", seconds)

