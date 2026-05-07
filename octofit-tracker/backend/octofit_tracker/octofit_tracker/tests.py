from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='Tony Stark',
            email='tony@avengers.com',
            password='ironman123',
        )

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {'name': 'Steve Rogers', 'email': 'steve@avengers.com', 'password': 'cap123'}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_user(self):
        response = self.client.get(f'/api/users/{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Tony Stark')


class TeamAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='Bruce Banner',
            email='bruce@avengers.com',
            password='hulk123',
        )
        self.team = Team.objects.create(name='Team Marvel')
        self.team.members.set([self.user])

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        data = {'name': 'Team DC'}
        response = self.client.post('/api/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_team(self):
        response = self.client.get(f'/api/teams/{self.team.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team Marvel')


class ActivityAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='Natasha Romanoff',
            email='natasha@avengers.com',
            password='widow123',
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='Yoga',
            duration=30,
            date=date(2026, 5, 1),
        )

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_activity(self):
        response = self.client.get(f'/api/activities/{self.activity.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['activity_type'], 'Yoga')


class LeaderboardAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='Barry Allen',
            email='barry@ccpd.com',
            password='flash123',
        )
        self.entry = Leaderboard.objects.create(user=self.user, score=700)

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_leaderboard_entry(self):
        response = self.client.get(f'/api/leaderboard/{self.entry.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['score'], 700)


class WorkoutAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name='Iron Man Endurance',
            description='High-intensity endurance training',
            exercises=['Running 5km', 'Pull-ups 3x10'],
        )

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_workout(self):
        response = self.client.get(f'/api/workouts/{self.workout.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Iron Man Endurance')


class APIRootTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_root_redirects_to_api(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, [status.HTTP_301_MOVED_PERMANENTLY, status.HTTP_302_FOUND])
