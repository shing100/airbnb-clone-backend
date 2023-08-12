from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExperienceList.as_view()),
    path("<int:pk>", views.ExperienceDetail.as_view()),
    path("<int:pk>/perks", views.ExperiencePerks.as_view()),
    path("<int:pk>/bookings", views.ExperienceBookings.as_view()),
    path("<int:pk>/reviews", views.ExperienceReviews.as_view()),
    path("<int:pk>/photos", views.ExperiencePhotos.as_view()),
    path("<int:pk>/photos/<int:photo_pk>",
         views.ExperienceThumbnailPhotoSelect.as_view()),
    path("<int:pk>/video", views.ExperienceVideo.as_view()),
    path("perks/", views.PerkList.as_view()),
    path("perks/<int:pk>", views.PerkDetail.as_view()),
]
