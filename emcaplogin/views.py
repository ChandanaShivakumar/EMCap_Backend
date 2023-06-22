from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from emcaplogin.serializers import RegisterSerializer, ForgotPasswordSerializer,UserPasswordResetSerializer, ChangePasswordSerializer,ResetPasswordSerializer
from emcaplogin.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            response_data = {
                "emp_id": user.emp_id,
                "email": user.email,
                "name": user.name,
                "role_id": user.role_id,
                "message": "Registration Successful",
                "token": token
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            token = get_tokens_for_user(user)
            user_data = {
                "id": user.emp_id,
                "email": user.email,
                "name": user.name,
                "role_id": user.role_id,
                
                
            }
            return Response({"token": token,"user": user_data,"message": "Login Success"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Successfully logged out."})
    
class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(email=serializer.validated_data['email'])
            token=  serializer.create(serializer.validated_data)
            return Response({'message': 'Password reset email sent.', 'token': token})
        return Response(serializer.errors, status=400)


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response("Password changed successfully.", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResetPasswordView(APIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = self.get_user_from_token(request)
            if user:
                serializer.save(user)
                return Response({'message': 'Password reset successful.'})
            else:
                return Response({'message': 'Invalid token.'}, status=400)
        return Response(serializer.errors, status=400)

    def get_user_from_token(self, request):
        # Simplified implementation of retrieving user from token
        access_token = request.META.get('HTTP_AUTHORIZATION')
        refresh_token = request.data.get('refresh_token')

        User = get_user_model()
        user = None
        if access_token:
            user = User.objects.filter(access_token=access_token).first()
        elif refresh_token:
            user = User.objects.filter(refresh_token=refresh_token).first()

        return user
    

class UserPasswordResetView(APIView):
#   renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)