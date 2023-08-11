from django.shortcuts import render
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
class StartpageView(APIView):

    def get(self,request):
        """
        Methode, that gets all articles from database and renders them at startindex.html
        """
        search_terms = request.GET.get('search_terms', '').split(',')
        queryset=Article.objects.all()
        for term in search_terms:
            lowercase_term = term.lower()
            
            queryset = queryset.filter(
                Q(title__icontains=lowercase_term) |
                Q(author__icontains=lowercase_term) |
                Q(text__icontains=lowercase_term)
            )
        serializer=ArticleSerializer(queryset,many=True)
        articles=serializer.data
        return render(request,'start/startindex.html',{'articles':articles})
    
    def post(self,request):
        """
        Methode, that filters the displayed articles for articles including search-params sends back the article container in html to template/js
        """
        search_terms = request.data.get('search_terms', [])
        articles = Article.objects.none()  
    
        for term in search_terms:
            lowercase_term = term.lower()
        
            articles = articles | Article.objects.filter(
                Q(title__icontains=lowercase_term) |
                Q(author__icontains=lowercase_term) |
                Q(text__icontains=lowercase_term)
            )
    
        serializer=ArticleSerializer(articles,many=True)
        articles=serializer.data
        rendered_template = render_to_string('start/filtered_articles.html', {'articles': articles})

        
        return JsonResponse(rendered_template, safe=False,)
        
    
    
class AddView(APIView):
    def get(self,request):
        """
        Render add-template, to add an article
        """
        return render(request,'add/addindex.html')
    
    def post(self,request):
        """
        New article, which is posted from template, is saved. Response:Status 201 to frontend
        """
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            new_article = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class LegalView(APIView):
    def get(self,request):
        """
        Render legal-template, to see legalnotice
        """
        return render(request,'legalnotice/legalindex.html')