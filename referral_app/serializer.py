from rest_framework import serializers
from .models import CustomUser


class PhoneSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)

class AuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    auth_code  = serializers.CharField(max_length=4)

class ReferralCodeSerializer(serializers.Serializer):
    referral_code = serializers.CharField(max_length=6)

class ProfileSerializer(serializers.ModelSerializer):
    referral = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'invite_code', 'referral_code', 'referrals']

    def get_referrals(self, obj):
        users = CustomUser.objects.filter(referral_code=obj.invite_code)
        return [user.phone_number for user in users]




















