

def importar_classe():
    """
    from django.contrib.auth.models import User
    """

def instanciar_objeto():
    """
    * Uso || class based view -> get_context_data 
    * Uso || function based view -> context = {} 

    new_user = User.objects.create_user(
        first_name="Lucas",
        last_name="Farias",
        username="Luuk",
        email="luuk@gmail.com",
        password="blablabla"
    )

    new_user.save()
    """

def urls_py():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexView.as_view(), name='index'),
    ]
    """

def views_py():
    """
    from django.views.generic import TemplateView
    
    class IndexView(TemplateView):
        template_name = 'index.html'

        def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data(**kwargs)
            return context
    """
