from django.shortcuts import render, redirect, get_object_or_404 #get_object_or_404 : 찾을 수 없을경우 404를 띄어준다.
from django.utils import timezone # pub_date를 표현하기위하여
from .models import Match
from .forms import MatchForm


# Create your views here.

def home(request):
    matches = Match.objects.all()
    return render(request, 'home.html',{'matches':matches})

def detail(request,id):
    match = get_object_or_404(Match, pk = id)
    return render(request, 'detail.html',{'match': match})

def new(request):
    form = MatchForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = MatchForm(request.POST, request.FILES)
    if form.is_valid():
        new_match = form.save(commit=False)
        new_match.pub_date = timezone.now()
        new_match.save()
        return redirect('detail', new_match.id)#원래 있던 페이지로 돌아가야하기 때문에, pk가 id이기 떄문에 인자로 new_blog.id를 해줌
    return redirect('home') 
    # Blog.title = request.POST['title']
    # Blog.writer = request.POST['writer']
    # Blog.body = request.POST['body']
    # Blog.pub_date = timezone.now()
    # Blog.save() # 객체를 만들어서 사용해줘야하기 때문에 이 방법은 X


def edit(request, id):
    edit_match = Match.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_match})

   
def update(request, id):
    update_match = Match.objects.get(id = id)
    update_match.title = request.POST['title'] 
    update_match.writer = request.POST['writer']
    update_match.body = request.POST['body']
    update_match.pub_date = timezone.now()
    update_match.save()#안하면 DB에 적용이 안됨
    return redirect('detail', update_match.id)

def delete(request, id):
    delete_match = Match.objects.get(id = id)
    delete_match.delete()
    return redirect('home')