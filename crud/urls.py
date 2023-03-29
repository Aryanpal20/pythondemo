from django.urls import path

from .views import ItemPost

urlpatterns = [
    path("create/",ItemPost.as_view()),
    path("get_all/", ItemPost.as_view()),
    path("update/<int:pk>/", ItemPost.as_view()),
    path("delete/<int:pk>/", ItemPost.as_view())
]