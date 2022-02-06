from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


from .models import Movie
from .serializers import MovieSerializer
from .services import get_movie
from .exceptions import ServiceUnavailable


# Create your views here.

class MovieList(APIView):
    """
    List all movies using external api.
    """
    def get(self, request, format=None):
        title = request.query_params.get('t')
        year = request.query_params.get('y')
        try:
            movie = get_movie(title, year)
        except:
            raise ServiceUnavailable()
        return Response(movie)


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned movies to a given title and year,
        by filtering against a `t` and `y` query parameters in the URL.
        """
        queryset = Movie.objects.all()
        title = self.request.query_params.get('t')
        year = self.request.query_params.get('y')

        if title is not None:
            queryset = queryset.filter(Title__icontains=title.title())
        if year is not None and year.isdigit():
            queryset = queryset.filter(Year=year)
        return queryset
