from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Board, Comment, User
import json

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        pw = request.POST.get('user_pw')
        users = User.objects.filter(user_email=email, user_pw=pw)
        if users.exists():
            for user in users:
                request.session['user_info'] = {
                'user_email': user.user_email,
                'user_name' : user.user_name
                }
            return redirect('board:index')
    return redirect('board:login_page')

def login_page(request):
    return render(request, 'board/board_login.html')

def signup_page(request):
    return render(request, 'board/board_signup.html')

def signup(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        user_name = request.POST.get('user_name')
        user_pw = request.POST.get('user_pw')
        user = User.objects.create(user_email=user_email, user_name=user_name, user_pw=user_pw)
        request.session['user_info'] = {
            'user_email': user.user_email,
            'user_name' : user.user_name
        }
        return redirect('board:login')
    return render(request, 'board/board_signup.html')

def index(request):
    
    board_list = Board.objects.order_by('board_id')
    context = {
        'board_list' : board_list,
        'user' : request.session.get('user')
    }
    
    return render(request, 'board/board_list.html', context)

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    comment = Comment.objects.filter(board_id=board_id)
    context = {
        'board': board,
        'comment': comment
    }
    return render(request, 'board/board_detail.html', context)

def create_board(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        user_name = request.POST.get('user_name')
        users = User.objects.filter(user_name=user_name)
        cnt = 0
        for user in users:
            if cnt <= 1:
                Board.objects.create(title=title, content=content, user_id=user.user_id)
            return redirect('board:index')
        cnt+=1
    return render(request, 'board/board_form.html')

def create_comment(request, board_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        user_name = request.POST.get('user_name')
        users = User.objects.filter(user_name=user_name)
        board = get_object_or_404(Board, pk=board_id)
                 
        cnt = 0
        for user in users:
            if cnt <= 1:
                Comment.objects.create(board_id=board, content=content,user_id=user.user_id)
        return redirect('board:index')
    return render(request, 'board/board_detail.html')