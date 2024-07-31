from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Board, Comment
import json

# Create your views here.
def index(request):
    
    board_list = Board.objects.order_by('createdAt')
    data = list(board_list.values())
    print(data[0])
    return HttpResponse(data)
    #return render(request, 'board/board_list.html', context)
    #return JsonResponse(data, safe=False)
