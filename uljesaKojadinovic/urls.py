from django.urls import path
from .views import (SignupAPIView, login, logout, LoginAPIView, create_author, frak, index, room,
                    ListUserAPIView, AuthorBookCreateAPIView, BookListAPIView, BookCreateAPIView,
                    AuthorBookDetailUpdateDestoyAPIViwe, BookDetailUpdateDestoyAPIViwe, BorrowerBookDetailUpdateDestoyAPIViwe,
                    BorrowerBookListCreateAPIView, LibraryUserDetailUpdateDestoyAPIViwe, AuthorBookListAPIView, BorrowerBookListAPIView)
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'uljesaKojadinovic'

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('users/', ListUserAPIView.as_view()),
    path('users/<int:pk>', LibraryUserDetailUpdateDestoyAPIViwe.as_view()),
    path('list-author/', AuthorBookListAPIView.as_view()),
    path('list-create-author/', AuthorBookCreateAPIView.as_view()),
    path('list-create-author/<int:pk>',AuthorBookDetailUpdateDestoyAPIViwe.as_view()),
    path('create-book/', BookCreateAPIView.as_view()),
    path('list-book/', BookListAPIView.as_view()),
    path('list-create-book/<int:pk>', BookDetailUpdateDestoyAPIViwe.as_view()),
    path('list-borrower-book/', BorrowerBookListAPIView.as_view()),
    path('create-borrower-book/', BorrowerBookListCreateAPIView.as_view()),
    path('create-borrower-book/<int:pk>', BorrowerBookDetailUpdateDestoyAPIViwe.as_view()),

    # path('login/', LoginAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', logout),
    path('celery/', create_author),
    # path('chat/<str:room_name>/', frak),
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]

