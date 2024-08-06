from django.shortcuts import render

def home(request):
    return render(request, 'third_task/home.html')

def shop(request):
    return render(request, 'third_task/shop.html')

def cart(request):
    return render(request, 'third_task/cart.html')