from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import ArticleForm
from django.http import HttpResponse
from . models import Article

# Create your views here.

@login_required(login_url='my-login')
def writer_dashboard (request):
    return render(request, 'writer/writer-dashboard.html')


@login_required(login_url='my-login')
def create_article (request):
    
    form = ArticleForm
    
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect ('my-articles')

    context = {'CreateArticleForm': form}
    
    return render (request, 'writer/create-article.html', context)


@login_required(login_url='my-login')
def my_articles(request):
    
    current_user = request.user.id
    article = Article.objects.all().filter(user=current_user)
    context = {'AllArticles' : article}
    return render (request, 'writer/my-articles.html', context)



@login_required(login_url='my-login')
def update_article(request, pk):
    
    #retrieve the article ID
    article = Article.objects.get(id=pk)
    
    #pass specific instance of the article
    form = ArticleForm(instance=article)
    
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        
        #check if valid
        if form.is_valid():
            form.save()
            return redirect ('my-articles')
        
    context = {'UpdateArticleForm' : form}    
    
    return render (request, 'writer/update-article.html', context)
            
    
    
    
    
    