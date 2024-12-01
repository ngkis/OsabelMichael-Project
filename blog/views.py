from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Announcement, Feedback, Category

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'blog/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'blog/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'blog/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class HomePageView(ListView):
    model = Post
    template_name = 'blog/homepage.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-date_created')[:5]

class PostListView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/viewpost.html'

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'blog/announcement.html'
    context_object_name = 'announcements'


class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['message']
    template_name = 'blog/feedback.html'
    success_url = '/'
