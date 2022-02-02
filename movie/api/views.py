from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from movie.models import Movie
from movie.api.serializers import MovieSerializer

@api_view(['GET', 'POST'])
def movie_list_create_api_view(request):
    
    if request.method == 'GET':
        movies = Movie.objects.filter(is_active=True) 
        serializer = MovieSerializer(movies, many=True) 

        return Response({
        "header": {
        "isSuccess": True,
        "statusCode": 200,
        # if isSuccess return False; 
        # "message": "Success"
        },
        "body": {"data":serializer.data}
        }, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, pk):
    try:
        movie_instance = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({
        "header": {
        "isSuccess": True,
        "statusCode": 404,
        "message":  f'There is no movie with id: {pk}.'
        },
        "body": {"data":None}
        }, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = MovieSerializer(movie_instance) 
        return Response({
        "header": {
        "isSuccess": True,
        "statusCode": 200,
        "message":  'Success.'
        },
        "body": {"data":serializer.data}
        }, status=status.HTTP_200_OK)


    elif request.method == 'PUT':
        serializer = MovieSerializer(movie_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
        "header": {
        "isSuccess": True,
        "statusCode": 200,
        "message":  'Update successfully.'
        },
        "body": {"data":serializer.data}
        }, status=status.HTTP_200_OK)
        
        return  Response({
        "header": {
        "isSuccess": True,
        "statusCode": 404,
        "message":  'Can\'t change successfully.'
        },
        "body": {"data":None}
        }, status=status.HTTP_404_NOT_FOUND)


    elif request.method == 'DELETE':
        movie_instance.delete()
        return Response({
        "header": {
        "isSuccess": True,
        "statusCode": 204,
        "message": 'Deleted successfully.'
        },
        "body": {"data":None}
        }, status=status.HTTP_204_NO_CONTENT)
