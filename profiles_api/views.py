from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import status
from profiles_api import serializers

from profiles_api import models

from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

from rest_framework import filters

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
# Create your views here.

class HelloApiView(APIView):

      serializer_class = serializers.HelloSer

      def get(self, request, format = None):

            li = [1, 2, 'Hello']
            
            return Response({'message':'Hello World!', 'api': li})
      
      def post(self, request):

            serializer = self.serializer_class(data = request.data)
            # print(request.data)
            if serializer.is_valid():
                  name = serializer.validated_data.get('name')
                  return Response({'message': name})
            
            else:
                  return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
      
      def put(self, request, pk = None):
            return Response({'message':'PUT'})
      
      def patch(self, request, pk = None):
            return Response({'message':'PATCH'})
      
      def delete(self, request, pk = None):
            return Response({'message':'Delete'})

class HelloViewSet(viewsets.ViewSet):

      serializer_class = serializers.HelloSer

      def list(self, request):
            
            li = [1, 2, 'Hello']
            return Response({'message':'Hello World!', 'api': li}) 
      
      def create(self, request):
            serializer = self.serializer_class(data = request.data)

            if serializer.is_valid():
                  name = serializer.validated_data.get('name')
                  return Response({'message' : 'Success' + name})

            else:
                  return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
      
      def retrieve(self, request, pk = None):
            return Response({'http_method':'GET'})
      
      def update(self, request, pk = None):
            return Response({'http_method': 'PUT'})

      def partial_update(self, request, pk= None):
            return Response({'http_method': 'p_update'})
      
      def destroy(self, request, pk = None):
            return Response({'http_response': 'Delete'})


class UserProfileViewSet(viewsets.ModelViewSet):
      serializer_class = serializers.ProfileSer
      queryset = models.UserProfile.objects.all()

      authentication_classes = (TokenAuthentication,)
      permission_classes = (permissions.UpdateProfilePermission, )

      filter_backends = (filters.SearchFilter, )
      search_fields = ('name', 'email',)

class UserLoginView(ObtainAuthToken):
      renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES