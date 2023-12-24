from django.urls import path
from .views import GetUploadUrl, PhotoDetail, VideoDetail

urlpatterns = [
    path("photos/get-url", GetUploadUrl.as_view()),
    path("photos/<int:pk>", PhotoDetail.as_view()),
    path("videos/<int:pk>", VideoDetail.as_view()),
]
