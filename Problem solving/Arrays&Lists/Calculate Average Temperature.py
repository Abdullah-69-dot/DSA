DaysNumber = int(input("Enter the number of days: "))
Temps = []
for i in range(DaysNumber):
    DayTemp = float(input(f"Enter the temperature for day {i+1}: "))
    Temps.append(DayTemp)
AVG = sum(Temps)/DaysNumber
print("The average temperature is: ", AVG)