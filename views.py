from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer,LoginSerailizer
from rest_framework.views import APIView
# Create your views here.

    
class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerailizer(data=request.data)
        serializer.is_valid(raise_exception = True)
        return Response({'success':True})
    
class RegView(APIView):
    def post(self,request):
        serializer = LoginSerailizer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        user.set_password(serializer.data['password'])
        user.save()
        return Response({'success':True})
