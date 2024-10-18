from rest_framework.permissions import IsAuthenticated
from django_otp.plugins.otp_totp.models import TOTPDevice
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SetupOTPView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        # Créer un dispositif TOTP pour l'utilisateur s'il n'en a pas
        device, created = TOTPDevice.objects.get_or_create(user=user, confirmed=False)

        if created:
            # Retourne les informations nécessaires pour configurer l'appareil
            return Response({
                "detail": "Dispositif OTP créé. Veuillez scanner le QR code avec votre application d'authentification.",
                "otp_secret": device.bin_key  # Clé secrète pour générer le QR code
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"detail": "Un dispositif OTP existe déjà pour cet utilisateur."},
                status=status.HTTP_400_BAD_REQUEST,
            )
