import re
import urllib.request

#https://www.weather-forecast.com/locations/Dublin/forecasts/latest

city = input("Enter your city: ")
url = "https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
print(url)
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)

m = re.search('span class="phrase"',data1)
start = m.end()
end = start + 200
newString = data1[start:end]


m = re.search("</span>",newString)
end = m.start()-1
final = newString[0:end]
print(final)
