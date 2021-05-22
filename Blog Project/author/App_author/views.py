from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView
from App_author.models import Blog, Comment
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
import uuid
# Create your views here.

class CreatBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content',)
    template_name = 'App_author\create_blog.html'


    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace("", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))


class Bloglist(ListView):
    context_object_name = 'blog'
    model = Blog
    template_name = 'App_author/blog_list.html'
    queryset = Blog.objects.order_by('-publish_date')


@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()


    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('App_author:blog_details', kwargs={'slug':slug}))
    return render(request, 'App_author/blog_details.html', context={'blog':blog, 'comment_form':comment_form})


class Myblog(LoginRequiredMixin, TemplateView):
    template_name = 'App_author/my_blog.html'


class updateblog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content',)
    template_name = 'App_author/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_author:blog_details', kwargs={'slug':self.object.slug})
