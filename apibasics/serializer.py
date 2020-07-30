from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    class Meta:
        model=Article
        fields=['title', 'author']
    # title= serializers.CharField(max_length=100)
    # author= serializers.CharField(max_length=100)
    # created=serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Article.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance  