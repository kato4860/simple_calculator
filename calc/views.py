from django.shortcuts import render, reverse
import subprocess


def calc_view(request):
    if request.method == "POST" and 'start' in request.POST:
            #если нажата кнопка старт
            start = request.POST.get('start', False)
            print("запущено")
            #пропишем команду и путь до файла
            script = 'python calc/test.py'
            #os.system(script)
            #выпоним команду в терминале
            subprocess.Popen(script, shell=True)

            return redirect('/calc/index.html', {'start': start})
    """
    Принимаем от пользователя строку
    с математическим выражением +-/*
    """

    template_name = 'calc/index.html'
    result = request.POST.get('solution')
    print(f'RESULT ===>>> {result}')

    if result is None:
        result = '''
        Для расчёта введите два значения.
        Разделяя знаками + - * / **
        '''

    elif '+' in result:
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
