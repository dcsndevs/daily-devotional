from django.shortcuts import render


def bible(request):
    return render(request, 'bible/index.html')