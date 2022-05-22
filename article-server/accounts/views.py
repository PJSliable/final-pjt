from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProfileSerializer, CustomRegisterSerializer, ChangePasswordSerializer


# change_password 부분
from rest_framework.permissions import IsAuthenticated   
from rest_framework.generics import UpdateAPIView



User = get_user_model()

@api_view(['GET','DELETE'])
def profile_or_delete_account(request, username):
    user = get_object_or_404(User, username=username)

    def profile():
        serializer = ProfileSerializer(user)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_account():
        user_nickname = request.user.nickname
        user.delete()
        return JsonResponse({'message': '{} accounts were deleted successfully!'.format(user_nickname)}, status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        profile()
    elif request.method == 'DELETE':
        if user == request.user:
            delete_account()


@api_view(['POST'])
def update(request):
    serializer = CustomRegisterSerializer(instance=request.user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# 복붙한거라 실행되는지 모르겠음. test 필요
class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }
                return Response(response)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)