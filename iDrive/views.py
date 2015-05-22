from iDrive.models import *
from iDrive.serializers import *

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.models import User

from random import randrange


class BarUserViewSet(viewsets.ModelViewSet):
    serializer_class = BarUserSerializer
    #Need to add addtional permission for owner only
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = BarUser.objects.all()

    def pre_save(self, obj):
        # This assumes that the Bar User is created with the corresponding User object
        # i.e. no admins can create a BarUser
        obj.user = self.request.user 

class PromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionSerializer
    # Need to add additional permissions for owner only
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Promotion.objects.all()

class PartyViewSet(viewsets.ModelViewSet):
    serializer_class = PartySerializer
    # Need to add additional permissions for party members and nearest bar.
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Party.objects.all()

    def get_queryset(self):
        queryset = Party.objects.all()
        codeParams = self.request.QUERY_PARAMS.get('code', None)

        if codeParams is not None:
            queryset = queryset.filter(code=codeParams)[:1]
        return queryset

    def pre_save(self, obj):
        obj.code = randrange(1000,9999)



class PartyUserViewSet(viewsets.ModelViewSet):
    serializer_class = PartyUserSerializer
    # Need to add additional permissions for party members
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = PartyUser.objects.all()

    
