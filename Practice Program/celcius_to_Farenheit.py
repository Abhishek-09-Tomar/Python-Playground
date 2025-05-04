# topic - change the temperature from celcius to farenheit

# formula to convert celcius to farenheit : F = (C * 9/5) + 32

# take input from the user as temperature in celcius
temp_in_celcius = float(input("enter the temperature in celcius : "))

# convert the temperature from celcius to farenheit.
temp_in_farenheit = temp_in_celcius * (9/5) + 32

# print the result
print(temp_in_celcius, "degree celcius = ",temp_in_farenheit, "degree Farenheit")