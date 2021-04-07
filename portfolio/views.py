from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Education, Experience, Project, Skill, Technology, Interest
from .serializers import (
    EducationSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    SkillSerializer,
    TechnologySerializer,
    InterestSerializer,
)


class EducationGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class ExperienceGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class ProjectGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class SkillGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class TechnologyGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class InterestGenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)

    def post(self, request):
        return Response({"data": self.create(request).data})

    def put(self, request, pk=None):
        return Response({"data": self.partial_update(request, pk).data})

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


""" @api_view(['GET'])
def educations():
    educations = Education.objects.all()
    serializers = EducationSerializer(educations)
    return Response(serializers.data)


@api_view(['GET'])
def experiences():
    experiences = Experience.objects.all()
    serializers = ExperienceSerializer(experiences)
    return Response(serializers.data)


@api_view(['GET'])
def projects():
    projects = Project.objects.all()
    serializers = ProjectSerializer(projects)
    return Response(serializers.data)


@api_view(['GET'])
def skills():
    skills = Skill.objects.all()
    serializers = SkillSerializer(skills)
    return Response(serializers.data)


@api_view(['GET'])
def technologies():
    technologies = Technology.objects.all()
    serializers = TechnologySerializer(technologies)
    return Response(serializers.data)


@api_view(['GET'])
def interests():
    interests = Interest.objects.all()
    serializers = InterestSerializer(interests)
    return Response(serializers.data) """
