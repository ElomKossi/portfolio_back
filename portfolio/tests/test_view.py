from django.test import TestCase
from mixer.backend.django import mixer
import pytest
from portfolio.models import Education, Experience, Project, Skill, Technology, Interest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestEducationViews(TestCase):

    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_education_list_works(self):
        education = mixer.blend(Education, title="Geoffrey")

        educatio2 = mixer.blend(Education, title="Naomi")

        url = reverse("education_api")

        # call the url
        response = self.client.get(url)

        print(dir(response), "response")

        # assertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

    def test_education_create_works(self):
        # data
        input_data = {
            "title": "Wangari",
            "school": "Maathai",
            "lacation": "Lomé TOGO",
            "duration": "1000"
        }

        url = reverse("education_api")

        # call the url
        response = self.client.post(url, data=input_data)

        # assertions
        # - json
        # - status

        print(response.data)
        assert response.json() != None
        assert response.status_code == 200
        assert Education.objects.count() == 1

    def test_education_detail_works(self):
        # create a education

        education = mixer.blend(Education, pk=1, title="Geoffrey")
        print(Education.objects.last().pk, "qs")
        url = reverse("education_pk_api", kwargs={"pk": 1})
        response = self.client.get(url)

        education2 = mixer.blend(Education, pk=2, title="Naomi")
        url2 = reverse("education_pk_api", kwargs={"pk": 2})
        response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["data"]["title"] == "Geoffrey"

        assert response2.json()["data"]["title"] == "Naomi"

    def test_education_delete_works(self):
        # create a education

        education = mixer.blend(Education, pk=1, title="Geoffrey")
        assert Education.objects.count() == 1

        url = reverse("education_pk_api", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Education.objects.count() == 0


class TestExperienceViews(TestCase):

    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_experience_list_works(self):
        experience = mixer.blend(Experience, title="Geoffrey")

        experience2 = mixer.blend(Experience, title="Naomi")

        url = reverse("experience_api")

        # call the url
        response = self.client.get(url)

        print(dir(response), "response")

        # assertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

    def test_experience_create_works(self):
        # data
        input_data = {
            "title": "Wangari",
            "company": "Maathai",
            "lacation": "Lomé TOGO",
            "duration": "1000",
            "summary": "1000"
        }

        url = reverse("experience_api")

        # call the url
        response = self.client.post(url, data=input_data)

        # assertions
        # - json
        # - status

        print(response.data)
        assert response.json() != None
        assert response.status_code == 200
        assert Experience.objects.count() == 1

    def test_experience_detail_works(self):
        # create a experience

        experience = mixer.blend(Experience, pk=1, title="Geoffrey")
        print(Experience.objects.last().pk, "qs")
        url = reverse("experience_pk_api", kwargs={"pk": 1})
        response = self.client.get(url)

        experience2 = mixer.blend(Experience, pk=2, title="Naomi")
        url2 = reverse("experience_pk_api", kwargs={"pk": 2})
        response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["data"]["title"] == "Geoffrey"

        assert response2.json()["data"]["title"] == "Naomi"

    def test_experience_delete_works(self):
        # create a experience

        experience = mixer.blend(Experience, pk=1, title="Geoffrey")
        assert Experience.objects.count() == 1

        url = reverse("experience_pk_api", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Experience.objects.count() == 0


class TestProjectViews(TestCase):

    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_project_list_works(self):
        project = mixer.blend(Project, title="Geoffrey")

        project2 = mixer.blend(Project, title="Naomi")

        url = reverse("project_api")

        # call the url
        response = self.client.get(url)

        print(dir(response), "response")

        # assertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

    def test_project_create_works(self):
        # data
        input_data = {
            "title": "Wangari",
            "duration": "1000",
            "summary": "1000"
        }

        url = reverse("project_api")

        # call the url
        response = self.client.post(url, data=input_data)

        # assertions
        # - json
        # - status

        print(response.data)
        assert response.json() != None
        assert response.status_code == 200
        assert Project.objects.count() == 1

    def test_project_detail_works(self):
        # create a project

        project = mixer.blend(Project, pk=1, title="Geoffrey")
        print(Project.objects.last().pk, "qs")
        url = reverse("project_pk_api", kwargs={"pk": 1})
        response = self.client.get(url)

        project2 = mixer.blend(Project, pk=2, title="Naomi")
        url2 = reverse("project_pk_api", kwargs={"pk": 2})
        response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["data"]["title"] == "Geoffrey"

        assert response2.json()["data"]["title"] == "Naomi"

    def test_project_delete_works(self):
        # create a project

        project = mixer.blend(Project, pk=1, title="Geoffrey")
        assert Project.objects.count() == 1

        url = reverse("project_pk_api", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Project.objects.count() == 0


class TestSkillViews(TestCase):

    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_skill_list_works(self):
        skill = mixer.blend(Skill, name="Geoffrey")

        skill2 = mixer.blend(Skill, name="Naomi")

        url = reverse("skill_api")

        # call the url
        response = self.client.get(url)

        print(dir(response), "response")

        # assertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

    def test_skill_create_works(self):
        # data
        input_data = {
            "name": "Wangari-tech",
        }

        url = reverse("skill_api")

        # call the url
        response = self.client.post(url, data=input_data)

        # assertions
        # - json
        # - status

        print(response.data)
        assert response.json() != None
        assert response.status_code == 200
        assert Skill.objects.count() == 1

    def test_skill_detail_works(self):
        # create a skill

        skill = mixer.blend(Skill, pk=1, name="Geoffrey")
        print(Skill.objects.last().pk, "qs")
        url = reverse("skill_pk_api", kwargs={"pk": 1})
        response = self.client.get(url)

        skill2 = mixer.blend(Skill, pk=2, name="Naomi")
        url2 = reverse("skill_pk_api", kwargs={"pk": 2})
        response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["data"]["name"] == "Geoffrey"

        assert response2.json()["data"]["name"] == "Naomi"

    def test_skill_delete_works(self):
        # create a skill

        skill = mixer.blend(Skill, pk=1, name="Geoffrey")
        assert Skill.objects.count() == 1

        url = reverse("skill_pk_api", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Skill.objects.count() == 0


class TestTechnologyViews(TestCase):

    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_technology_list_works(self):
        technology = mixer.blend(Technology, name="Geoffrey")

        technology2 = mixer.blend(Technology, name="Naomi")

        url = reverse("technology_api")

        # call the url
        response = self.client.get(url)

        print(dir(response), "response")

        # assertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

    def test_technology_create_works(self):
        # datas

        skill_input_data = {
            "name": "Wangari-tech"
        }

        skill_url = reverse("skill_api")

        # call the url
        skill_response = self.client.post(skill_url, data=skill_input_data)
        
        technology_input_data = {
            "name": "Wangari",
            "skill": Skill.objects.last().pk
        }

        url = reverse("technology_api")

        # call the url
        response = self.client.post(url, data=technology_input_data)

        # assertions
        # - json
        # - status

        print(response.data)
        assert response.json() != None
        assert response.status_code == 200
        assert Technology.objects.count() == 1

    def test_technology_detail_works(self):
        # create a technology

        technology = mixer.blend(Technology, pk=1, name="Geoffrey")
        print(Technology.objects.last().pk, "qs")
        url = reverse("technology_pk_api", kwargs={"pk": 1})
        response = self.client.get(url)

        technology2 = mixer.blend(Technology, pk=2, name="Naomi")
        url2 = reverse("technology_pk_api", kwargs={"pk": 2})
        response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["data"]["name"] == "Geoffrey"

        assert response2.json()["data"]["name"] == "Naomi"

    def test_technology_delete_works(self):
        # create a technology

        technology = mixer.blend(Technology, pk=1, name="Geoffrey")
        assert Technology.objects.count() == 1

        url = reverse("technology_pk_api", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Technology.objects.count() == 0


class TestInterestViews(TestCase):

    def setUp(self):
        self.client = APIClient()

        print(self.client, "self.client")

    def test_interest_list_works(self):
        interest = mixer.blend(Interest, name="Geoffrey")

        interest2 = mixer.blend(Interest, name="Naomi")

        url = reverse("interest_api")

        # call the url
        response = self.client.get(url)

        print(dir(response), "response")

        # assertions
        # - json
        # - status
        assert response.json() != None

        assert len(response.json()) == 2

        assert response.status_code == 200

    def test_interest_create_works(self):
        # data
        input_data = {
            "name": "Wangari"
        }

        url = reverse("interest_api")

        # call the url
        response = self.client.post(url, data=input_data)

        # assertions
        # - json
        # - status

        print(response.data)
        assert response.json() != None
        assert response.status_code == 200
        assert Interest.objects.count() == 1

    def test_interest_detail_works(self):
        # create a interest

        interest = mixer.blend(Interest, pk=1, name="Geoffrey")
        print(Interest.objects.last().pk, "qs")
        url = reverse("interest_pk_api", kwargs={"pk": 1})
        response = self.client.get(url)

        interest2 = mixer.blend(Interest, pk=2, name="Naomi")
        url2 = reverse("interest_pk_api", kwargs={"pk": 2})
        response2 = self.client.get(url2)

        # assertions
        # - json
        # - status

        print(response.json(), "response json")

        assert response.json() != None
        assert response.status_code == 200
        assert response.json()["data"]["name"] == "Geoffrey"

        assert response2.json()["data"]["name"] == "Naomi"

    def test_interest_delete_works(self):
        # create a interest

        interest = mixer.blend(Interest, pk=1, name="Geoffrey")
        assert Interest.objects.count() == 1

        url = reverse("interest_pk_api", kwargs={"pk": 1})
        response = self.client.delete(url)
        # assertions
        # - json
        # - status

        print(dir(response.json), "response json")
        print((response.status_code), "response json")

        assert response.status_code == 204

        assert Interest.objects.count() == 0