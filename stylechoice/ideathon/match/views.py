from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Match
from .forms import MatchForm


# Create your views here.

def home(request):
    matches = Match.objects.order_by('-pub_date') #all()말고 다른 method #-pub_date는 역순 = 최신글들이 위로 보여짐
    search = request.GET.get('search')
    if search == 'true':
        writer = request.GET.get('writer')
        matches = Match.objects.filter(writer=writer)
    paginator = Paginator(matches, 8)
    page = request.GET.get('page') #GET에 .get을 하면 정보가 없어도 표현가능하다.
    matches = paginator.get_page(page)
    return render(request, 'home.html', {'matches':matches})

def search(request):
    matchs = Match.objects.order_by('-pub_date')
    find = request.GET.get('find')
    if find == 'true':
        writer = request.GET.get('writer')
        matchs = Match.objects.filter(wrtier=writer)
    # paginator = Paginator(matchs, 8)
    # page = request.GET.get('page') #GET에 .get을 하면 정보가 없어도 표현가능하다.
    # matchs = paginator.get_page(page)
    return render(request, 'search.html', {'matchs':matchs})

def choice(request):
    return render(request, 'choice.html')

def detail(request,id):
    # match = Match.objects.get(id=id)
    match = get_object_or_404(Match, pk = id)
    return render(request, 'detail.html', {'match':match})

def new(request):
    form = MatchForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form = MatchForm(request.POST, request.FILES)
    if form.is_valid():
        new_match = form.save(commit=False) #pub_date를 담지 않았으니 임시저장을 해주어야함.
        new_match.writer = request.POST['writer']
        new_match.pub_date = timezone.now()
        # new_match.nickname = request.POST['nickname']
        new_match.save()
        return redirect('detail', new_match.id)
    return redirect('home')
    # new_match = Match()
    # new_match.title = request.POST['title']
    # new_match.writer = request.POST['writer']
    # new_match.nickname = request.POST['nickname']
    # new_match.body = request.POST['body']
    # new_match.pub_date = timezone.now()
    # new_match.image = request.FILES['image']
    # new_match.save()
    
    # return redirect('detail', new_match.id)

def edit(request, id):
    # edit_match = Match.objects.get(id=id)
    edit_match = get_object_or_404(Match, pk = id)
    return render(request, 'edit.html',{'match':edit_match})

def update(request, id):
    # update_match = Match.objects.get(id=id)
    update_match = get_object_or_404(Match, pk = id)
    update_match.title = request.POST['title']
    update_match.writer = request.POST['writer']
    update_match.body = request.POST['body']
    update_match.image = request.FILES['image']
    update_match.pub_date = timezone.now()
    update_match.save()
    return redirect('detail', update_match.id)

# def update(request, id):
#     update_match = Match.objects.get(id=id)
#     if request.method=="POST":
#         form = MatchForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             update_match.writer = form.cleaned_data['writer']
#             update_match.title = form.cleaned_data['titel']
#             update_match.body = form.cleaned_data['body']
#             update_match.image = form.cleaned_data['image']
#             update_match.pub_date = timezone.now()
#             update_match.save()
#             return redirect('detail', update_match.id)
#     else:
#         form = MatchForm()
#         context = {
#             'form':form,
#             'writing':True,
#             'now':'edit',
#         }
#         return render(request, 'edit.html',context)

    # edit_match = Match()
    # edit_match.title = request.POST['title']
    # edit_match.writer = request.POST['writer']
    # edit_match.nickname = request.POST['nickname']
    # edit_match.body = request.POST['body']
    # edit_match.pub_date = timezone.now()
    # edit_match.image = request.FILES['title']
    # edit_match.save()
    
    # return redirect('detail', edit_match.id)

def delete(request, id):
    delete_match = Match.objects.get(id=id)
    delete_match.delete()

    return redirect('home')

def picto(request):
    return render(request, 'pictogram.html')
