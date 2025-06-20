from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from . models import Movies

from .serializers import MoviesSerializer

# Create your views here.

class MoviesListCreateView(APIView):

    serializer_class = MoviesSerializer

    def get (self,request,*args,**kwargs):

        movies = Movies.objects.all()

        serializer = self.serializer_class(movies, many=True)

        return Response(data = serializer.data, status=200)
    
    def post (self,request,*args,**kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(data={msg := "Movie created successfully"}, status=201)

        return Response(data=serializer.errors, status=400)
    
    def put (self,request,*args,**kwargs):
        movie_id = kwargs.get('id')

        try:
            movie = Movies.objects.get(id=movie_id)
        except Movies.DoesNotExist:
            return Response(data={msg := "Movie not found"}, status=404)

        serializer = self.serializer_class(movie, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data={msg := "Movie updated successfully"}, status=200)

        return Response(data=serializer.errors, status=400)
    
    def delete (self,request,*args,**kwargs):
        movie_id = kwargs.get('id')

        try:
            movie = Movies.objects.get(id=movie_id)
        except Movies.DoesNotExist:
            return Response(data={msg := "Movie not found"}, status=404)

        movie.delete()

        return Response(data={msg := "Movie deleted successfully"}, status=204)
    
    