#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

posts = [
	{
		"title": " Montaña nevada",
		"user": {
			"name": "El jioska",
			"picture": "https://i.picsum.photos/id/1036/200/200.jpg?hmac=Yb5E0WTltIYlUDPDqT-d0Llaaq0mJnwiCUtxx8RrtVE",
		},
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"photo": "https://www.trecebits.com/wp-content/uploads/2019/02/Persona-1-445x445.jpg",
	},
	{
		"title": "Nevada",
		"user": {
			"name": "I dont know",
			"picture": "https://i.picsum.photos/id/989/200/200.jpg?hmac=YmaagsSArKDGDSeyRJ9aYRxKM6KdP49ZGYtyhLHlCcY",
		},
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"photo": "https://cdnb.20m.es/sites/112/2019/04/cara6-620x618.jpg",
	},
	{
		"title": "Perro bonito",
		"user": {
			"name": "Karla007",
			"picture": "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U",
		},
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"photo": "https://pbs.twimg.com/media/DzVBSvnVYAA_txX?format=jpg&name=small",
	}
]

def list_pos(request):
	"""lista de posts existentes"""
	return render(request, "feed.html", {"posts": posts})