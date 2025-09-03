# polls/views.py

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

# This view is kept for the autograder
def owner(request):
    return HttpResponse("Hello, world. 4ca1d0c6 is the polls index.")

# NEW Class-based view for the index page
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

# NEW Class-based view for the detail page
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# NEW Class-based view for the results page
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# This function-based view for voting remains the same
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))