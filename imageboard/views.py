from django.shortcuts import render
from .models import Post, Thread, Board, FilePost, FileThread
from .forms import PostForm, ThreadForm, PostFileForm, ThreadFileForm


def mainpage(request):
    boards = Board.objects.all()
    context = {'boards': boards}
    return render(request, 'imageboard/mainpage.html', context=context)


def board(request, board_l):
    boardlist = Board.objects.all()
    threads = Thread.objects.filter(board__letter=board_l)
    current_board = Board.objects.get(letter=board_l)
    files = FileThread.objects.all()
    if request.POST:
        form = ThreadForm(request.POST)
        form_file = ThreadFileForm()
        files = request.FILES.getlist('file')
        if form.is_valid():
            thread_instance = form.save(commit=False)
            thread_instance.save()
            for file in files:
                file_instance = FileThread(file=file, thread=thread_instance)
                file_instance.save()
    else:
        form_file = ThreadFileForm
        form = ThreadForm(initial={'board': current_board})
    context = {'threads': threads, 'current_board': current_board, 'form': form, 'boards': boardlist,
               'files': files,
               'form_file': form_file}
    return render(request, 'imageboard/board.html', context=context)


def thread(request, thread_n, board_l):
    boardlist = Board.objects.all()
    current_board = Board.objects.get(letter=board_l)
    current_thread = Thread.objects.get(pk=thread_n)
    current_thread_files = FileThread.objects.filter(thread=current_thread)
    posts = Post.objects.filter(thread_id=thread_n)
    files = FilePost.objects.filter(post__thread_id=thread_n)
    if request.POST:
        form = PostForm(request.POST)
        form_file = PostFileForm()
        if form.is_valid():
            post_instance = form.save(commit=False)
            post_instance.save()
            for file in request.FILES.getlist('file'):
                file_instance = FilePost(file=file, post=post_instance)
                file_instance.save()
    else:
        form_file = PostFileForm()
        form = PostForm(initial={'board': current_board,
                                 'thread': current_thread})
    context = {
        'current_board': current_board,
        'current_thread': current_thread,
        'form': form,
        'form_file': form_file,
        'posts': posts,
        'boards': boardlist,
        'files': files,
        'current_thread_files': current_thread_files,
    }
    return render(request, 'imageboard/thread.html', context=context)
