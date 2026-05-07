from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Cleared existing data.')

        # Create users (superheroes)
        users_data = [
            {'username': 'ironman', 'email': 'tony.stark@avengers.com', 'password': 'ironman123'},
            {'username': 'spiderman', 'email': 'peter.parker@avengers.com', 'password': 'spiderman123'},
            {'username': 'blackwidow', 'email': 'natasha.romanoff@avengers.com', 'password': 'blackwidow123'},
            {'username': 'superman', 'email': 'clark.kent@dcheroes.com', 'password': 'superman123'},
            {'username': 'wonderwoman', 'email': 'diana.prince@dcheroes.com', 'password': 'wonderwoman123'},
            {'username': 'batman', 'email': 'bruce.wayne@dcheroes.com', 'password': 'batman123'},
        ]
        for data in users_data:
            User(**data).save()
        self.stdout.write(f'Created {len(users_data)} users.')

        # Create teams (Team Marvel and Team DC)
        team_marvel = Team(
            name='Team Marvel',
            members=['ironman', 'spiderman', 'blackwidow']
        )
        team_marvel.save()

        team_dc = Team(
            name='Team DC',
            members=['superman', 'wonderwoman', 'batman']
        )
        team_dc.save()

        self.stdout.write('Created 2 teams: Team Marvel and Team DC.')

        # Create activities
        activities_data = [
            {'username': 'ironman', 'activity_type': 'Running', 'duration': 30.0, 'date': date(2026, 5, 1)},
            {'username': 'spiderman', 'activity_type': 'Web Slinging', 'duration': 45.0, 'date': date(2026, 5, 1)},
            {'username': 'blackwidow', 'activity_type': 'Martial Arts', 'duration': 60.0, 'date': date(2026, 5, 2)},
            {'username': 'superman', 'activity_type': 'Flying', 'duration': 40.0, 'date': date(2026, 5, 2)},
            {'username': 'wonderwoman', 'activity_type': 'Sword Training', 'duration': 50.0, 'date': date(2026, 5, 3)},
            {'username': 'batman', 'activity_type': 'Cape Gliding', 'duration': 35.0, 'date': date(2026, 5, 3)},
        ]
        for data in activities_data:
            Activity(**data).save()
        self.stdout.write(f'Created {len(activities_data)} activities.')

        # Create leaderboard entries
        leaderboard_data = [
            {'username': 'ironman', 'score': 950},
            {'username': 'spiderman', 'score': 870},
            {'username': 'blackwidow', 'score': 920},
            {'username': 'superman', 'score': 990},
            {'username': 'wonderwoman', 'score': 880},
            {'username': 'batman', 'score': 910},
        ]
        for data in leaderboard_data:
            Leaderboard(**data).save()
        self.stdout.write(f'Created {len(leaderboard_data)} leaderboard entries.')

        # Create workouts
        workouts_data = [
            {
                'name': 'Iron Man Strength Training',
                'description': 'High-intensity strength training inspired by Tony Stark.',
                'duration': 45.0,
            },
            {
                'name': 'Spider Agility Circuit',
                'description': 'Agility and flexibility exercises for web-slinging heroes.',
                'duration': 30.0,
            },
            {
                'name': 'Black Widow Combat Conditioning',
                'description': 'Combat conditioning and endurance training.',
                'duration': 60.0,
            },
            {
                'name': 'Superman Cardio Blast',
                'description': 'High-energy cardio workout fit for the Man of Steel.',
                'duration': 40.0,
            },
            {
                'name': 'Wonder Woman Warrior Workout',
                'description': 'Strength and endurance workout inspired by Amazonian warriors.',
                'duration': 55.0,
            },
            {
                'name': 'Batman Dark Knight Training',
                'description': 'Full-body conditioning routine for the Caped Crusader.',
                'duration': 50.0,
            },
        ]
        for data in workouts_data:
            Workout(**data).save()
        self.stdout.write(f'Created {len(workouts_data)} workouts.')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
