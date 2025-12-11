from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
        Activity.objects.create(user=user, type='Running', duration=30)
        Leaderboard.objects.create(user=user, points=100)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team_creation(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard_creation(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
