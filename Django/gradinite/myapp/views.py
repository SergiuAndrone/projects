from django.shortcuts import render
from .models import gradinitaModel


def home(request):

    numar_gradinite = gradinitaModel.objects.all().count()
    context = {'numar_gradinite': numar_gradinite}

    return render(request, "home.html", context=context)


def gradinite_private_sector1(request):
    nr_gradinite = gradinitaModel.objects.all()
    context = {'gradinite': {}}

    for item in nr_gradinite:
        if item.sector.lower() == 'sector 1' and item.tip.lower() == 'privata':
            context['gradinite'][item.nume] = item.adresa
            print(context)
    return render(request, 'gradinite_private/gradinite_private_sector1.html', context=context)


def gradinite_private_sector2(request):
    return render(request, 'gradinite_private/gradinite_private_sector2.html')


def gradinite_private_sector3(request):
    return render(request, 'gradinite_private/gradinite_private_sector3.html')


def gradinite_private_sector4(request):
    return render(request, 'gradinite_private/gradinite_private_sector4.html')


def gradinite_private_sector5(request):
    return render(request, 'gradinite_private/gradinite_private_sector5.html')


def gradinite_private_sector6(request):
    return render(request, 'gradinite_private/gradinite_private_sector6.html')


def gradinite_private_ilfov(request):
    return render(request, 'gradinite_private/gradinite_private_ilfov.html')


def gradinite_stat_sector1(request):
    return render(request, 'gradinite_stat/gradinite_stat_sector1.html')


def gradinite_stat_sector2(request):
    return render(request, 'gradinite_stat/gradinite_stat_sector2.html')


def gradinite_stat_sector3(request):
    return render(request, 'gradinite_stat/gradinite_stat_sector3.html')


def gradinite_stat_sector4(request):
    return render(request, 'gradinite_stat/gradinite_stat_sector4.html')


def gradinite_stat_sector5(request):
    return render(request, 'gradinite_stat/gradinite_stat_sector5.html')


def gradinite_stat_sector6(request):
    return render(request, 'gradinite_stat/gradinite_stat_sector6.html')


def gradinite_stat_ilfov(request):
    return render(request, 'gradinite_stat/gradinite_stat_ilfov.html')


def inscriere(request):
    return render(request, 'inscriere.html')


def contact(request):
    return render(request, 'contact.html')

