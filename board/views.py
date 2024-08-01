from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Board, Comment
import json

# Create your views here.
def index(request):
    
    board_list = Board.objects.order_by('board_id')
    context = {'board_list' : board_list}
    
    return render(request, 'board/board_list.html', context)

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    context = {'board': board}
    return render(request, 'board/board_detail.html', context)

def create_board(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        writer_id = request.POST.get('writer_id')
        Board.objects.create(title=title, content=content, writer_id=writer_id)
        return redirect('board:index')
    return render(request, 'board/board_form.html')