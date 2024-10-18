from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.core.mail import send_mail

class LoginWithOTPView(APIView):
    def post(self, request):
        # Récupération des identifiants (nom d'utilisateur et mot de passe)
        username = request.data.get('username')
        password = request.data.get('password')

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Vérifier si l'utilisateur a activé l'OTP
            device = TOTPDevice.objects.filter(user=user, confirmed=True).first()
            if device:
                # Génération et envoi du code OTP par e-mail
                code = device.generate_challenge()
                send_mail(
                    'Votre code OTP',
                    f'Votre code OTP est : {code}',
                    'noreply@example.com',  # Adresse email de l'expéditeur
                    [user.email],  # Adresse email du destinataire
                    fail_silently=False,
                )
                return Response(
                    {"detail": "Identifiants valides, un code OTP a été envoyé."},
                    status=status.HTTP_200_OK,
                )
            else:
                # Si l'utilisateur n'a pas d'appareil OTP, retour de la réponse appropriée
                return Response(
                    {"detail": "Aucun appareil OTP configuré pour cet utilisateur."},
                    status=status.HTTP_403_FORBIDDEN,
                )
        else:
            # Si les identifiants sont incorrects
            return Response(
                {"detail": "Identifiants incorrects."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
