from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Tests, Categories, Questions, Answers, Result
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import RegistrationForm, LoginForm, ResultForm
# from .serializers import ResultSerializer
from rest_framework import generics

from polls.api.serializers import ResultSerializer

def index(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            login(request, user)
            print('is_anon', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            print(user)
            return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'polls/index.html', {'form': form})
    # return render(request, 'polls/index.html')

# @permission_required('polls.show_categories')
@login_required()
def show_categories(request):
    categories = Categories.objects.filter(exist=True)
    context = {'categories': categories}
    return render(request, context=context, template_name='polls/show_categories.html')

def show_tests(request, category_id):
    tests = Tests.objects.filter(category_id=category_id, exist=True)
    context = {'tests': tests}
    return render(request, context=context, template_name='polls/show_tests.html')

def go_test(request, test_id):
    if request.method == 'POST':
        l = request.POST
        ll = dict(l)
        r = []
        for x in ll:
            r.append(x)

        del r[0]

        r = list(map(int, r))

        answers_list = Answers.objects.all()

        t = 0
        f = 0
        a = 0
        for an_list in answers_list:
            for l in r:
                if l == an_list.pk:
                    if an_list.exist == True:
                        t += 1
                        a += 1
                    else:
                        f += 1
                        a += 1


        res_a = a / 100
        res = round(t / res_a)

        Result.objects.create(
            UserName=request.user,
            Rating=res
        )

        context = {'r': r,
                   't': t,
                   'f': f,
                   'a': a,
                   'res': res,
                   'answers_list': answers_list}

        return render(request, context=context, template_name='polls/results_polls.html')
    else:
        test = Tests.objects.get(pk=test_id)

        question = Questions.objects.filter(test_id=test_id)
        answers = Answers.objects.all()

        context = {'question': question, 'test': test, 'answers': answers}

        return render(request, context=context, template_name='polls/go_test.html')

def results_test(request):
        results = Result.objects.all()
        context = {'results': results}
        return render(request, context=context, template_name='polls/show_results.html')

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'polls/auth/registration.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')

class ResultListView(generics.ListAPIView):
 queryset = Result.objects.all()
 serializer_class = ResultSerializer
class ResultDetailView(generics.RetrieveAPIView):
 queryset = Result.objects.all()
 serializer_class = ResultSerializer