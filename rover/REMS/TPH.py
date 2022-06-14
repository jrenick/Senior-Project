#############################################################
# 
# Author: James Renick
# Date: June 2022 Spring Quarter
# Senior Project
#
#############################################################

import csv
import math
import time  
import REMS.bme280_Read as BME

#Calling the function in the bme280_Read file to return the temperature, humidity, and pressure measurements
temperature,pressure,humidity = BME.readBME280All()

#getter function to return Temperature measurement
def getTemperature():
    temperature,pressure,humidity = BME.readBME280All()
    print("Temperature: %0.1f C" % temperature)
    return temperature

#getter function to return Humidity measurement
def getHumidity():
    temperature,pressure,humidity = BME.readBME280All()
    print("Humidity: %0.1f %%" % humidity)
    return humidity

#getter function to return Pressure measurement
def getPressure():
    temperature,pressure,humidity = BME.readBME280All()
    print("Pressure: %0.1f hPa" % pressure)
    return pressure

#getter function to return Dewpoint measurement
def getDewPoint():
    temperature,pressure,humidity = BME.readBME280All()
    b = 17.62
    c = 243.12
    gamma = (b * temperature / (c + temperature)) + math.log(humidity / 100.0)
    #The atmospheric temperature below which water droplets begin to condense and dew can form.
    dewpoint = (c * gamma) / (b - gamma)
    print("Dewpoint: %0.1f C " % dewpoint)
    return dewpoint

#Fuction that writes all 4 measurements to a CSV file
def writeToCSV():

    #CVS Header
    header = ['Temperature(C)', 'Humidity(%)', 'Pressure(hPa)', 'Dewpoint(C)']

    #Array to hold Sensor measurement readings
    REMS = []

    #opening CSV file to write to
    with open('REMS.csv', 'w', encoding='UTF8') as csvFile:
        csvWriter = csv.writer(csvFile)
        count = 0
        #writes the header to the first row of CSV file
        csvWriter.writerow(header)
        
        #while loop stores each sensor reading into Array and then write that List into the CSV file
        while count < 5:
            temperature,pressure,humidity = BME.readBME280All()
            REMS.append(temperature)
            REMS.append(humidity)
            REMS.append(pressure)
            #Dewpoint calculations
            b = 17.62
            c = 243.12
            gamma = (b * temperature / (c + temperature)) + math.log(humidity / 100.0)
            #The atmospheric temperature below which water droplets begin to condense and dew can form.
            dew = (c * gamma) / (b - gamma)
            REMS.append(dew)
            csvWriter.writerow(REMS)
            REMS.clear()
            #time.sleep(1)
            count = count + 1

#f.close
#-----------------------------------------------------------------------------------------
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT