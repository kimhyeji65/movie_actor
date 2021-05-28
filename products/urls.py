from django.urls    import path
from .views import ActorView,MovieView

#from .views import ProductListView

urlpatterns = [
   
   path('/actor', ActorView.as_view()),
   path('/movie', MovieView.as_view())

   
]



