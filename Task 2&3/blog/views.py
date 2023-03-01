

# def post_list(request):
#     search_query = request.GET.get('serch_que')

#     if search_query:
#         posts = Post.objects.filter(title__icontains=search_query) 
#     else:
#         posts = Post.objects.all()

#     posts = posts.order_by('-pub_date')
#     return render(request, 'blog\post_list.html', {'posts': posts})

from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    search_query = request.GET.get('serch_que')
    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(author__name__icontains=search_query)
    
    
    return render(request, 'blog/post_list.html', {'posts': posts})
