from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        start_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b2bc4c8d73b9279180f8ebabe89bf707"

        print(start_url)
        url = start_url.replace(" ", "")
        print(url)

        source = urllib.request.urlopen(url).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)
        print(list_of_data)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
            + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'city': city

        }
        print(data)
        return render(request, "index.html", data)

    else:

        return render(request, "index.html")
