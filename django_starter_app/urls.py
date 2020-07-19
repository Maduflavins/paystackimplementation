from django.urls import path, include
from django_starter_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('programmers', views.ProgrammerView)
router.register('paradigms', views.ParadigmView)

urlpatterns = [
	path('', include(router.urls)),
	path('buy/', views.purchase, name='purchase'),
]
