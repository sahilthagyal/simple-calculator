from django.shortcuts import render

def home(request):
    expression = request.POST.get('expression', '')
    btn = request.POST.get('btn', '')
    result = ''

    if request.method == "POST":

        if btn == 'C':
            expression = ''
            result = ''

        elif btn == 'backspace':
            expression = expression[:-1]

        elif btn == '=':
            try:
                result = str(eval(expression))
            except:
                result = "Error"

        else:
            # Append number/operator
            expression += btn

    return render(request, 'calapp/index.html', {
        'expression': expression,
        'result': result,
    })
