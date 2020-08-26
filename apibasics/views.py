from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Article
from .serializer import ArticleSerializer
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET', 'POST'])
class ArticleList(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        articles=Article.objects.all()
        serializer= ArticleSerializer(articles, many=True)
        return Response(serializer.data) # because of the decorator, we dont need any http objects/functions
        #we're no longer explicitly tying our requests or responses to json, other formats are welcome
    def post(self, request, format=None):    
        serializer= ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #we're returning response objects with data, but allowing REST framework to render the response into the correct content type for us
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
class Articledetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        article= self.get_object(pk=pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data) 
    def put(self, request, pk, format=None):
        article= self.get_object(pk=pk)
        serializer=ArticleSerializer(article, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        article= self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)           

