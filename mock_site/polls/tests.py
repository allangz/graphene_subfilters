from django.test import TestCase
from polls.models import Question
import datetime


class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="Question", pub_date=datetime.datetime.now())

    def test_question_name(self):
        """Test question name"""
        question = Question.objects.get(question_text="Question")
        self.assertEqual(str(question), 'Question')
