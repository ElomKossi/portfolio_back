
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import EducationGenericAPIView, ExperienceGenericAPIView, ProjectGenericAPIView, SkillGenericAPIView, TechnologyGenericAPIView, InterestGenericAPIView

urlpatterns = [
    path('education', EducationGenericAPIView.as_view(), name="education_api"),
    path('education/<str:pk>', EducationGenericAPIView.as_view(), name="education_pk_api"),
    
    path('experience', ExperienceGenericAPIView.as_view(), name="experience_api"),
    path('experience/<str:pk>', ExperienceGenericAPIView.as_view(), name="experience_pk_api"),
    
    path('project', ProjectGenericAPIView.as_view(), name="project_api"),
    path('project/<str:pk>', ProjectGenericAPIView.as_view(), name="project_pk_api"),
    
    path('skill', SkillGenericAPIView.as_view(), name="skill_api"),
    path('skill/<str:pk>', SkillGenericAPIView.as_view(), name="skill_pk_api"),
    
    path('technology', TechnologyGenericAPIView.as_view(), name="technology_api"),
    path('technology/<str:pk>', TechnologyGenericAPIView.as_view(), name="technology_pk_api"),
    
    path('interest', InterestGenericAPIView.as_view(), name="interest_api"),
    path('interest/<str:pk>', InterestGenericAPIView.as_view(), name="interest_pk_api"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
