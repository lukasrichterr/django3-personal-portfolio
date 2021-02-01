from django.urls import path
from . import views

app_name = 'blog'

# post_id ist automatisch die erste Variable, die an detail() übergeben wird

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:post_id>/', views.detail, name='detail'),
]
