from django.shortcuts import render

# Create your views here.

def add(request):
    if request.method=="POST":
        number1=int(request.POST.get("txt_number1"))
        number2=int(request.POST.get("txt_number2"))
        result=number1 + number2
        return render(request, 'Basics/Add.html',{'sum':result})
    else:
        return render(request, 'Basics/Add.html')

def largest(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt_number1"))
        num2=int(request.POST.get("txt_number2"))
        if num1 >num2:
            result = num1
        else:
            result = num2
        return render(request, 'Basics/Largest.html',{'Largest':result})
    else:
        return render(request, 'Basics/Largest.html')

def calculator(request):
    if request.method=="POST":
        number1=int(request.POST.get("txt_number1"))
        number2=int(request.POST.get("txt_number2"))
        operator=request.POST.get("operator")
        if operator=="+":
            result=number1 + number2
        elif operator=="-":
            result=number1 - number2
        elif operator=="*":
            result=number1 * number2
        elif operator=="/":
            result=number1 / number2
        return render(request, 'Basics/Calculator.html',{'sum':result})
    else:
        return render(request, 'Basics/Calculator.html')