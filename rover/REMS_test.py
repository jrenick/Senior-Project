import REMS.TPH as TPH
 
temp = TPH.getTemperature()
temp = TPH.getTemperature()
press = TPH.getPressure()
press = TPH.getPressure()
humid = TPH.getHumidity()
humid = TPH.getHumidity()
dew = TPH.getDewPoint()
dew = TPH.getDewPoint()
 
TPH.writeToCSV()