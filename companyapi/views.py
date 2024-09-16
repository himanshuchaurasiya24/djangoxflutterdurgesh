from django.http import HttpResponse, JsonResponse
def homepage(request):
    print('homepage requested.')
    friends = ['himanshu', 'shishir', 'anuj', 'ankit']
    # return HttpResponse('This is a Homepage.')
    return JsonResponse(friends, safe=False)