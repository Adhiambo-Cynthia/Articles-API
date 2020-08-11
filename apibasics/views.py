from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Article
from .serializer import ArticleSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def articleList(request, format=None):
    if request.method == "GET":
        articles=Article.objects.all()
        serializer= ArticleSerializer(articles, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data) # because of the decorator, we dont need any http objects/functions
    elif request.method=="POST":
        # data= JSONParser().parse(request)
        #we're no longer explicitly tying our requests or responses to json, other formats are welcome
        serializer= ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400) 
        #we're returning response objects with data, but allowing REST framework to render the response into the correct content type for us
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk, format=None):
    try:
        article=Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=ArticleSerializer(article)
        return Response(serializer.data) 
    elif request.method=="PUT":
        # data=JSONParser().parse(request)
        serializer=ArticleSerializer(article, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)           

