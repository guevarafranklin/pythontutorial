print("Welcome to the weight conversion !")
WeightInput = float(input("Enter your weight: "))
WeightType = str(input("Enter what metric you are, and the program will convert it to the other, (k)g or (l)bs: "))
NewWeight = 0.0
Metric = "NA"
if WeightType == "k" or WeightType == "K":
    NewWeight = WeightInput * 2.2
    Metric = "lbs"
elif WeightType == "l" or WeightType == "L":
    NewWeight = WeightInput * 0.45
    Metric = "kg"
else:
    print("You have to select k or l for starting the metric conversion")

print("You have converted  to ", Metric)
print("the conversion is: ", str(NewWeight), Metric)