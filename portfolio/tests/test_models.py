from django.test import TestCase
from mixer.backend.django import mixer
import pytest
from portfolio.models import Education, Experience, Project, Skill, Technology, Interest

pytestmark = pytest.mark.django_db


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


class test_experience_model(TestCase):
    def test_experience_can_be_created(self):
        experience = mixer.blend(Experience)
        rslt = Experience.objects.last()

        assert rslt == experience

    def test_str_return(self):
        experience = mixer.blend(Experience)
        rslt = Experience.objects.last()

        assert str(rslt) == experience.title


class test_project_model(TestCase):
    def test_project_can_be_created(self):
        project = mixer.blend(Project)
        rslt = Project.objects.last()

        assert rslt == project

    def test_str_return(self):
        project = mixer.blend(Project)
        rslt = Project.objects.last()

        assert str(rslt) == project.title


class test_skill_model(TestCase):
    def test_skill_can_be_created(self):
        skill = mixer.blend(Skill)
        rslt = Skill.objects.last()

        assert rslt == skill

    def test_str_return(self):
        skill = mixer.blend(Skill)
        rslt = Skill.objects.last()

        assert str(rslt) == skill.name


class test_technology_model(TestCase):
    def test_technology_can_be_created(self):
        technology = mixer.blend(Technology)
        rslt = Technology.objects.last()

        assert rslt == technology

    def test_str_return(self):
        technology = mixer.blend(Technology)
        rslt = Technology.objects.last()

        assert str(rslt) == technology.name


class test_interest_model(TestCase):
    def test_interest_can_be_created(self):
        interest = mixer.blend(Interest)
        rslt = Interest.objects.last()

        assert rslt == interest

    def test_str_return(self):
        interest = mixer.blend(Interest)
        rslt = Interest.objects.last()

        assert str(rslt) == interest.name
