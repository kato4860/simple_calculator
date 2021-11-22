from django.shortcuts import render, reverse


def calc_view(request):
    """
    Принимаем от пользователя строку
    с математическим выражением +-/*
    """

    template_name = 'calc/index.html'
    result = request.POST.get('solution')
    print(result)

    if '+' in result:
        solution = result.split('+')
        print(solution)
        result = float(solution[0]) + float(solution[1])

    elif '-' in result:
        solution = result.split('-')
        result = float(solution[0]) - float(solution[1])

    elif '/' in result:
        solution = result.split('/')
        result = float(solution[0]) / float(solution[1])

    elif '**' in result:
        solution = result.split('**')
        result = float(solution[0]) ** float(solution[1])

    elif '*' in result:
        solution = result.split('*')
        result = float(solution[0]) * float(solution[1])

    context = {
        'result': result
    }

    return render(request, template_name, context)
