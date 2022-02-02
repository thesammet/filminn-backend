from rest_framework import serializers
from movie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']