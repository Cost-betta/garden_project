from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class CultivarTestCase(APITestCase):
    fixtures = [
        'cultivar_test',
    ]

    def setUp(self):
        """Подготовка контекста для теста."""
        credentials = {'username': 'admin@example.com', 'password': '123456'}
        get_user_model().objects.create_superuser(**credentials)
        self.client.login(**credentials)

    def test_cultivar_filter_allele(self):
        url = reverse('identikit_hazelnut:cultivars-list')
        expected = {
            300: {
                "id": 300,
                "name": "Test 0",
                "country": "POLAND",
                "region": "CENTRAL_EUROPEAN",
                "description": "",
                "famous": None,
                "allele": {
                    "id": 300,
                    "allele_1": "5/",
                    "allele_2": "11"
                },
                "leaf": 300,
                "nut": 300
            },
            301: {
                "id": 301,
                "name": "Test 1",
                "country": "ALBANIA",
                "region": "OTHER",
                "description": "",
                "famous": None,
                "allele": {
                    "id": 301,
                    "allele_1": "8/",
                    "allele_2": "32"
                },
                "leaf": 301,
                "nut": 301
            },
            302: {
                "id": 302,
                "name": "Test 2",
                "country": "SPAIN",
                "region": "SPANISH_ITALIAN",
                "description": "",
                "famous": None,
                "allele": {
                    "id": 302,
                    "allele_1": "15/",
                    "allele_2": "22"
                },
                "leaf": 302,
                "nut": 302
            },
            303: {
                "id": 303,
                "name": "Test 3",
                "country": "ESTONIA",
                "region": "CENTRAL_EUROPEAN",
                "description": "",
                "famous": None,
                "allele": {
                    "id": 303,
                    "allele_1": "9",
                    "allele_2": "20/"
                },
                "leaf": 303,
                "nut": 303
            },
            304: {
                "id": 304,
                "name": "Test 4",
                "country": "CHILE",
                "region": "SPANISH_ITALIAN",
                "description": "",
                "famous": None,
                "allele": {
                    "id": 304,
                    "allele_1": "2",
                    "allele_2": "6/"
                },
                "leaf": 304,
                "nut": 304
            }
        }
        with self.assertNumQueries(306):
            response = self.client.get(
                url,
                data={
                    'expand': 'allele',
                    'limit': 310
                },
            )
            self.assertEqual(response.status_code, 200)
            for cultivar in response.json()['results']:
                id_ = cultivar['id']
                if id_ in [300, 301, 302, 303, 304]:
                    self.assertDictEqual(
                        expected[id_],
                        cultivar,
                        f"API don't work with the parameter 'expand'. expected: {expected[id_]}, actual: {cultivar}.",
                    )

    def test_cultivar_filter_alleles(self):
        url = reverse('identikit_hazelnut:cultivars-list')
        expected = {
            "id": 240,
            "name": "Moscow N26",
            "country": "RUSSIA",
            "region": "OTHER",
            "description": "",
            "famous": None,
            "allele": {
                "id": 240,
                "allele_1": "1/",
                "allele_2": "29"
            },
            "leaf": 240,
            "nut": 240
        }
        with self.assertNumQueries(5):
            response = self.client.get(
                url,
                data={
                    'expand': 'allele',
                    'alleles': '29,29/'
                },
            )
            self.assertEqual(response.status_code, 200)
            actual = response.json()['results'][0]
            self.assertDictEqual(
                expected,
                actual,
                f"API don't work with the parameter 'alleles'. expected: {expected}, actual: {actual}.",
            )

    def test_cultivar_filter_names(self):
        url = reverse('identikit_hazelnut:cultivars-list')
        expected = {
            87: {
                "id": 87,
                "name": "Густав (Gustav’s Zeller)",
                "country": "GERMANY",
                "region": "CENTRAL_EUROPEAN",
                "description": "",
                "famous": True,
                "allele": {
                    "id": 87,
                    "allele_1": "15/",
                    "allele_2": "20/"
                },
                "leaf": 87,
                "nut": 87
            },
            30: {
                "id": 30,
                "name": "Сиклер (Macrocarpa)",
                "country": "UNITED_KINGDOM",
                "region": "SPANISH_ITALIAN",
                "description": "",
                "famous": True,
                "allele": {
                    "id": 30,
                    "allele_1": "1/",
                    "allele_2": "2"
                },
                "leaf": 30,
                "nut": 30
            },
            104: {
                "id": 104,
                "name": "Сиклер (Sickler’s Zellernuss)",
                "country": "GERMANY",
                "region": "CENTRAL_EUROPEAN",
                "description": "",
                "famous": True,
                "allele": {
                    "id": 104,
                    "allele_1": "5/",
                    "allele_2": "20/"
                },
                "leaf": 104,
                "nut": 104
            }
        }
        with self.assertNumQueries(3):
            response = self.client.get(
                url,
                data={
                    'expand': 'allele',
                    'names': 'Густ,Сикл'
                },
            )
            self.assertEqual(response.status_code, 200)
            for cultivar in response.json()['results']:
                id_ = cultivar['id']
                self.assertDictEqual(
                    expected[id_],
                    cultivar,
                    f"API don't work with the parameter 'expand'. expected: {expected[id_]}, actual: {cultivar}.",
                )

    def test_cultivar_filter_alleles_(self):
        url = reverse('identikit_hazelnut:cultivars-list')
        with self.assertNumQueries(16):
            response = self.client.get(
                url,
                data={
                    'pollinators': 'Giant',
                    'expand': 'allele',
                },
            )
            self.assertEqual(response.status_code, 200)
            self.assertNotIn('5/', response.json()['results'],f'Pollinators were chosen incorrectly')
            self.assertNotIn('15/', response.json()['results'], f'Pollinators were chosen incorrectly')