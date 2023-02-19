from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def omlet(request):
    servings = request.GET.get("servings")
    if servings == None:
        context = {
            'recipe': DATA['omlet'], 'name': 'Омлет'
        }
    else:
        dic = {}
        for key, value in DATA['omlet'].items():
            dic[key] = value * int(servings)
        context = {
                'recipe': dic, 'name': 'Омлет'
            }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = request.GET.get("servings")
    if servings == None:
        context = {
            'recipe': DATA['pasta'], 'name': 'Паста'
        }
    else:
        dic = {}
        for key, value in DATA['pasta'].items():
            dic[key] = value * int(servings)
        context = {
            'recipe': dic, 'name': 'Паста'
        }
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = request.GET.get("servings")
    if servings == None:
        context = {
            'recipe': DATA['buter'], 'name': 'Бутерброт'
        }
    else:
        dic = {}
        for key, value in DATA['buter'].items():
            dic[key] = value * int(servings)
        context = {
            'recipe': dic, 'name': 'Бутерброт'
        }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
