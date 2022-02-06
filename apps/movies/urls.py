from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'favoritemovies', views.MovieViewSet, 'favoritemovies')


urlpatterns = [
    path('', include(router.urls)),
    path('movies/', views.MovieList.as_view())
    
]
