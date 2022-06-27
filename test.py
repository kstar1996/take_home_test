from main import app
import unittest
import json


class FlaskTestCase(unittest.TestCase):
    def test_home(self):
        test_data = {
            'all_participants': '/participant?ref_num=all',
            'retrieve_participant': '/participant?ref_num={ref_num}',
            'add_participant': '/participant/add/{ref_num}',
            'update_participant': '/participant/update/{ref_num}',
            'delete_participant': '/participant/delete/{ref_num}',
        }
        tester = app.test_client(self)
        response = tester.get('/')
        # make sure response status code equals 200
        self.assertEqual(response.status_code, 200)
        # check if the response data is correct
        self.assertEqual(test_data, json.loads(response.data))

    def test_get_all_participants(self):
        test_data = {
            "A123": {
                "name": "eujin-1",
                "date_of_birth": "19960521",
                "phone_number": "+821012345678",
                "address": "South Korea"
            },
            "A456": {
                "name": "eujin-2",
                "date_of_birth": "19910409",
                "phone_number": "+821098765432",
                "address": "UK"
            }
        }
        tester = app.test_client(self)

        response1 = tester.post('/participant/add/A123',
                                data=json.dumps(test_data["A123"]), headers={'Content-Type': 'application/json'})
        self.assertEqual(response1.status_code, 200)

        response2 = tester.post('/participant/add/A456',
                                data=json.dumps(test_data["A456"]), headers={'Content-Type': 'application/json'})
        self.assertEqual(response2.status_code, 200)

        response3 = tester.get('/participant?ref_num=all', content_type='application/json')
        self.assertEqual(response3.status_code, 200)

        self.assertTrue(response3.json == {
            "A123": {
                "name": "eujin-1",
                "date_of_birth": "19960521",
                "phone_number": "+821012345678",
                "address": "South Korea"
            },
            "A456": {
                "name": "eujin-2",
                "date_of_birth": "19910409",
                "phone_number": "+821098765432",
                "address": "UK"
            }
        }, True)

    def test_get_particular_participant(self):
        test_data = {
            "A123": {
                "name": "eujin-1",
                "date_of_birth": "19960521",
                "phone_number": "+821012345678",
                "address": "South Korea"
            },
            "A456": {
                "name": "eujin-2",
                "date_of_birth": "19910409",
                "phone_number": "+821098765432",
                "address": "UK"
            }
        }
        tester = app.test_client(self)

        response1 = tester.post('/participant/add/A123',
                                data=json.dumps(test_data["A123"]), headers={'Content-Type': 'application/json'})
        self.assertEqual(response1.status_code, 200)
        response2 = tester.post('/participant/add/A456',
                                data=json.dumps(test_data["A456"]), headers={'Content-Type': 'application/json'})
        self.assertEqual(response2.status_code, 200)

        response3 = tester.get('/participant?ref_num=A123', content_type='application/json')
        self.assertEqual(response3.status_code, 200)

        self.assertTrue(response3.json == {
            "name": "eujin-1",
            "date_of_birth": "19960521",
            "phone_number": "+821012345678",
            "address": "South Korea"
        }, True)

    def test_update_participant(self):
        test_data1 = {
            "name": "eujin-1",
            "date_of_birth": "19960521",
            "phone_number": "+821012345678",
            "address": "South Korea"
        }
        test_data2 = {
            "name": "eujin-1",
            "date_of_birth": "19960521",
            "phone_number": "+447975777666",
            "address": "UK"
        }

        tester = app.test_client(self)

        response1 = tester.post('/participant/add/A123',
                                data=json.dumps(test_data1), headers={'Content-Type': 'application/json'})
        self.assertEqual(response1.status_code, 200)
        response2 = tester.post('/participant/update/A123',
                                data=json.dumps(test_data2), headers={'Content-Type': 'application/json'})
        self.assertEqual(response2.status_code, 200)

        response3 = tester.get('/participant?ref_num=A123', content_type='application/json')
        self.assertEqual(response3.status_code, 200)

        self.assertTrue(response3.json == {
            "name": "eujin-1",
            "date_of_birth": "19960521",
            "phone_number": "+447975777666",
            "address": "UK"
        }, True)

    def test_delete_participant(self):
        test_data = {
            "name": "eujin-1",
            "date_of_birth": "19960521",
            "phone_number": "+821012345678",
            "address": "South Korea"
        }

        tester = app.test_client(self)

        response1 = tester.post('/participant/add/A123',
                                data=json.dumps(test_data), headers={'Content-Type': 'application/json'})
        self.assertEqual(response1.status_code, 200)

        response2 = tester.delete('/participant/delete/A123')
        self.assertEqual(response2.status_code, 200)

        response3 = tester.get('/participant?ref_num=all', content_type='application/json')
        self.assertEqual(response3.status_code, 200)
        self.assertTrue(response3.json == {}, True)


if __name__ == '__main__':
    unittest.main()
