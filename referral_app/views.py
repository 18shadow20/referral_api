import time
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
import random


class AuthView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error':"Номер телефона обязателен"},status=400)
        user = CustomUser.get_or_create_user(phone_number=phone_number)
        temp_code = str(random.randint(1000, 9999))
        user.auth_code = temp_code
        user.save()
        time.sleep(random.randint(1,2))
        return Response({'message':'Успешно создан'},status=200)


class AuthVerifyView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        user = CustomUser.objects.get(phone_number=phone_number)

        if not phone_number:
            return Response({'error':'Номер обязательны'},status=400)
        if not user:
            return Response({'error': "Пользователь не найден"}, status=400)

        user.auth_code = None
        user.save()
        return Response({'message':'Успешная авторизация'},status=200)


class ProfileView(APIView):
    def get(self, request):
        phone_number = request.data.get('phone_number')
        user = CustomUser.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({'error': "Пользователь не найден"}, status=400)

        referrals = CustomUser.objects.filter(referral_code=user.invite_code)
        referral_list = [u.phone_number for u in referrals]
        return Response({
            'phone_number': user.phone_number,
            'invite_code': user.invite_code,
            'referral_code': user.referral_code,
            'referrals': referral_list,
        })

    def post(self, request):
        phone_number = request.data.get('phone_number')
        referral_code = request.data.get('referral_code')
        user = CustomUser.objects.filter(phone_number=phone_number).first()

        if not user:
            return Response({'error':"Пользователь не найден"},status=400)
        if not CustomUser.objects.filter(invite_code=referral_code).exists():
            return Response({'error': 'Такого реферального кода не существует'}, status=400)
        if referral_code == user.invite_code:
            return Response({'error': 'Нельзя использовать свой код'}, status=400)
        if user.referral_code:
            return Response({'error': 'Код уже активирован'}, status=400)

        user.referral_code = referral_code
        user.save()
        return Response({'message': 'Код активирован'}, status=200)




