from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Game

class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Game.objects.create(name='Elden Ring', owner=testuser1, description='Prepare to die.....alot.')
        test_thing.save()

    def test_things_model(self):
        game = Game.objects.get(id=1)
        actual_owner = str(game.owner)
        actual_name = str(game.name)
        actual_description = str(game.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'Elden Ring')
        self.assertEqual(actual_description,'Prepare to die.....alot.')
