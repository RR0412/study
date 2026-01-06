from django.shortcuts import render

def index_view(request):
    return render(request, 'calculatorapp/index.html')

def calculate(request):
    if request.method == 'GET':
        return render(request, 'calculatorapp/form.html')
    elif request.method == 'POST':
        context = {
            'number1': request.POST.get('number1'),
            'number2': request.POST.get('number2'),
            'operation': request.POST.get('operation')
        }
        if context['operation'] == 'add':
            sign = '+'
            result = int(context['number1']) + int(context['number2'])
        elif context['operation'] == 'subtract':
            sign = '-'
            result = int(context['number1']) - int(context['number2'])
        elif context['operation'] == 'multiply':
            sign = '*'
            result = int(context['number1']) * int(context['number2'])
        elif context['operation'] == 'divide':
            sign = '/'
            result = int(context['number1']) / int(context['number2'])
        context['result'] = str(result)
        context['sign'] = sign 
        return render(request, 'calculatorapp/calculation.html',context)
