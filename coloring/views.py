from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def home_screen(request):
    return render(request, 'coloring/home_screen.html')

def timer_screen(request):
    return render(request, 'coloring/timer_screen.html')

def timer_screen_update(request):
    return render(request, 'coloring/timer_screen_update.html')

def template_1(request):
    return render(request, 'coloring/template_1.html')

def template_2(request):
    return render(request, 'coloring/template_2.html')