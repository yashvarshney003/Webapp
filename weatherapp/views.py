from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
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
			data["error_code"] =  "City not found"
			 
	else:
		data = {}

	return render(request, "main/index.html", data)
 
