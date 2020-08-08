from django.shortcuts import render, redirect
from .forms import UserRegisterForm, Feedback
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Policy, Answer

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			# messages.success(request, f'Account for {username} has been created Log In!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html',{'form':form})

@login_required
def home(request):
    if request.user.is_superuser:
        return render(request,'user/dashboard.html')
    else:
        return render(request,'user/home.html',{'questions':Policy.objects.all()})
        
def question_detail(request,ques_pk):
	question = Policy.objects.filter(pk=ques_pk)[0]
	if request.method == 'POST':
		form = Feedback(request.POST)
		if form.is_valid():
			answer = form.cleaned_data['answer']
			gender = form.cleaned_data['gender']
			age = form.cleaned_data['age']
			region = form.cleaned_data['region']

			answer = Answer(question = question, answer = answer,gender = gender, age = age, region=region)
			answer.save()

			return redirect('home')

	else:
		form = Feedback()
	return render(request,'user/question-detail.html',{'form':form,'question':question,'answers':Answer.objects.filter(question = question)})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def create_policy(request):
	return render(request,'user/create-policy.html')