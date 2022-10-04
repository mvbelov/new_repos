from django.http import JsonResponse
from django.shortcuts import render


def json_get(request):
    data = {
        "arr_object": [{
            'id': 1,
            'name': 'Alex'
        },
            {
                'id': 2,
                'name': 'Sara'
            }]
    }

    return JsonResponse(data)


def json_page(request):
    return render(request, 'page1.html')
