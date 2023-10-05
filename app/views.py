from django.shortcuts import render

# Create your views here.
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from app.models import *
from app.forms import *

#FBV by using HttpResponse
def fbv_string(request):
    return HttpResponse('This is FBV response')

#CBV by using HttpResponse
class cbv_string(View):
    def get(self,request):
        return HttpResponse('This is CBV response')
    
#FBV by using html page
def fbv_page(request):
    return render(request,'fbv_page.html')

#CBV by using html page
class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')
    
#insert FBV by using Html   
def insert_fbv(request):
    SFO=studentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=studentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data inserted successfully')
    return render(request,'insert_fbv.html',d)

#insert CBV by using Html 
class insert_cbv(View):
    def get(self,request):
        SFO=studentForm()
        d={'SFO':SFO}
        return render(request,'insert_cbv.html',d)
    def post(self,request):
        SFDO=studentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
        return HttpResponse('data inserted successfully')

#TempView by using Html Page
class insert_TEMP(TemplateView):
    template_name='insert_TEMP.html'