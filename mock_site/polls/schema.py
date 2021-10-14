import graphene
from graphene_django import DjangoObjectType
from .models import Question, Choice, SubChoice


class SubChoiceType(DjangoObjectType):
    class Meta:
        model = SubChoice
        fields = "__all__"


class ChoiceType(DjangoObjectType):
    sub_choices = graphene.List(SubChoiceType, search_sub_choices=graphene.String())

    class Meta:
        model = Choice
        fields = ("id", "choice_text", "question")

    def resolve_sub_choices(self, info, search_sub_choices=None):
        if search_sub_choices:
            return self.subchoice_set.filter(sub_choice_text__icontains=search_sub_choices)

        return self.subchoice_set.all()


class QuestionType(DjangoObjectType):
    choices = graphene.List(ChoiceType, search_choices=graphene.String())

    class Meta:
        model = Question
        fields = ("id", "question_text")

    def resolve_choices(self, info, search_choices=None):
        if search_choices:
            return self.choice_set.filter(choice_text__icontains=search_choices)

        return self.choice_set.all()


class Query(graphene.ObjectType):
    all_questions = graphene.List(QuestionType, search_text=graphene.String())
    all_choices = graphene.List(ChoiceType, search_text=graphene.String())
    all_sub_choices = graphene.List(SubChoiceType)

    def resolve_all_questions(self, info, search_text=None):
        qs = Question.objects.all()
        if search_text:
            qs = qs.filter(question_text__icontains=search_text)

        return qs

    def resolve_all_choices(self, info, search_text=None):
        qs = Choice.objects.all()
        if search_text:
            qs = qs.filter(choice_text__icontains=search_text)

        return qs

    def resolve_all_sub_choices(self, info):
        qs = SubChoice.objects.all()
        return qs


schema = graphene.Schema(query=Query)
