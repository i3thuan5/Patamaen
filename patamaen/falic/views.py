from django.shortcuts import render


def falic(request):
    return render(request, template_name='patamaen/falic.html')
