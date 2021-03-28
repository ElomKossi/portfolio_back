
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import EducationGenericAPIView, ExperienceGenericAPIView, ProjectGenericAPIView, SkillGenericAPIView, TechnologyGenericAPIView, InterestGenericAPIView

urlpatterns = [
    path('education', EducationGenericAPIView.as_view()),
    path('education/<str:pk>', EducationGenericAPIView.as_view()),
    
    path('experience', ExperienceGenericAPIView.as_view()),
    path('experience/<str:pk>', ExperienceGenericAPIView.as_view()),
    
    path('project', ProjectGenericAPIView.as_view()),
    path('project/<str:pk>', ProjectGenericAPIView.as_view()),
    
    path('skill', SkillGenericAPIView.as_view()),
    path('skill/<str:pk>', SkillGenericAPIView.as_view()),
    
    path('technology', TechnologyGenericAPIView.as_view()),
    path('technology/<str:pk>', TechnologyGenericAPIView.as_view()),
    
    path('interest', InterestGenericAPIView.as_view()),
    path('interest/<str:pk>', InterestGenericAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
