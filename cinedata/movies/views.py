from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from . models import Movies

# Create your views here.

class MoviesListView(APIView):

    def get (self,request,args,*kwargs):

        movies = Movies.objects.all()

        


        return Response(status=200)