from iDrive.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class BarUserSerializer(serializers.ModelSerializer):
    promotions = serializers.PrimaryKeyRelatedField(
        many=True, required=False)
    cur_parties = serializers.SerializerMethodField(
        'get_cur_parties')

    class Meta:
        model = BarUser
        fields = (
            'id', 'geo_lat', 'geo_long', 
            'description', 'promotions', 'cur_parties')

    def get_cur_parties(self, obj):
        return list(Party.objects.filter(
            closed=False, 
            cur_checkin_bar=obj))

class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = ('id', 'bar', 'description', 'min_amount', 'max_amount',
            'active_monday','active_tuesday','active_wednesday','active_thursday',
            'active_sunday','active_saturday','active_sunday', 'expiry_date')

class PartySerializer(serializers.ModelSerializer):
    past_members = serializers.PrimaryKeyRelatedField(
        required=False, many=True)
    des_drivers = serializers.PrimaryKeyRelatedField(
        required=False, many=True)

    class Meta:
        model = Party
        fields = (
            'id', 'cur_checkin_bar', 
            'closed', 'active_members',
            'past_members', 'des_drivers',
            'code')
        read_only_fields=('code',)

class PartyUserSerializer(serializers.ModelSerializer):
    friends = serializers.PrimaryKeyRelatedField(
        required=False, many=True)

    class Meta:
        model = PartyUser
        fields = (
            'id', 'cur_party',
            'past_parties', 'friends',
            'name')
        read_only_fields = ('past_parties',)






