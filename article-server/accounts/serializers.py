from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie
from community.models import Review


class CustomRegisterSerializer(RegisterSerializer):
    # 추가 설정 필드: nickname
    nickname = serializers.CharField(max_length=30)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        return data

class ProfileSerializer(serializers.ModelSerializer):
    class ProfileMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk', 'poster_path', 'title', 'vote_average',)


    class ProfileReviewSerializer(serializers.ModelSerializer):
        # class UserSerializer(serializers.ModelSerializer):
        #     class Meta:
        #         model = get_user_model()
        #         fields = ('pk', 'username', ) # 'nickname'

        # like_users = UserSerializer(read_only=True, many=True)

        class Meta:
            model = Review
            fields = ('pk', 'rate', 'movie', 'title', 'content',) #  'like_users'

    my_movies = ProfileMovieSerializer(many=True, read_only=True)
    reviews = ProfileReviewSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'my_movies', 'reviews', ) # 'nickname',



class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)