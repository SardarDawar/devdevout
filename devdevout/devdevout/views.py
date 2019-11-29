from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def base(request, slug):
    categories = Category.objects.get(slug=slug)
    lists = code_post.objects.filter(status="published")
    blogs = code_post.objects.filter(catagory=categories, status="published")

    context = {
        'blogs': blogs,
        'list': lists
    }
    return render(request, 'category.html', context)


def base1(request):
    categories = Category.objects.all()
    print(categories)
    context = {
        'cat': categories
    }
    return render(request, 'base.html', context)


def BlogList(request):
    blog = code_post.objects.filter(status='published')
    article = Article.objects.filter(status='published')

    paginator = Paginator(blog, 12)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:

        blogs = paginator.page(1)
    except EmptyPage:

        blogs = paginator.page(paginator.num_pages)

    for i in (blogs):
        i.description = i.description[:500]
    
    context = {
        'blogs': blogs,
        'blog': blog,
        'article':article,
    }
    return render(request, 'bloglist.html', context)


def BlogDetail(request, slug):
    lis = code_post.objects.filter(status="published")
    blogs = code_post.objects.get(slug=slug, status="published")
    examples = example.objects.filter(code_post=blogs)

    print(examples)

    context = {
        'blogs': blogs,
        'example': examples,
        'list': lis,
      

    }
    return render(request, 'blogdetail.html', context)

def BlogDetailArticle(request, slug0):
    lis = Article.objects.filter(status="published")
    articles = Article.objects.get(slug=slug0, status="published")

    context = {

        'list': lis,
        'blogs':articles

    }
    return render(request, 'blogdetailarticle.html', context)


def BlogAuthors(request):
    authors = BlogAuthor.objects.all()

    paginator = Paginator(authors, 12)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:

        blogs = paginator.page(1)
    except EmptyPage:

        blogs = paginator.page(paginator.num_pages)

    for i in (blogs):
        i.description = i.description[:500]
    print(blog)
    context = {
        'blogs': blogs,
        'blog': blog
    }

    context = {
        'authors': blogs
    }

    return render(request, 'authorlist.html', context)


def BlogListByAuthor(request, id):
    target_author = BlogAuthor.objects.get(id=id)
    print(target_author)
    blogs = code_post.objects.filter(author=target_author)
    context = {
        'blogs': blogs,
        'author': target_author
    }
    return render(request, 'authorblogs.html', context)


def search(request):

    query = request.GET.get('query', None)
    listing = code_post.objects.filter(status="published")
    listing1 = Article.objects.filter(status="published")
    blogs = code_post.objects.filter(status="published")
    article = Article.objects.filter(status="published")
    if query is not None:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(catagory__Name__icontains=query) |
            Q(author__author__username__icontains=query)

        )
  
       
        article= article.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(catagory__Name__icontains=query) |
            Q(author__author__username__icontains=query)

        )
    print(blogs)
    print(article)
    
    paginator = Paginator(blogs, 12)

    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:

        blogs = paginator.page(1)
    except EmptyPage:

        blogs = paginator.page(paginator.num_pages)

    context = {

        'blogs': blogs,
        'list': listing,
        'list1': listing1,
        'query': query,
        'article':article,
    }

    return render(request, 'search.html', context)


def about(request):
    return render(request, 'about.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})


def affiliations(request):
    return render(request, 'affiliations.html', {})


# def html(request):
#     return render(request,'html.html',{})
# def css(request):
#     return render(request,'css.html',{})
# def js(request):
#     return render(request,'js.html',{})
def html(request):
    categories = Category.objects.get(slug='html')
    lists = code_post.objects.filter(status="published")
    blogs = code_post.objects.filter(catagory=categories, status="published")

    context = {
        'blogs': blogs,
        'list': lists
    }
    return render(request, 'html.html', context)


def css(request):
    categories = Category.objects.get(slug='css')
    lists = code_post.objects.filter(status="published")
    blogs = code_post.objects.filter(catagory=categories, status="published")

    context = {
        'blogs': blogs,
        'list': lists
    }
    return render(request, 'css.html', context)


def js(request):
    categories = Category.objects.get(slug='javascript')
    lists = code_post.objects.filter(status="published")
    blogs = code_post.objects.filter(catagory=categories, status="published")

    context = {
        'blogs': blogs,
        'list': lists
    }
    return render(request, 'js.html', context)

def fashion(request):
    categories = Category.objects.get(slug='fashion')
    lists = code_post.objects.filter(status="published")
    sub=Sub_Category.objects.filter(Category=categories)
    blogs = code_post.objects.filter(catagory=3, status="published")
    articles = Article.objects.filter(catagory=3, status="published")


    context = {
        'blogs': blogs,
        'list': lists,
        'articles':articles,
        'sub':Sub_Category,
    }
    return render(request, 'fashion.html', context)
def finance(request):
    categories = Category.objects.get(slug='finance')
    lists = code_post.objects.filter(status="published")
    sub=Sub_Category.objects.filter(Category=categories)
    blogs = code_post.objects.filter(catagory=4, status="published")
    articles = Article.objects.filter(catagory=4, status="published")


    context = {
        'blogs': blogs,
        'list': lists,
        'articles':articles,
        'sub':Sub_Category,
    }
    return render(request, 'finance.html', context)

def Software(request):
    categories = Category.objects.get(slug='software')
    lists = code_post.objects.filter(status="published")
    sub=Sub_Category.objects.filter(Category=categories)
    blogs = code_post.objects.filter(catagory=categories.id, status="published")
    articles = Article.objects.filter(catagory=categories.id, status="published")


    context = {
        'blogs': blogs,
        'list': lists,
        'articles':articles,
        'sub':Sub_Category,
    }
    return render(request, 'software.html', context)
def Technology(request):
    categories = Category.objects.get(slug='technology')
    lists = code_post.objects.filter(status="published")
    sub=Sub_Category.objects.filter(Category=categories)
    blogs = code_post.objects.filter(catagory=categories.id, status="published")
    articles = Article.objects.filter(catagory=categories.id, status="published")


    context = {
        'blogs': blogs,
        'list': lists,
        'articles':articles,
        'sub':Sub_Category,
    }
    return render(request, 'technology.html', context)
def Home_Life(request):
    categories = Category.objects.get(slug='home_life')
    lists = code_post.objects.filter(status="published")
    sub=Sub_Category.objects.filter(Category=categories)
    blogs = code_post.objects.filter(catagory=categories.id, status="published")
    articles = Article.objects.filter(catagory=categories.id, status="published")


    context = {
        'blogs': blogs,
        'list': lists,
        'articles':articles,
        'sub':Sub_Category,
    }
    return render(request, 'home_life.html', context)
def myView(request, param):
    if not param:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

    return render_to_response('404.html')


def myView1(request, param):
    if not param:
        return HttpResponseNotFound('<h1>No Page Here</h1>')

    return render_to_response('500.html')



