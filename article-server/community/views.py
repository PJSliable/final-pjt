from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.forms.models import model_to_dict

from movies.models import Genre, Movie
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer


@api_view(['GET','POST'])
def review_list_or_create(request):
    def review_list():
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_review():
        movie_pk = request.data.get('movie')
        user = request.user
        Newdata = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'rate': request.data.get('rate'),
            'movie': movie_pk
        }
        serializer = ReviewSerializer(data=Newdata)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return review_list()
    elif request.method == 'POST':
        return create_review()


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def review_detail_like_or_update_delete(request, reviewPk):
    review = get_object_or_404(Review, pk=reviewPk)
    if request.user:
        user = request.user

    def review_detail():
        serializer = ReviewSerializer(review)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def like_review():
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(user)
        else:
            review.like_users.add(user)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_review():
        movie_pk = request.data.get('movie')
        user = request.user
        Newdata = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'rate': request.data.get('rate'),
            'movie': movie_pk
        }
        serializer = ReviewSerializer(instance=review, data=Newdata)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete_review():
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'POST':
        return like_review()
    elif request.method == 'PATCH':
        if user == review.user:
            return update_review()
    elif request.method == 'DELETE':
        if user == review.user:
            return delete_review()


@api_view(['POST'])
def create_comment(request):
    review_pk = request.data.get('reviewPk')
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data.get('comment'))

    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE','PATCH'])
def comment_update_or_delete(request, commentPk):
    review_pk = request.data.get('reviewPk') 
    comment = get_object_or_404(Comment, pk=commentPk)
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user

    def update_comment():
        serializer = CommentSerializer(instance=comment, data=request.data.get('comment'))
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=user)
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def comment_delete():
        if request.user == comment.user:
            comment.delete()
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    if request.method == 'PATCH':
        if user == review.user:
            return update_comment()
    elif request.method == 'DELETE':
        if user == review.user:
            return comment_delete()