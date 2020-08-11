from django.shortcuts import render
from .models import AdditionalService, Service, Scenario


def index(request):
	return render(request, 'sbiv_mechts/osnova.html')

def svadba(request):
	return render(request, 'sbiv_mechts/svadba.html')
def lk(request):
		return render(request, 'sbiv_mechts/lk.html')

def katalog(request):
		return render(request, 'sbiv_mechts/katalog.html')
def classic(request):
		return render(request, 'sbiv_mechts/classic.html')
def viez_registric(request):
		return render(request, 'sbiv_mechts/viez_registric.html')
def uslugi(request):
	sv = Service.objects.get(id = 1)
	kor = Service.objects.get(id = 2)
	drr = Service.objects.get(id = 3)
	yub = Service.objects.get(id = 4)
	return render(request, 'sbiv_mechts/uslugi.html',{"sv": sv, "kor": kor , "drr": drr, "yub": yub})

def scenariy(request):
	cl = Scenario.objects.get(id = 1)
	mor = Scenario.objects.get( id = 2)
	isp = Scenario.objects.get(id = 3)
	prov = Scenario.objects.get(id = 4)
	stul = Scenario.objects.get(id = 5)
	stilyg = Scenario.objects.get(id = 6)
	return render(request, 'sbiv_mechts/scenariy.html',{"cl": cl, "mor": mor,"isp":isp, "prov":prov,"stul":stul,"stilyg":stilyg})
def ofic(request):
		return render(request, 'sbiv_mechts/ofic.html')
def rab(request):
		return render(request, 'sbiv_mechts/rab.html')
def lk_korzina(request):
		return render(request, 'sbiv_mechts/lk_korzina.html')
def artist(request):
	ofic = AdditionalService.objects.get(id = 1)
	shou = AdditionalService.objects.get(id = 2)
	focus = AdditionalService.objects.get(id = 3)
	pou = AdditionalService.objects.get(id = 4)
	return render(request, "sbiv_mechts/artist.html",{"ofic": ofic, "shou": shou , "focus": focus, "pou": pou})
