from django import forms
from posts.models import Poss

class PostForms(forms.ModelForm):

	class Meta:
		model = Poss
		fields = ('user', 'profile', 'title', 'photo')