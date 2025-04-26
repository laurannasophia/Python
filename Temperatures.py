def celciusToFahrenheit():
    fahrenheit = int(celcius * 1.8 + 32)
    result = print(str(celcius) + "C" + " = " + str(fahrenheit) + "F")
    return result

def celciustoKelvin():
    kelvin = int(celcius + 273.15)
    result = print(str(celcius) + "C" + " = " + str(kelvin) + "K")
    return result

celcius = input("Syötä lämpötila celsiuksissa ")
celcius = int(celcius)

celciusToFahrenheit()
celciustoKelvin()