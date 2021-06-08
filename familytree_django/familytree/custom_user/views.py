from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import custom_user_model
from .serializers import UserSerializer

# Create your views here.
class UsersList(APIView):
    def get(self, request, format=None):
        users = custom_user_model.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserProfile(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({
                'id': 0,
                'username': 'Anonymous',
                'email': 'Not found',
                'name': 'Not found',
                'staff': False
            })
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'name': user.name,
            'staff': user.is_staff
        })