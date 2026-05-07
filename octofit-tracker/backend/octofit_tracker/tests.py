from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
import datetime


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='securepassword123'
        )

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(
                username='anotheruser',
                email='testuser@example.com',
                password='anotherpassword'
            )


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Alpha Team',
            members=['alice', 'bob']
        )

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Alpha Team')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            username='testuser',
            activity_type='Running',
            duration=30.0,
            date=datetime.date.today()
        )

    def test_activity_str(self):
        self.assertIn('testuser', str(self.activity))
        self.assertIn('Running', str(self.activity))


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.entry = Leaderboard.objects.create(
            username='testuser',
            score=150
        )

    def test_leaderboard_str(self):
        self.assertIn('testuser', str(self.entry))
        self.assertIn('150', str(self.entry))


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Morning Run',
            description='A 5km morning run',
            duration=45.0
        )

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Morning Run')


class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='apiuser',
            email='apiuser@example.com',
            password='securepassword123'
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITest(APITestCase):
    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        data = {'name': 'Beta Team', 'members': ['charlie', 'diana']}
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_activity(self):
        data = {
            'username': 'testuser',
            'activity_type': 'Cycling',
            'duration': 60.0,
            'date': str(datetime.date.today())
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITest(APITestCase):
    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_workout(self):
        data = {
            'name': 'Evening Yoga',
            'description': 'Relaxing yoga session',
            'duration': 30.0
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class APIRootTest(APITestCase):
    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_root_redirect(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [status.HTTP_302_FOUND, status.HTTP_301_MOVED_PERMANENTLY])
