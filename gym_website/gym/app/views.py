from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def programs(request):
    return render(request, 'programs.html')

def trainers(request):
    return render(request, 'trainers.html')

def memberships(request):
    return render(request, 'memberships.html')

def contact(request):
    return render(request, 'contact.html')

def demo(request):
    return render(request, 'demo.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

