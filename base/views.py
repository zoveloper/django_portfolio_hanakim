from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import PostForm

from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.filter(active=True)[0:20]

    context = {'posts':posts}
    return render(request,'base/index.html',context)

def posts(request, pk):
    posts = Post.objects.filter(active=true)

    context = {'posts':posts}
    return render(request,'base/posts.html', context)

def post(request, pk):
    post=Post.objects.get(id=pk)

    context = {'post':post}
    return render(request,'base/post.html', context)

def profile(request):
    return render(request,'base/profile.html')

#CRUD VIEWS
@login_required(login_url="home")
def createPost(request):
    form = PostForm

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form':form}
    return render(request,'base/post_form.html', context)

@login_required(login_url="home")
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form':form}
    return render(request,'base/post_form.html', context)

@login_required(login_url="home")
def deletePost(request,pk):
    post =Post.objects.get(id=pk)

    if request.method =='POST':
        post.delete()
        return redirect('home')
    context = {'item':post}
    return render(request,'base/delete.html',context)


def contact(request):
    return render(request,'base/contact.html')

def sendEmail(request):

	if request.method == 'POST':
        
		template = render_to_string('base/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})
            
		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['junsang1113@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request,'base/index.html' )