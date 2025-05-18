from rest_framework.views import APIView
from rest_framework.response import Response

class WelcomeView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the ALX Travel App API!'})
