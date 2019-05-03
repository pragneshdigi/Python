from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from votings.models import Choice, Question

def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'votings/index.html', context)
    #output = '-----'.join([s.question_text for s in question_list])
    #return HttpResponse(output)
    #return HttpResponse("Wow! Writing First Web App In Django!")

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'votings/detail.html', {'question': question})
    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'votings/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'votings/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('votings:results', args=(question.id,)))
    #return HttpResponse("You're voting on question %s." % question_id)


    