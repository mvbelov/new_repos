from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def get_json(request):
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


def get_page(request):
    return render(request, 'page1.html')
