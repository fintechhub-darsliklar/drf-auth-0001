from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.users.seralizers.user_auth import UserSeralizer
from apps.users.models import User


class LoginView(APIView):

    def post(self, request):

        return Response({}, status=status.HTTP_200_OK)