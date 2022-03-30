from django.shortcuts import render
from django.http import JsonResponse
from .chat import get_response
# Create your views here.


def home(request):
    return render(request, 'chat.html')


def msg(request):
    if request.method == 'POST':
        m = request.POST['msg']
        msg = get_response(m)
        return JsonResponse({'success': 'true', 'msg': msg}, safe=False)
    return JsonResponse({'success': 'false'})
