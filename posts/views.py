#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

posts = [
	{
		"name": "Joel Cedeño",
		"user": "Jioska",
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"picture": "https://i.picsum.photos/id/1036/200/200.jpg?hmac=Yb5E0WTltIYlUDPDqT-d0Llaaq0mJnwiCUtxx8RrtVE",
	},
	{
		"name": "Aksoij",
		"user": "Idontknow",
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"picture": "https://i.picsum.photos/id/989/200/200.jpg?hmac=YmaagsSArKDGDSeyRJ9aYRxKM6KdP49ZGYtyhLHlCcY",
	},
	{
		"name": "Karla",
		"user": "Karla007",
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"picture": "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U",
	}
]

def list_pos(request):
	"""lista de posts existentes"""
	content = []
	for post in posts:
		content.append("""
			<p><strong>{name}</strong></p>
			<p><small>{user} - <i>{timestamp}</i></small></p>
			<figure><img src="{picture}"/></figure>
		""".format(**post))
	return HttpResponse("<br>".join(content))