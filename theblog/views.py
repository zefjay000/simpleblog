from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
#from .forms import PostForm
#CAUSES ERROR ABOVE
#BECAUSE YOU CANT HAVE FIELDS AND FORMS
#FROM VIDEO 6 ~ 12 MIN
from django.urls import reverse_lazy


#def home(request):
#    return render(request, "home.html", {})

class HomeView(ListView):
    model= Post
    template_name = "home.html"
    ordering = ["-post_date"]
    #shows latest blog post
    #above

class ArticleDetailView(DetailView):
    model= Post
    template_name ="article_details.html"

class AddPostView(CreateView):
    model= Post
    #form_class= PostForm
    #CAUSES ERROR ABOVE
    template_name= "add_post.html"
    fields = "__all__"
    #fields= ["title", "body"]

class UpdatePostView(UpdateView):
    model= Post
    template_name= "update_post.html"
    fields= ["title", "title_tag",
             "body"]

class DeletePostView(DeleteView):
    model=Post
    template_name= "delete_post.html"
    success_url= reverse_lazy("home")


#any time you create a webpage
# you create a view, url, html template