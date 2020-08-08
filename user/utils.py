from better_profanity import profanity
from summarizer import Summarizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

def profanity_filter(text):
    profanity.load_censor_words()
    censored_text = profanity.censor(text)
    return censored_text

def analysis_text(text):
    lines_list = tokenize.sent_tokenize(text)
    sid = SentimentIntensityAnalyzer()
    main_list = []
    for sentence in lines_list:
        ss = sid.polarity_scores(sentence)
        list = []
        for k in sorted(ss):
            list.append(ss[k])
        main_list.append(list)
    x = [i[1] for i in main_list]
    x = sum(x)/len(x)
    return x

def summarize_text(text):
    model = Summarizer()
    result = model(body, min_length=60, ratio=0.1)
    full = ''.join(result)
    return full
