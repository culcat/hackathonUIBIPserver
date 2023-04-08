
from django.contrib import admin
from django.urls import path
from server.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directions/', DirectionList.as_view(), name='direction_list'),
    path('candidates/', CandidateList.as_view(), name='candidate_list'),
    path('candidates/<int:pk>/', CandidateDetail.as_view(), name='candidate_detail'),
    path('question/', QuesttionList.as_view(), name='questtion_list'),
    path('answer/<int:pk>/', UserAnswerDetail.as_view(), name='answer_list'),
    path('answer/', UserCreateAnswer.as_view(), name='answer_ist'),

]
