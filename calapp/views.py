from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    expression = request.POST.get('expression', '')
    btn = request.POST.get('btn', '')
    result = ''

    if btn == 'C':
        expression = ''
        result = ''
    elif btn == 'backspace':
        expression = expression[:-1]
    elif btn == '=':
        try:
            # Simple eval for learning/demo. Replace with safe_eval later
            result = str(eval(expression))
        except:
            result = 'Error'
    else:
        expression += btn

    return render(request, 'calapp/index.html', {
        'expression': expression,
        'result': result
    })

def home(request):
    expression = request.POST.get('expression','')
    result = ''
    btn = request.POST.get('btn','')

    if btn == 'C':
        result = ''
        expression = ''
    elif btn == 'backspace':
        expression = expression[:-1]
    elif btn == '=':
        try:
            result = str(eval(expression))
        except:
            result = 'Error'
    else:
        expression += btn
    return render(request,'calapp/index.html',{'expression':expression,'result':result})