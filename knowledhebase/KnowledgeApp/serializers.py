from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__' 


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=['id','author','text','created_at','title']
    
    def create(self, validated_data): 

        article = Article.objects.create(**validated_data)
       
        return Article
    
    def update(self, instance, validated_data):
        article = instance.article

        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.author=validated_data.get('author', instance.author)
        instance.save()
        return instance