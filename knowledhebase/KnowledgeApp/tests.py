from django.test import TestCase
from rest_framework.test import APIClient
from .models import Article
from rest_framework import status
import json
import html
from django.views.decorators.csrf import csrf_exempt

# Create your tests here.
class StartpageTests(TestCase):
    """
    Tests for get articles request startpage and search for author (included and not included)
    """
    def setup(self):
        self.client=APIClient()
        self.article=Article.objects.create(
            author="testauthor",
            title="testtitel",
            text="testtext")
        self.article.save()
        self.article2=Article.objects.create(
            author="Karl",
            title="Muster",
            text="muster")
        self.article.save()
        
    def test_get_Articles(self):
        response=self.client.get('/startpage/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_test(self):
        self.setup()
        data='test'
        response=self.client.get('/startpage/?search_terms='+data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        articles_count = len(response.context['articles'])
        self.assertTrue(articles_count > 0)


    def test_wrong_search_test(self):
        self.setup()
        data='rufus'
        response=self.client.get('/startpage/?search_terms='+data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        articles_count = len(response.context['articles'])
        self.assertTrue(articles_count == 0)
    
    """
    def test_search_test(self):
        self.setup()
        array=['tes',]
        data={'search_terms':array}
        response=self.client.post('/startpage/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        encoded_html=response.content.decode('utf-8')
        decoded_html = html.unescape(encoded_html)
        self.assertIn('testauthor', decoded_html)

    def test_search_wrong(self):
        self.setup()
        array=['tes',]
        data={'search_terms':array}
        response=self.client.post('/startpage/',data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        encoded_html=response.content.decode('utf-8')
        decoded_html = html.unescape(encoded_html)
        self.assertNotIn('Karl', decoded_html)
    """

class AddPageTests(TestCase):
    """
    Tests for rendering add-page and creating new article (with valid and invalid data)
    """
    def setup(self):
            self.client=APIClient()
            

    def test_add_article(self):
            self.setup()
            data={
                'author':'testauthor',
                'title':'testtitle',
                'text':'testtext'
            }
            response=self.client.post('/add/',data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_article_with_invalid_data(self):
        self.setup()
        data={
            'author':'testauthor',
            'title':'testtitle'}
        response=self.client.post('/add/',data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
         

    def test_get_addpage(self):
         self.setup()
         response=self.client.get('/add/')
         self.assertEqual(response.status_code,status.HTTP_200_OK)


        
        
       