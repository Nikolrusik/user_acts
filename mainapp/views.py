from typing import Dict, Any
from django.views.generic import TemplateView
from django.db.models import Avg, Count

from .models import Person


class PersonStat(TemplateView):
    template_name = 'mainapp/stat.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(PersonStat, self).get_context_data(**kwargs)
        person_id = kwargs['pk']
        person = Person.objects.get(id=person_id)
        context['person'] = person
        context['positive_actions'] = person.actions.filter(
            estimation__gt=5).count()
        context['neutral_actions'] = person.actions.filter(
            estimation=5).count()
        context['negative_actions'] = person.actions.filter(
            estimation__lt=5).count()
        context['avg_rating'] = person.actions.aggregate(
            avg_rating=Avg('estimation'))
        return context


class QueryPersons(TemplateView):
    template_name = 'mainapp/query.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(QueryPersons, self).get_context_data(**kwargs)
        context['user_count'] = Person.objects.filter(
            is_married=True,
            is_jobless=None,
            actions__estimation__gt=6,
            address__city='N'
        ).annotate(
            action_count=Count('actions'),
            avg_estimation=Avg('actions__estimation')
        ).values('action_count', 'avg_estimation')
        return context
