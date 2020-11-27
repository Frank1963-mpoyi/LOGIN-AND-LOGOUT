from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # act like decorator in function view, Userpassestest only the own can update it own test
from .models import Post
from django.views.generic import (
    
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    
    )




class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts' # to replace the default : object_list
    ordering = ['-date_posted']
    #<app>/<model> <viewtype>.html
    

class PostDetailView(DetailView):
    model = Post
    # convention template //<app>/<model> <viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    
#every post need to have an author we want the author to be the current login user
# but it doesnt know that we have to tell it by overriding form valid method for ceate view
# it allow us to add the author before the form is submitted   
    def form_valid(self, form): # here we override form valid method
        form.instance.author = self.request.user # before you submitt the form take that instance set the author = current login user
        #here is form validation
        return super().form_valid(form) # form_valid(form) just run form valid method on the parent class and pass that form as an argument
# the post was created now we must redirect

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # always put to the left of updateview
    model = Post
    fields = ['title','content']
    def form_valid(self, form): 
        form.instance.author = self.request.user 
        return super().form_valid(form) 
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False
# here only the author of the post can only update because it like someone can edit your twiter
# self.get_object() mean get the post we trying to update
# if self.request.user == post.author: check if the current user is the author of the post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # convention template //<app>/<model> <viewtype>.html
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True 
        return False
    