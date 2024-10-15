from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def Home(request):
    popular_post = Post.objects.filter(Section='Popular', Status=1).order_by('-id')[0:4]
    recent_post = Post.objects.filter(Section='Recent', Status=1).order_by('-id')[0:4]
    main_post = Post.objects.filter(Main_Post=True, Status=1)[0:1]
    Editors_Pick =Post.objects.filter(Section='Editors_Pick', Status=1).order_by('-id')
    Trending = Post.objects.filter(Section='Treanding', Status=1).order_by('-id')
    Inspiration = Post.objects.filter(Section='Inspiration', Status=1).order_by('-id')[0:6]
    Latest_post = Post.objects.filter(Section='Latest_Post', Status=1).order_by('-id')[0:4]
    category = Category.objects.all()
    context = {'popular_post':popular_post, 'recent_post':recent_post, 'main_post': main_post, 'Editors_Pick': Editors_Pick, 'Trending':Trending, 'Inspiration': Inspiration,'Latest_post':Latest_post, 'category':category}
    
    return render(request, 'app/index.html', context)





def Blog(request):
    blogs = Post.objects.all().order_by('-id')
    popular_post = Post.objects.filter(Section='Popular', Status=1).order_by('-id')[0:4] #this is send in the template because of the get data in the slidebar. 
    category = Category.objects.all() #this is send in the template because of the get data in the slidebar. 
    context = {'blogs':blogs, 'popular_post':popular_post, 'category':category}
    return render(request, 'app/blogpost.html',context)


def BlogDetail(request, slug):
    blog = Post.objects.get(slug=slug)
    popular_post = Post.objects.filter(Section='Popular', Status=1).order_by('-id')[0:4]
    hashtag = Tag.objects.filter(Post=blog)
    category = Category.objects.all()
    context = {'blog':blog, 'hashtag':hashtag, 'popular_post':popular_post, 'category':category}
    return render(request, 'app/blog-single.html', context)


# def CategoryPosts(request, slug):
#     categories = Category.objects.get(slug=slug)
#     context = {' categories': categories}
#     return render(request, 'app/category_posts.html', context)



def CategoryDetail(request):
    category = Category.objects.all()
    popular_post = Post.objects.filter(Section='Popular', Status=1).order_by('-id')[0:4] #this is send in the template because of the get data in the slidebar. 
    context = {'category': category, 'popular_post':popular_post}
    return render(request, 'app/category.html', context)

def About(request):
    blogs = Post.objects.all().order_by('-id')
    popular_post = Post.objects.filter(Section='Popular', Status=1).order_by('-id')[0:4] #this is send in the template because of the get data in the slidebar. 
    category = Category.objects.all() #this is send in the template because of the get data in the slidebar. 
    context = {'blogs':blogs, 'popular_post':popular_post, 'category':category}
    return render(request, 'app/about.html', context)


def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('InputName')
        email = request.POST.get('InputEmail')
        subject = request.POST.get('InputSubject')
        message = request.POST.get('InputMessage')
        try: 
            submit_data = ContactSubmission(name = name, email = email, subject = subject, message = message)
            submit_data.save()
            messages.success(request, "Your messages is submitted successfully. We will notify soon")
            return redirect('/contact')
        except Exception as e:
            messages.success(request, "Something going wrong. Try again")
    return render(request, 'app/contact.html')
