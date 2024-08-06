from django.shortcuts import render

def class_based_view(request):
    return render(request, 'second_task/class_based_view.html')

def function_based_view(request):
    return render(request, 'second_task/function_based_view.html')