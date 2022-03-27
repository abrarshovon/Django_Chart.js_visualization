from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import JsonModel
def index(request):
    f = open('./stock_market_data.json')
    data = json.load(f)
    si= len(data)
    return render(request, 'showJson/index.html', {'data': data, 'si':si})
#def home(request):
   # jsonmodel= JsonModel.objects.all()

  #S  return render(request, 'showJson/main.html', {'data': jsonmodel})
class JsonListView(ListView):
    paginate_by = 20
    model = JsonModel
    template_name= 'showJson/main.html'
    context_object_name= 'data'

class JsonDetailView(DetailView):
    model = JsonModel
    template_name= 'showJson/jsondetail.html'
    context_object_name= 'heda'
class JsonCreateView(CreateView):
    model = JsonModel
    template_name= 'showJson/jsoncreate.html'
    fields=['id', 'date','trade_code','high','low','open','close','volume']
    success_url="/json/"
class JsonUpdateView(UpdateView):
    model = JsonModel
    template_name= 'showJson/jsoncreate.html'
    fields=['date','trade_code','high','low','open','close','volume']
    success_url="/json/"
class JsonDeleteView(DeleteView):
    model = JsonModel
    template_name= 'showJson/confirm.html'
    success_url="/json/"