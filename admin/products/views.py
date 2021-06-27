# from django.shortcuts import render
from rest_framework import viewsets

# tutorial-learning, this is looking like where you defined how the application interfaces with the db

class ProductViewSet(viewsets.ViewSet):
  def list(self, request): # /api/products
    pass

  def create(self, request): # /api/products
    pass

  def retrieve(self, request, pk=None): # .api/products/<str:id>
    pass
  def update(self, request, pk=None): # .api/products/<str:id>
    pass
  def delete(self, request, pk=None): # .api/products/<str:id>
    pass