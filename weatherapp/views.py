from django.shortcuts import render
import urllib.request
import json
# Create your views here.
number_of_request = 0 
def index(request):
	global number_of_request
	number_of_request+=1 
	if(request.method == 'POST'):
		city =  request.POST['city']
		try:
			source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=acd57eb705c23fe2fe0de21a55ed1b05').read()
			print(f" source is {source}")
			
			list_of_data = json.loads(source)
			data = {} 
			if "error_code" in data.keys():
				del data["error_code"]

			data = {
				"number_of_request": str(number_of_request),
				"city": str(city),
				"country_code": str(list_of_data['sys']['country']),
				"coordinate": str(list_of_data['coord']['lon']) + ', '
				+ str(list_of_data['coord']['lat']),

				"temp": str(list_of_data['main']['temp']) + ' °C',
				"pressure": str(list_of_data['main']['pressure']),
				"humidity": str(list_of_data['main']['humidity']),
				'main': str(list_of_data['weather'][0]['main']),
				'description': str(list_of_data['weather'][0]['description']),
				'icon': list_of_data['weather'][0]['icon'],
			}
			print(data)
		except: 
			data = {}
			data["number_of_request"] =  str(number_of_request)
			data["error_code"] =  "City not found"
			 
	else:
		data = {}

	return render(request, "main/index.html", data)
 
