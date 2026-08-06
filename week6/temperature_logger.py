#  Temperature Logger (math module)

import math  # math utility for performing math operations

# provided input
temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]
station_name = "Kathmandu Weather Station"


# get average function that returns the mean temperature
def get_average(temps):
    # inside math library, we don't have a mean or
    #  average method unlike statistics library
    return sum(temps) / len(temps)


# returns the standard deviation
def get_deviation(temps):
    # local variable "mean" for accessing the mean returned by the get_average()
    mean = get_average(temps)
    # inside math library, we don't have a stdev
    #  method unlike statistics library
    # thus, we have to manually calculate it
    variance = 0
    # for calculating stdev, we need variance
    for i in temps:
        variance += (i - mean) ** 2

    variance = variance / len(temps)
    # sqert of variance is stdev
    standard_deviation = math.sqrt(variance)

    return standard_deviation


# get summary function to return the summary stats
def get_summary(temps):
    print(f"{station_name}")
    print(f"Minimum Temperature: {min(temps)}")
    print(f"Maximum Temperature: {max(temps)}")
    print(f"Average Temperature: {get_average(temps)}")
    print(f"Standard Deviation: {get_deviation(temps):.2f}")


# calling the function
get_summary(temperatures)

# print(mean)
# this will generate a NameError
# mean is defined in a local scope, only inside the get_deviation() function
# thus it cannot be accessed outside the function unlike the variable "station_name"
