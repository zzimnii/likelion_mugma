from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm, CommentForm
from .models import Post, Comment, Profile
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def home(request):
    recipes = Post.objects.filter(category='V').order_by('-like_count')[:3]
    nrecipes = Post.objects.order_by('-like_count')[:3]
    return render(request, 'index.html', {'recipes':recipes, 'nrecipes':nrecipes})

def normal(request):
    recipes = Post.objects.order_by('date')
    paginator = Paginator(recipes, 6) #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page = request.GET.get('page') #GET 방식으로 정보를 받아오는 데이터
    recipes = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'normal.html',{'recipes':recipes})

def create(request):
    if (request.method == 'POST' or request.method == 'FILES'):
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('normal')
    else:
        form = PostModelForm()
    return render(request, 'postw.html', {'form':form})

def detail(request, recipe_id):
    recipe_detail= get_object_or_404(Post, pk=recipe_id)
    comments = Comment.objects.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        finished_form = comment_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=recipe_id)
        finished_form.author = request.user
        finished_form.save()
    return render(request, 'detail.html', {'recipe_detail':recipe_detail, 'comment_form': comment_form, 'comments':comments})

def update(request, recipe_id):
    original_recipe = Post.objects.get(id=recipe_id)
    if request.method == 'POST' or request.method == 'FILES':
        update_form = PostModelForm(request.POST, request.FILES)
        if update_form.is_valid():
            original_recipe.title = update_form.cleaned_data['title']
            original_recipe.recipe = update_form.cleaned_data['recipe']
            original_recipe.photo = update_form.cleaned_data['photo']
            original_recipe.save()
            return redirect('/detail/'+str(original_recipe.id))
    else:
        update_form = PostModelForm(instance=original_recipe)
        return render(request, 'form_update.html', {'update_form':update_form})

def delete(request, recipe_id):
    recipe = Post.objects.get(id=recipe_id)
    recipe.delete()
    return redirect('normal')

def likes(request, recipe_id):
    like_b = get_object_or_404(Post, id=recipe_id)
    if request.user in like_b.like.all():
        like_b.like.remove(request.user)
        like_b.like_count -= 1
        like_b.save()
    else:
        like_b.like.add(request.user)
        like_b.like_count += 1
        like_b.save()
    return redirect('/detail/' + str(recipe_id))

def NVtrendy(request):
    recipes = Post.objects.filter(category='NV').order_by('-like_count')[:10]
    paginator = Paginator(recipes, 5) #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page = request.GET.get('page') #GET 방식으로 정보를 받아오는 데이터
    recipes = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'trendy.html',{'recipes':recipes})

def Vtrendy(request):
    recipes = Post.objects.filter(category='V').order_by('-like_count')[:10]
    paginator = Paginator(recipes, 5) #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page = request.GET.get('page') #GET 방식으로 정보를 받아오는 데이터
    recipes = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'vegan.html',{'recipes':recipes})

def NVsteady(request):
    recipes = Post.objects.filter(category='NV').order_by('-like_count')[:5]
    return render(request, 'NVsteady.html',{'recipes':recipes})

def Vsteady(request):
    recipes = Post.objects.filter(category='V').order_by('-like_count')[:5]
    return render(request, 'Vsteady.html',{'recipes':recipes})

def mypage(request):
    return render(request, 'mypage.html')

def mugup(request):
    like_posts = Post.objects.filter(like=request.user)
    paginator = Paginator(like_posts, 4) #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page = request.GET.get('page') #GET 방식으로 정보를 받아오는 데이터
    like_posts = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'mugup.html', {'like_posts':like_posts})

def mugrap(request):
    return render(request, 'mypage.html')

def myprofile(request):
    return render(request, 'myprofile.html')

def mugchef(request):
    mugchefs = User.objects.all()
    paginator = Paginator(mugchefs, 10) #Paginator(분할될 객체, 페이지 당 담길 객체수)
    page = request.GET.get('page') #GET 방식으로 정보를 받아오는 데이터
    mugchefs = paginator.get_page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'mugchef.html',{'mugchefs':mugchefs})

def chefdetail(request, chef_id):
    chef = User.objects.get(pk=chef_id)
    chef_recipe = chef.post_set.all()
    return render(request, 'chefdetail.html', {'chef':chef, 'chef_recipe':chef_recipe})   