from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'author':'lokesh',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':'April 20, 2025'
    },
    {
        'author':'rahul',
        'title':'Blog post 2',
        'content':'second post content',
        'date_posted':'April 21, 2025'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'Django blog'})