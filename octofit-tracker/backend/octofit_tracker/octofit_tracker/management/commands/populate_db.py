from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')

        # Delete in order to respect foreign key dependencies
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating users (superheroes)...')
        users_data = [
            {'name': 'Tony Stark', 'email': 'tony@avengers.com', 'password': 'ironman123'},
            {'name': 'Steve Rogers', 'email': 'steve@avengers.com', 'password': 'cap123'},
            {'name': 'Natasha Romanoff', 'email': 'natasha@avengers.com', 'password': 'widow123'},
            {'name': 'Bruce Banner', 'email': 'bruce@avengers.com', 'password': 'hulk123'},
            {'name': 'Bruce Wayne', 'email': 'bruce@gotham.com', 'password': 'batman123'},
            {'name': 'Clark Kent', 'email': 'clark@dailyplanet.com', 'password': 'superman123'},
            {'name': 'Diana Prince', 'email': 'diana@themyscira.com', 'password': 'wonderwoman123'},
            {'name': 'Barry Allen', 'email': 'barry@ccpd.com', 'password': 'flash123'},
        ]

        users = {}
        for data in users_data:
            user = User.objects.create(**data)
            users[data['name']] = user
            self.stdout.write(f"  Created user: {user.name}")

        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.set([
            users['Tony Stark'],
            users['Steve Rogers'],
            users['Natasha Romanoff'],
            users['Bruce Banner'],
        ])
        self.stdout.write(f"  Created team: {team_marvel.name}")

        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.set([
            users['Bruce Wayne'],
            users['Clark Kent'],
            users['Diana Prince'],
            users['Barry Allen'],
        ])
        self.stdout.write(f"  Created team: {team_dc.name}")

        self.stdout.write('Creating activities...')
        activities_data = [
            {'user': users['Tony Stark'], 'activity_type': 'Running', 'duration': 45, 'date': date(2026, 5, 1)},
            {'user': users['Steve Rogers'], 'activity_type': 'Weightlifting', 'duration': 60, 'date': date(2026, 5, 1)},
            {'user': users['Natasha Romanoff'], 'activity_type': 'Yoga', 'duration': 30, 'date': date(2026, 5, 2)},
            {'user': users['Bruce Banner'], 'activity_type': 'Cycling', 'duration': 50, 'date': date(2026, 5, 2)},
            {'user': users['Bruce Wayne'], 'activity_type': 'Martial Arts', 'duration': 90, 'date': date(2026, 5, 1)},
            {'user': users['Clark Kent'], 'activity_type': 'Running', 'duration': 20, 'date': date(2026, 5, 3)},
            {'user': users['Diana Prince'], 'activity_type': 'Swimming', 'duration': 40, 'date': date(2026, 5, 3)},
            {'user': users['Barry Allen'], 'activity_type': 'Sprinting', 'duration': 15, 'date': date(2026, 5, 4)},
        ]

        for data in activities_data:
            activity = Activity.objects.create(**data)
            self.stdout.write(f"  Created activity: {activity.user.name} - {activity.activity_type}")

        self.stdout.write('Creating leaderboard entries...')
        leaderboard_data = [
            {'user': users['Tony Stark'], 'score': 480},
            {'user': users['Steve Rogers'], 'score': 520},
            {'user': users['Natasha Romanoff'], 'score': 390},
            {'user': users['Bruce Banner'], 'score': 410},
            {'user': users['Bruce Wayne'], 'score': 600},
            {'user': users['Clark Kent'], 'score': 350},
            {'user': users['Diana Prince'], 'score': 445},
            {'user': users['Barry Allen'], 'score': 700},
        ]

        for data in leaderboard_data:
            entry = Leaderboard.objects.create(**data)
            self.stdout.write(f"  Created leaderboard entry: {entry.user.name} - {entry.score}")

        self.stdout.write('Creating workouts...')
        workouts_data = [
            {
                'name': 'Iron Man Endurance',
                'description': 'High-intensity endurance training inspired by Tony Stark',
                'exercises': ['Running 5km', 'Pull-ups 3x10', 'Push-ups 3x20', 'Plank 3x60s'],
            },
            {
                'name': 'Super Soldier Strength',
                'description': 'Full body strength workout inspired by Captain America',
                'exercises': ['Deadlift 5x5', 'Bench Press 5x5', 'Squat 5x5', 'Military Press 5x5'],
            },
            {
                'name': 'Dark Knight Combat',
                'description': 'Martial arts and agility training inspired by Batman',
                'exercises': ['Shadow Boxing 3x5min', 'Jump Rope 10min', 'Plyometric Push-ups 3x12', 'Box Jumps 3x10'],
            },
            {
                'name': 'Wonder Woman Warrior',
                'description': 'Functional fitness workout inspired by Wonder Woman',
                'exercises': ['Kettlebell Swings 4x15', 'Turkish Get-ups 3x5', 'Battle Ropes 4x30s', 'Lunges 3x12'],
            },
        ]

        for data in workouts_data:
            workout = Workout.objects.create(**data)
            self.stdout.write(f"  Created workout: {workout.name}")

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
