from django.contrib import auth , messages
from django.db.models import Q, query , Count
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.shortcuts import render , get_object_or_404 , redirect , reverse
from .forms import CommentForm , PostForm , ContactForm
from .models import Post , Author , PostView
from marketing.models import Signup

# Create your views here.

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def get_category_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset' : queryset,
    }
    return render(request , 'search_results.html' , context)

def index(request):
    featured = Post.objects.filter(featured=True).order_by('-timestamp')
    latest = Post.objects.order_by('-timestamp')[0:3]
    backg = Post.objects.order_by('-timestamp')[0:1]
    gallery = Post.objects.order_by('-timestamp')[0:4]

    if request.method == 'POST':
        email = request.POST['email']
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'object_list' : featured ,
        'latest' : latest,
        'backg' : backg ,
        'gallery' : gallery,
    }
    return render(request , 'index.html' , context)

def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(post_list , 4)
    page_request_var = 'page'
    page  = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)    

    context = {
        'queryset' : paginated_queryset,
        'page_request_var' : page_request_var,
        'most_recent' : most_recent,
        'category_count' : category_count,
    }
    return render(request , 'blog.html' , context)

def post(request , id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post = get_object_or_404(Post , id=id)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user , post=post)

    form = CommentForm(request.POST or None , request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail" , kwargs={
                'id' : post.id
            }))
            
    context = {
        'form' : form,
        'post' : post,
        'most_recent' : most_recent,
        'category_count' : category_count,
    }
    return render(request , 'post.html' , context)

def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None , request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = get_author(request.user)
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id' : form.instance.id,
            }))
    context = {
        'title' : title,
        'form' : form
    }
    return render(request , 'post_create.html' , context)

def post_update(request , id):
    title = 'Update'
    post = get_object_or_404(Post , id=id)
    form = PostForm(request.POST or None , request.FILES or None , instance=post)
    author = get_author(request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id' : form.instance.id,
            }))
    context = {
        'title' : title,
        'form' : form
    }
    return render(request , 'post_create.html' , context)

def post_delete(request , id):
    post = get_object_or_404(Post , id=id)
    post.delete()
    return redirect(reverse("post-list"))


def contact(request):
    form = ContactForm(request.POST or None , request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request , "Thank You for Contacting Us!")
            return redirect(reverse("home"))

    context ={
        'form' : form
    }    
    return render(request , 'contact.html' , context)