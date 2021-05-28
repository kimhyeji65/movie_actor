#from django.shortcuts import render
import json
from django.views import View
from django.http import JsonResponse
from .models import Actor, Movie
# Create your views here.

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()

        result = []
        
        
        for actor in actors:
            movies = actor.movie_set.all()

            movies_list = []
            for movie in movies:
                movie_info = {
                    'title':movie.title,
                }
                movies_list.append(movie_info)

            actor_info = {
                'last_name':actor.last_name,
                'first_name':actor.first_name,      
                'movie' : movies_list
            }
            result.append(actor_info)

        return JsonResponse({'result':result}, status=200)

   
        

        

    def post(self, request):   
        try:
            data = json.loads(request.body)
            
            Actor.objects.create(first_name=data['first_name'],last_name=data['last_name'], date_of_birth=data['date_of_birth'])
            
        
            return JsonResponse({'message': 'SUCCESS'}, status=201)

   
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)


class MovieView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            #actor=Actor.objects.get(name=data)
            Movie.objects.create(title=data['title'] ,release_date =data['release_date'] ,running_time =data['running_time'])

            return JsonResponse({'message': 'SUCCESS'}, status=201)

    
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status=400)
        except Actor.DoesNotExist:
            return JsonResponse({'message': 'USER DOES NOT EXIST'}, status= 404)



    def get(self, request):

        movies = Movie.objects.all()
        result = []
        
        
        for movie in movies:
            actors = actor.objects.all()

            actors_list = []
            for actor in actors:
                actor_info ={
                    'actor_name' : movie.actor.last_name

                
                }


            actors_list.append(actor_info)

            movie_info = {
                'title':movie.title ,
                'running_time':movie.running_time,      
                'name' : actors_list
            }
        result.append(movie_info)

        return JsonResponse({'result':result}, status=200)
