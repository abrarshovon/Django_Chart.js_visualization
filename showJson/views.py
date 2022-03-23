from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):
    f = open('./stock_market_data.json')
    data = json.load(f)
    si= len(data)
    return render(request, 'showJson/index.html', {'data': data, 'si':si})


