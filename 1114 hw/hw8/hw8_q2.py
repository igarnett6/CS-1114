'''

Your name
CS 1114
Your netID

Purpose of program
'''


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    fileName = complete_weather_filename
    cleanFileName = cleaned_weather_filename
    precipList = []
    firstPartList = []
    file = open(fileName, "r")
    cleanFile = open(cleanFileName, "w")
    count = 0
    for line in file:
        count += 1
    for line in file:
        for i in range(8):
           precipitation = line.lstrip(",")
        precipList.append(precipitation)
    for line in file:
        for j in range(4)
            firstPart = line.rstrip(",")
        firstPartList.append(firstPart)
    for k in range(count):
        cleanFile.writeline(firstPartList[k] + precipList[k])


# Part B
def f_to_c(f_temperature):
    return (f_temperature-32)*(5/9) # modify this

def in_to_cm(inches):
    return inches*2.54 # modify this

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    # Similar to clean_data() - read in the file and make a new file with metric values.



# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    # prints average highs and lows in each month for the given city



# Part D
# Write your question (as a comment), and implement a function to answer it



def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    # add your code here
    

    
main()
