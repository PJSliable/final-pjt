from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404


from movies.models import Genre, Movie
from .models import Review, Comment
from .serializers import ReviewSerializer, CommentSerializer

def review_list():
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
@api_view(['POST'])
def review_create(request, moviePk):
    user = request.user
    movie = get_object_or_404(Movie, pk=moviePk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST','DELETE'])
def review_detail_like_or_update_delete(request, moviePk, reviewPk):
    movie = get_object_or_404(Movie, pk=moviePk)
    review = get_object_or_404(Review, pk=reviewPk)
    user = request.user 

    def review_detail():
        pass

    def like_review():
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(user)
        else:
            review.like_users.add(user)
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_review():
        pass

    def delete_review():
        if user == review.user:
            review.delete()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'GET':
        return review_detail()
    elif request.method == 'POST':
        return like_review()
    elif request.method == 'PATCH':
        return update_review()
    elif request.method == 'DELETE':
        return delete_review()


@api_view(['POST'])
def create_comment(request, article_pk):
    user = request.user
    review = get_object_or_404(Review, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(review=review, user=user)
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    review = get_object_or_404(Review, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = review.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        return delete_comment()