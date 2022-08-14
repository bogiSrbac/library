from rest_framework import serializers
from .models import LibraryUser, Book, AuthorBook, BorrowBook
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework.validators import UniqueTogetherValidator
import datetime
from rest_framework.settings import api_settings

class CreateAuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, allow_blank=True, max_length=150, allow_null=True)
    last_name = serializers.CharField(required=False, allow_blank=True, max_length=150, allow_null=True)
    year_of_birth = serializers.DateField()

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=AuthorBook.objects.all(),
                fields= ['first_name', 'last_name', 'year_of_birth']
            )
        ]

    def create(self, validated_data):
        print('in create part')
        return AuthorBook.objects.create(**validated_data)


class CreateLibraryUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phone_number',
                  'date_joined', 'membership_duration', 'start_date', 'end_date', 'fee', 'duration', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validate_password(validated_data['password']) == None:
            password = make_password(validated_data['password'])

            user = LibraryUser.objects.create(
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                phone_number=validated_data['phone_number'],
                date_joined=timezone.now(),
                membership_duration=validated_data['membership_duration'],
                fee=validated_data['fee'],
                password=password,
            )
            return user


class LibraryUserSerializer(serializers.ModelSerializer):
    end_date = serializers.ReadOnlyField()
    duration = serializers.ReadOnlyField()
    active_member = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    class Meta:
        model = LibraryUser
        fields = ['id', 'first_name', 'last_name', 'phone_number',
                  'date_joined', 'membership_duration', 'start_date', 'end_date', 'fee', 'duration', 'active_member', 'email']


class AuthorBookSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()
    class Meta:
        model = AuthorBook
        fields = ['id', "first_name", "last_name", "year_of_birth", 'books']

    def get_books(self, obj):
        products = Book.objects.filter(author=obj)  # will return product query set associate with this category
        response = BookSerializer(products, many=True).data
        print(obj)
        return response


class BookSerializer(serializers.ModelSerializer):
    author2 = AuthorBookSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'book_name', 'release_year', 'pages', 'ganres', 'author', 'quantity', 'author2']


class BorrowBookSerilaizer(serializers.ModelSerializer):
    # lend_date = serializers.ReadOnlyField()
    # return_date = serializers.ReadOnlyField()
    duration = serializers.ReadOnlyField()
    days_left = serializers.ReadOnlyField()
    class Meta:
        model = BorrowBook
        fields = ['id', 'borrower', 'book', 'lend_date', 'return_date', 'duration', 'days_left', 'returned']

    def validate(self, attrs):
        queryset = BorrowBook.objects.filter(borrower=attrs['borrower'], returned=False)
        querysetBook = BorrowBook.objects.filter(borrower=attrs['borrower'], borrower__borrowbook__book=attrs['book'])
        queryset = len(list(queryset))
        if queryset >= 3 and self.context.get('request').method != "PUT":
            raise serializers.ValidationError("On your account you already have 3 book borrowed")
        elif querysetBook and self.context.get('request').method != "PUT":
            raise serializers.ValidationError(f"You already borrowed book {attrs['book']}")
        return attrs






