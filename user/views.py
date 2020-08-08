from django.shortcuts import render, redirect
from .forms import UserRegisterForm, Feedback, CreatePolicy
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
        return render(request,'user/dashboard.html',{'questions':Policy.objects.all()})
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

	if request.method == 'POST':
		form = CreatePolicy(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			summary = form.cleaned_data['summary']
			policy = Policy(name = name, summary=summary)
			policy.save()

			return redirect('home')

	else:
		form = CreatePolicy()
	return render(request,'user/create-policy.html',{'form':form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_ques_detail(request,ques_pk):
	# responses = Policy.objects.filter(answer__question_id=ques_pk)
	question = Policy.objects.filter(pk=ques_pk)[0]
	# policy = Policy.objects.filter(pk = ques_pk)[0]
	# responses = Answer.objects.filter()
	# responses = policy.object.filter(answer_set=ques_pk)
	# responses = policy.answers_set.all()
	male = 0
	female = 0
	other = 0

	# male_yes = 0
	# male_no = 0
	# female_yes = 0
	# female_no = 0
	# male_neutral = 0 
	answers = Answer.objects.filter(question = question)
	for i in answers:
		if i.gender == 'male':
			male +=1
		elif i.gender == 'female':
			female +=1
		else :
			other +=1


	return render(request,'user/admin-ques-detail.html',{'male':male,'female':female,'other':other})
