from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quora_app/question_list.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'quora_app/question_detail.html', {'question': question, 'answers': answers})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'quora_app/ask_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'quora_app/answer_question.html', {'form': form, 'question': question})

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        like.delete()
    return redirect('question_detail', question_id=answer.question.id)
