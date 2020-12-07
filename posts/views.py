from django.contrib.auth.decorators import login_required
from posts.forms import PostForms
from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from datetime import datetime
from posts.models import Poss
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Poss
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'

@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForms(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('posts:feed')
	else:
		form = PostForms()
		
	return render(
			request=request,
			template_name='posts/new.html',
			context={
				'form':form,
				'user':request.user,
				'profile':request.user.profile
			}
		)