import secrets
import uuid

from django.contrib.auth.models import User
from django.shortcuts import render
from requests import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializer import *
from .models import *
from rest_framework import generics, status


class QuesttionList(generics.ListAPIView):
    queryset = Questtion.objects.all()
    serializer_class = QuesttionSerializer


class DirectionList(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class CandidateList(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return CandidateSerializer
        return CandidateCreateSerializer


class UserCreateAnswer(generics.ListCreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = AnswerSerializer


class UserAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = AnswerSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return AnswerSerializer
        return AnswerCreateSerializer

class APIKeyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        key = str(uuid.uuid4())
        api_key = APIKey.objects.create(user=user, key=key)
        return Response({'key': api_key.key}, status=status.HTTP_201_CREATED)

