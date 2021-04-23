from rest_framework import generics, status
from app.serializers.password_reset import PasswordResetEmailRequestSerializer, SetNewPasswordSerializer
from rest_framework.response import Response
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from app.models import User
from rest_framework import viewsets


class RequestPasswordEmailReset(generics.GenericAPIView):
    serializer_class = PasswordResetEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        return Response({'success': "A link to reset your password has just been sent"},
                        status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):

    def get(self, request, uidb64, token):

        try:
            user_pk = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_pk)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({"error": "Invalid token, please request a new one"},
                                status=status.HTTP_401_UNAUTHORIZED)

            return Response({"success": True,
                             "message": "Credentials Valid",
                             "uidb64": uidb64,
                             "token": token},
                            status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:

            return Response({"error": "Invalid token, please request a new one"},
                            status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPI(viewsets.ModelViewSet):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"success": True,
                         "message": "Password reset successful"},
                        status=status.HTTP_200_OK)
