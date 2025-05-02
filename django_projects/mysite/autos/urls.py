from django.urls import path

from . import views

app_name = "autos"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("make/list", views.Make_List.as_view(), name="make_list"),
    path("make/create", views.Make_Create.as_view(), name="make_create"),
    path("make/update", views.Make_Update.as_view(), name="make_update"),
    path("make/delete", views.Make_Delete.as_view(), name="make_delete"),
    path("autos/list", views.Autos_List.as_view(), name="autos_list"),
    path("autos/create", views.Autos_Create.as_view(), name="autos_create"),
    path("autos/update", views.Autos_Update.as_view(), name="autos_update"),
    path("autos/delete", views.Autos_Delete.as_view(), name="autos_delete"),
]
