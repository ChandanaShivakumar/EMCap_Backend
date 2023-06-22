from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.test import Client
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from rest_framework import serializers
from django.contrib.auth import get_user_model
from emcaplogin.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.hashers import make_password
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)

    # class Meta:
    #     model = get_user_model()
    #     fields = ['emp_id', 'email', 'name', 'role_id', 'password']

    # def create(self, validated_data):
    #     user = get_user_model().objects.create_user(
    #         emp_id=validated_data['emp_id'],
    #         email=validated_data['email'],
    #         name=validated_data['name'],
    #         role_id=validated_data['role_id'],
    #         password=validated_data['password']
    #     )
    #     return user
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['emp_id', 'email', 'name', 'password', 'password2', 'role_id']
        extra_kwargs={
            'password':{'write_only':True}
            }

        # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
            password = attrs.get('password')
            password2 = attrs.get('password2')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            return attrs

    def create(self, validate_data):
            return User.objects.create_user(**validate_data)
    

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        user = User.objects.get(email=email)

        if user:
            token = generate_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.emp_id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            print('Test')
            link = 'http://localhost:3000/reset/'+uid+'/'+token
            print('Password Reset Link', link)
            # Send the password reset email with the token
            email_subject = 'Reset Your Password'
            email_message = f'Hello {user.name},\n\nClick the link below to reset your password:'+ link
            
            sender_email = 'mrihankg@gmail.com'
            receiver_email = user.email

            # Create a multipart message
            message = MIMEMultipart()
            message['Subject'] = email_subject
            message['From'] = sender_email
            message['To'] = receiver_email

            # Attach the message body as plain text
            message.attach(MIMEText(email_message, 'plain'))

            # SMTP server configuration
            smtp_host = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'mrihankg@gmail.com'
            smtp_password = 'rwrqssikdnqbhjjr'

            try:
                # Create an SMTP connection
                with smtplib.SMTP(smtp_host, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(sender_email, receiver_email, message.as_string())

                print("Email sent successfully!")
            except Exception as e:
                print("An error occurred while sending the email:", str(e))
        else:
            print("User not found.")

    def save(self):
        email = self.validated_data['email']
        user = User.objects.get(email=email)
        user.save()


def generate_token(user):
    token = default_token_generator.make_token(user)
    return token

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    new_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        user = self.context['request'].user
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect.")

        if new_password != confirm_password:
            raise serializers.ValidationError("New password and confirm password do not match.")

        return attrs

    def save(self):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'})

    def save(self, user):
        user.password = make_password(self.validated_data['password'])
        user.save()


class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      emp_id = smart_str(urlsafe_base64_decode(uid))
      user = User.objects.get(emp_id=emp_id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(user, token)
      raise serializers.ValidationError('Token is not Valid or Expired')