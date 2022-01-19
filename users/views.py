from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer


class UserInfoView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, *args, **kwargs):
        user = self.request.user.id
        queryset = User.objects.all().filter(id=user)
        serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)
