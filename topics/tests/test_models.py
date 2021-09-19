from django.test import TestCase
from topics.models import Topic
from django.core.exceptions import ValidationError

class AnimalTestCase(TestCase):
    def setUp(self):
        Topic.objects.create(name="topic1")
        Topic.objects.create(name="topic2")

    def test_topic_name(self):
        topic1 = Topic.objects.get(name="topic1")
        topic2 = Topic.objects.get(name="topic2")
        self.assertEqual(topic1.name, 'topic1')
        self.assertEqual(topic2.name, 'topic2')
    
    def test_topic_regex_name(self):
        regix = Topic(name = "hello world")
        with self.assertRaisesMessage(
                ValidationError,
                'Invalide topic name'
        ):
            regix.save()