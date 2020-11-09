#url
from django.urls import path

from ClonInstagram import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world/', local_views.hello_world),
    path("sorted/", local_views.sorted_numers),
    path("saludo/<str:name>/<int:age>", local_views.hi),
    path("hola/<str:nombre>/<int:edad>", local_views.saludo),

    path("posts/", posts_views.list_pos),
]
