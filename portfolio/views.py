from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Education

@api_view(['GET'])
def educations():
    educations = Education.objects.all()

    return Response(educations)