from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from room.schema import schema

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
