from rest_framework.test import APITestCase
from rest_framework import status
import json

from drf_registration.utils.users import get_user_model


class MovieViewTestCase(APITestCase):
    """Tests /favoritemovies endpoint
    """

    def setUp(self) -> None:
        self.favorite_movies_url = '/favoritemovies/'
        self.valid_movie = {
            "Title": "The Avengers",
            "Year": "2012",
            "Rated": "PG-13",
            "Released": "04 May 2012",
            "Runtime": "143 min",
            "Genre": "Action, Adventure, Sci-Fi",
            "Director": "Joss Whedon",
            "Writer": "Joss Whedon, Zak Penn",
            "Actors": "Robert Downey Jr., Chris Evans, Scarlett Johansson",
            "Plot": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
            "Language": "English, Russian, Hindi",
            "Country": "United States",
            "Awards": "Nominated for 1 Oscar. 38 wins & 80 nominations total",
            "Poster": "https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
            "Ratings": [
                {
                    "Source": "Internet Movie Database",
                    "Value": "8.0/10"
                },
                {
                    "Source": "Rotten Tomatoes",
                    "Value": "91%"
                },
                {
                    "Source": "Metacritic",
                    "Value": "69/100"
                }
            ],
            "Metascore": "69",
            "imdbRating": "8.0",
            "imdbVotes": "1,333,613",
            "imdbID": "tt0848228",
            "Type": "movie",
            "DVD": "25 Sep 2012",
            "BoxOffice": "$623,357,910",
            "Production": "N/A",
            "Website": "N/A",
            "Response": "True"
        }

        self.user_model = get_user_model()
        self.user = self.user_model.objects.create(
            username='username',
            email='test@example.com',
        )
        self.user.set_password('123456')
        self.user.save()

        self.client.force_authenticate(user=self.user)
        self.client.login(user=self.user)


    def test_create_valid_movie(self):
        response = self.client.post(self.favorite_movies_url, data=self.valid_movie, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_movie(self):
        invalid_movie = {
            'Title': 'Random',
        }
        response = self.client.post(self.favorite_movies_url, data=invalid_movie, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  

    def test_create_already_existed_movie(self):
        _ = self.client.post(self.favorite_movies_url, data=self.valid_movie, format='json')
        response = self.client.post(self.favorite_movies_url, data=self.valid_movie, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_already_existed_movie_letter_size(self):
        _ = self.client.post(self.favorite_movies_url, data=self.valid_movie, format='json')
        response = self.client.post(self.favorite_movies_url, data={
            'Title': 'the aVenGers',
            'Year': '2012',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_car(self):
        response = self.client.post(self.favorite_movies_url, data=self.valid_movie, format='json')
        movie_id = response.data['id']

        response = self.client.delete(self.favorite_movies_url + f'{movie_id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_favorite_movies(self):
        _ = self.client.post(self.favorite_movies_url, data=self.valid_movie, format='json')
        response = self.client.get(self.favorite_movies_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)[0]['Title'], self.valid_movie['Title'])
        self.assertEqual(json.loads(response.content)[0]['Year'], int(self.valid_movie['Year']))
        
    def test_movie_query_params(self):
        _ = self.client.post(self.favorite_movies_url, data=self.valid_movie, format='json')
        _ = self.client.post(self.favorite_movies_url, data={
            'Title': 'Kiler',
            'Year': '1997',
        }, format='json')
        response = self.client.get(self.favorite_movies_url, {'t': 'Kiler'})
        self.assertEqual(len(json.loads(response.content)), 1)
        response = self.client.get(self.favorite_movies_url, {'y': 2012})
        self.assertEqual(len(json.loads(response.content)), 1)