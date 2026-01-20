from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Article

def index_view(request):
    articles = Article.objects.all()
    return render(request,'index.html', context = {'articles': articles})

def article_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'article_create.html',{'status_choices': Article.StatusChoices.choices})
    elif request.method == 'POST':    
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        status = request.POST.get('status') or Article.StatusChoices.ACTIVE
        article = Article.objects.create(title=title, text=text, author=author,status=status)       
        return redirect('article_view', pk=article.pk)

def article_view(request,pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', context={'article': article
    })

