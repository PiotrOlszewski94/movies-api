from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        title = attrs.get('Title')
        year = attrs.get('Year')
        # Validate if movie exists in the database
        if Movie.objects.filter(Title=title.title(), Year=year).exists():
            raise serializers.ValidationError('Movie already exists in the database.')
        return attrs

    class Meta:
        model = Movie
        fields = '__all__'
