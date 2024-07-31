from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Board, Comment
import json

# Create your views here.
def index(request):
    
    board_list = Board.objects.order_by('board_id')
    data = list(board_list.values())
    print(data[0])
    return HttpResponse(data)
    #return render(request, 'board/board_list.html', context)
    #return JsonResponse(data, safe=False)

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    context = {'board': board}
    return render(request, 'board/board_detail.html', context)
