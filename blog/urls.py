from django.urls import path, include

from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("feed/", feed, name="feed"),
    path("new/", create_post, name="create_post"),
    path("post/<uuid:post_id>/", post_detail, name="post_detail"),
]
