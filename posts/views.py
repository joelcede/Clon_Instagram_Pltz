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
			"picture": "https://i.picsum.photos/id/1027/60/60.jpg?hmac=NKZ0Vfbc1l_5mdJsZpOIQ0iRjvpE24KmZiI5l2ZUiaE",
		},
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"photo": "https://i.picsum.photos/id/1036/800/600.jpg?hmac=UlkhfPDDY0vtyrlU4liFSP9GbaUs-g1OhGteuXA1fUc",
	},
	{
		"title": "Selva Tropical?",
		"user": {
			"name": "I dont know",
			"picture": "https://i.picsum.photos/id/1005/60/60.jpg?hmac=5DMnJ9LV55ZoxPEqtcVAhfi8DWd30Xq_wK9KOII3UVY",
		},
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"photo": "https://i.picsum.photos/id/10/2500/1667.jpg?hmac=J04WWC_ebchx3WwzbM-Z4_KC_LeLBWr5LZMaAkWkF68",
	},
	{
		"title": "Venado",
		"user": {
			"name": "Karla007",
			"picture": "https://i.picsum.photos/id/883/60/60.jpg?hmac=nQLWaBJIpcHUkzfqaWQSTDslkVZHOte_jEuvcb_EMWI",
		},
		"timestamp": datetime.now().strftime("%b %dth %Y - %H:%M hrs"),
		"photo": "https://i.picsum.photos/id/1003/1181/1772.jpg?hmac=oN9fHMXiqe9Zq2RM6XT-RVZkojgPnECWwyEF1RvvTZk",
	}
]

def list_pos(request):
	"""lista de posts existentes"""
	return render(request, "feed.html", {"posts": posts})