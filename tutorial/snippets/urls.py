from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    # Ex: /snippets/5
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    # Ex: /users/3
    path('users/<int:pk>/', views.UserDetail.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)