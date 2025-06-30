from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, home, add_recipe, edit_recipe, delete_recipe

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_recipe, name='add_recipe'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
    path('delete/<int:recipe_id>/', delete_recipe, name='delete_recipe'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
]

path('accounts/', include('django.contrib.auth.urls')),

