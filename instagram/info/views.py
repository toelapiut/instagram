from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):

    image=Article.objects.all()

    return render(request,'index.html',{"images":image})


def search_results(request):

    if 'caption' in request.GET and request.GET["caption"]:
        search_term=request.GET.get("caption")
        searched_comment=Comment.search_by_comment_text(search_term)
        message=f"{search_term}"
        

        return render(request,'all-temps/search.html',{"message":message,"comment":searched_comment})
    else:
        message="You haven't searched for anyone"

        return render(request,'all-temps/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def user_profile(request,user_id):

    User_info=User.objects.get(id=user_id)
    article=Article.objects.get(pk=user_id)
    print(article)
    return render(request,'all-temps/profile.html',{"user_info":User_info,"article":article})


@login_required(login_url='/accounts/login/')
def image_reviews(request,article_id):
    current_user = request.user
    try:
        if request.method=='POST':
            form=CommentForm(request.POST)
            if form.is_valid():
                article = form.save(commit=True)
                article.user = current_user
                article.save()

        else:
            form=CommentForm()

        article=Article.objects.get(id=article_id)

    except DoesNotExist:
        raise HttpExist404()

    return render(request,'all-temps/article.html',{"article":article,"form":form})

@login_required(login_url='/accounts/login/')
def image_update(request):
    current_user = request.user
    try:
        if request.method=='POST':
            form = NewArticleForm(request.POST, request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.editor = current_user
                article.save()
        else:
            form=NewArticleForm()


    except DoesNotExist:
        raise HttpExist404()

    return render(request,'all-temps/profile.html',{"form":form})
