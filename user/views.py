from django.shortcuts import render, redirect
from .forms import UserRegisterForm, Feedback, CreatePolicy
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Policy, Answer
from googletrans import Translator
from .utils import *
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

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
	translator = Translator()
	# responses = Policy.objects.filter(answer__question_id=ques_pk)
	question = Policy.objects.filter(pk=ques_pk)[0]
	# policy = Policy.objects.filter(pk = ques_pk)[0]
	# responses = Answer.objects.filter()
	# responses = policy.object.filter(answer_set=ques_pk)
	# responses = policy.answers_set.all()
	male = 0
	female = 0
	other = 0

# <<<<<<< HEAD
	male_yes = 0
	male_no = 0
	female_yes = 0
	female_no = 0
	other_yes = 0
	other_no=0

	male_neutral = 0
	female_neutral = 0
	other_neutral = 0


	yes=0
	no=0
	neutral=0
	# male_neutral = 0
	responses = Answer.objects.filter(question = question)
	answers = Answer.objects.filter(question = question)
	print(responses)
	commentList = []
	sentimentsList = []
	for _ in answers:
		if (_.comment_language == 'en'):
			commentList.append(_.comment)
		else:
			result = translator.translate(_.comment, src=_.comment_language, dest='en')
			commentList.append(result.text)
	for i in commentList:
		result1 = profanity_filter(i)
		# result2 = analysis_text(i)
	corpus = "".join(commentList)
	corpus = corpus.replace('\n', '')
	corpus = corpus.replace('\r', '')
	# print(corpus,commentList)
	summary = summarize_text(corpus)
	text_tokens = word_tokenize(corpus)
	tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
	corpus = ''.join(tokens_without_sw)
	print(summary)
	# summary = "This is Bharadwaj Bharadwaj is this this isi is is this is"

	for i in responses:
		if i.answer == 'No':
			no+=1
			if i.gender == 'male':
				male_no +=1
			elif i.gender == 'female':
				female_no +=1
			else:
				other_no += 1
		elif i.answer == 'Neutral':
			neutral +=1
			if i.gender == 'male':
				male_neutral +=1
			elif i.gender == 'female':
				female_neutral +=1
			else:
				other_neutral += 1

		else:
			yes+=1
			if i.gender == 'male':
				male_yes +=1
			elif i.gender == 'female':
				female_yes +=1
			else:
				other_yes +=1

	labels=[]
	data=[]
	labelsyes=[]
	datayes=[]
	labelsno=[]
	datano=[]
	labelsneutral=[]
	dataneutral=[]

	labelsyes.append('Male')
	labelsyes.append('Female')
	labelsyes.append('Other')

	datayes.append(male_yes)
	datayes.append(female_yes)
	datayes.append(other_yes)

	labelsno.append('Male')
	labelsno.append('Female')
	labelsno.append('Other')

	datano.append(male_no)
	datano.append(female_no)
	datano.append(other_no)

	labelsneutral.append('Male')
	labelsneutral.append('Female')
	labelsneutral.append('Other')

	dataneutral.append(male_neutral)
	dataneutral.append(female_neutral)
	dataneutral.append(other_neutral)


	labels.append('Satisfied')
	labels.append('Not Satisfied')
	labels.append('Neutral')
	data.append(yes)
	data.append(no)
	data.append(neutral)

	return render(request,'user/admin-ques-detail.html',{'labels':labels,'data':data, 'labelsneutral':labelsneutral,'dataneutral':dataneutral,'labelsyes':labelsyes,'datayes':datayes,'labelsno':labelsno,'datano':datano,'question':question,'summary':summary, "corpus":corpus,'answers':answers})
# =======
# 	# male_yes = 0
# 	# male_no = 0
# 	# female_yes = 0
# 	# female_no = 0
# 	# male_neutral = 0

# 	for i in answers:
# 		if i.gender == 'male':
# 			male +=1
# 		elif i.gender == 'female':
# 			female +=1
# 		else :
# 			other +=1


	# return render(request,'user/test.html',{'male':male,'female':female,'other':other,'summary':summary,'question':question,'answers':answers})
# >>>>>>> 65d289e20a8c2fa8ba847f11ed13a36ce61f6473
