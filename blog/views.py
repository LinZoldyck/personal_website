from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from .models import Article, Author

# Create your views here.
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'summary','slug', 'author']



def index(request):
    Articles = Article.objects.all()
    return render(request, 'blog/index.html', {'Articles':Articles})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/detail.html', {'article':article})

def create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request,'blog/form.html', {'form':form})

def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blog/form.html', {'form':form })

def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method=='POST':
        article.delete()
        return redirect('index')
    return render(request, 'blog/delete.html', {'article':article})