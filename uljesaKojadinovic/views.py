from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import LibraryUser, Book, AuthorBook, BorrowBook
from .serializers import (LibraryUserSerializer, BookSerializer, CreateAuthorSerializer,
                          AuthorBookSerializer, BorrowBookSerilaizer, CreateLibraryUserSerializer)
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth import authenticate, logout
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, action
from .tasks import create_new_author
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# @receiver(post_save, sender=LibraryUser)

def index(request):
    return render(request, 'uljesaKojadinovic/index.html')

def room(request, room_name):
    return render(request, 'uljesaKojadinovic/room.html', {
        'room_name': room_name
    })


def left_days(sender, instance, **kwargs):
    print(kwargs)
    # if not created:
    #     for item in iter(kwargs.get('update_fields')):
    #         if item == 'field_name' and instance.field_name == "some_value":
    #             print(item)
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        'chat_momir',
        {
            'type': 'chat.message',
            'message': 'test message'
        }
    )
    print(instance.fee)
    print('Doslo je do promjene u bazi podataka')
    return HttpResponse('<p>Done</p>')
# pre_save.connect(left_days, sender=LibraryUser)
post_save.connect(left_days, sender=LibraryUser)
class ListUserAPIView(generics.ListAPIView):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #      # serializer.save(email=self.request.user)
    #      serializer.save()

class LibraryUserDetailUpdateDestoyAPIViwe(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer
    permission_classes = [permissions.IsAdminUser]


class AuthorBookListAPIView(generics.ListAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AuthorBookCreateAPIView(generics.ListCreateAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class AuthorBookDetailUpdateDestoyAPIViwe(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorBook.objects.all()
    serializer_class = AuthorBookSerializer
    permission_classes = [permissions.IsAdminUser]

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class BookCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class BookDetailUpdateDestoyAPIViwe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]

class BorrowerBookListAPIView(generics.ListAPIView):
    queryset = BorrowBook.objects.all()
    serializer_class = BorrowBookSerilaizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BorrowerBookListCreateAPIView(generics.ListCreateAPIView):
    queryset = BorrowBook.objects.all()
    serializer_class = BorrowBookSerilaizer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class BorrowerBookDetailUpdateDestoyAPIViwe(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowBook.objects.all()
    serializer_class = BorrowBookSerilaizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request, 'login request')
        email = request.data['email']
        password = request.data['password']

        if not email or not password:

            return Response({'error': 'Please, fill all filds'}, status=status.HTTP_400_BAD_REQUEST)

        check_email = LibraryUser.objects.filter(email=email).exists()
        if check_email == False:
            return Response({"error": "Email doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)
        if user is not None:
            print('fwfwfwfffwfwfwff')
            login(request, user)
            return Response({"message": "You logged in!"}, status=status.HTTP_400_BAD_REQUEST)






class SignupAPIView(APIView):
    permission_classes = []

    def post(self, request):
        password = request.POST.get('password', None)
        confirm_password = request.POST.get('confirm_password', None)
        if password == confirm_password:
            serializer = CreateLibraryUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'Password fields didn not match.'})

@api_view(["GET", "POST"])
def login(request):
    if request.method == 'POST':
        print('kjfkwebgfkwefiwekfgiwgifwgfigwgf')
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            return Response({'Message': "Success!"}, status=status.HTTP_200_OK)
        else:
            return Response({"Message": "Invalid"}, status=status.HTTP_400_BAD_REQUEST)
    # if request.method == 'POST':
    #     print('kfdkffkfkfkfkf')
    #     data = JSONParser().parse(request)
    #     user = authenticate(request, username=data['username'], password=data['password'])
    #     if user is None:
    #         return JsonResponse({"error": "Could not login. Please check username and password!"}, status=201)
    #     else:
    #         return JsonResponse({"success":"You are loged in"}, status=201)
    # print('eiugfww')
    return JsonResponse({"success":"You are loged in"}, status=201)

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def logout(request):
    logout(request)
    return Response('User Logged out successfully', status=status.HTTP_410_GONE)


@api_view(["GET", "POST"])
@permission_classes([])
def create_author(request):
    if request.method == "POST":

        serializer = CreateAuthorSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)

            create_new_author.delay(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse({'message':'Author successfully created'})
from django.core.mail import send_mail
@csrf_exempt
def frak(request):
    hdhdd = LibraryUser.objects.get(email='bogosavacm@yahoo.com')
    send_mail('test poruka', 'Samo provjera', 'realauto.polovniautomobili@gmail.com', ['realauto.polovniautomobili@gmail.com'], fail_silently=False)
    if request.method == "GET":
        query = BorrowBook.objects.filter(returned=False)
        print(request.user)
        for q in query:
            print(q.borrower.email)
        return Response({'message':"jkdjejkw"})
    return Http404

