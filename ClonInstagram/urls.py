#url
from django.urls import path

from ClonInstagram import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path("sorted/", views.sorted_numers),
    path("saludo/<str:name>/<int:age>", views.hi),
    path("hola/<str:nombre>/<int:edad>",views.saludo)
]
