from django.contrib.auth.decorators import login_required
from posts.forms import PostForms
from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from datetime import datetime
from posts.models import Poss


@login_required
def list_pos(request):
	"""lista de posts existentes"""
	posts = Poss.objects.all().order_by('-created')
	return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
	if request.method == 'POST':
		form = PostForms(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('feed')
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