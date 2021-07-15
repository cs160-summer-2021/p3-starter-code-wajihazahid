from django.urls import path
from . import views

urlpatterns = [
    # path('demo', views.index, name='demo'),
    # path('new_interaction', views.index, name='new_interaction')

    path('demo', views.demo, name='demo'),
    path('index', views.index, name='index'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('home_screen', views.home_screen, name='home_screen'),
    path('timer_screen', views.timer_screen, name='timer_screen'),
    path('timer_screen_update', views.timer_screen_update, name='timer_screen_update'),
    path('template_1', views.template_1, name='template_1'),
    path('template_2', views.template_2, name='template_2')

]
