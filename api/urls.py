from django.urls import path
from .views import VideoStream

urlpatterns = [
    # endpoint da API
    path(
        "video_stream/",
        VideoStream.as_view(),
        name="video_stream",
    ),
]