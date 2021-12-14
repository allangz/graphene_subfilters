import graphene
from graphene_django import DjangoObjectType
from .models import Question, Choice, SubChoice


class SubChoiceType(DjangoObjectType):
    class Meta:
        model = SubChoice
        fields = "__all__"


class ChoiceType(DjangoObjectType):
    sub_choices = graphene.List(SubChoiceType, search_sub_choices=graphene.String(), order_by=graphene.String())

    class Meta:
        model = Choice
        fields = ("id", "choice_text", "question")

    def resolve_sub_choices(self, info, search_sub_choices=None,  order_by=None):
        qs = self.subchoice_set.all()
        if search_sub_choices:
            return qs.filter(sub_choice_text__icontains=search_sub_choices)
        if order_by:
            qs = qs.order_by(order_by)

        return qs


class QuestionType(DjangoObjectType):
    choices = graphene.List(ChoiceType, search_choices=graphene.String(), order_by=graphene.String())
    is_old = graphene.Boolean(default_value=False)

    class Meta:
        model = Question
        fields = ("id", "question_text", "pub_date")

    def resolve_is_old(self, info):
        res = False
        if self.id % 2 == 0:
            res = True
        return res

    def resolve_choices(self, info, search_choices=None, order_by=None):
        qs = self.choice_set.all()
        if search_choices:
            qs = qs.filter(choice_text__icontains=search_choices)
        if order_by:
            qs = qs.order_by(order_by)

        return qs


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
