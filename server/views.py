from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import generics


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
