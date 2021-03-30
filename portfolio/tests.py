from django.test import TestCase
from mixer.backend.django import mixer
import pytest
from .models import Education


class test_education_model(TestCase):

    # def setUp(self):
    #     self.education = Education.objects.create(
    #         title="LICENCE EN INFORMATIQUE", school="INSTITUT AFRICAIN D'INFORMATIQUE", lacation="Lomé, TOGO", duration="2014 - 2017")

    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a + b

        assert c == 3

    def test_education_can_be_created(self):
        education = mixer.blend(Education)
        rslt = Education.objects.last()

        assert rslt == education

    def test_str_return(self):
        education = mixer.blend(Education)
        rslt = Education.objects.last()

        assert str(rslt) == education.title
