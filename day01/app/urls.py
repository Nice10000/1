
from django.urls import path # type: ignore
from . import views

urlpatterns = [
  path('category/', views.categoryview),
  path('unit/', views.unitview),
  path('test/',views.test),

]

