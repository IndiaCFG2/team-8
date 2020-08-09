from django.db import models

# Create your models here.
class Policy(models.Model):
    name = models.CharField(max_length=120)
    summary = models.TextField()
    # answer = models.TextField()
    def __str__(self):
        return self.name

GENDER_CHOICES = (
    ("male","male"),
    ("female","female"),
    ("other","other")
)

STATE_CHOICE = (
    ("Andhra","Andhra"),
    ("Telangana","Telangana"),
    ("West Bengal","West Bengal"),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Goa","Goa"),
    ("Chattisghar","Chattisghar"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("J & K","J & K"),
    ("Jharkhand","Jharkhand"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Kerala","Kerala"),

)

ANSWER_CHOICE = (
    ("Yes","Yes"),
    ("No","No"),
    ("Neutral","Neutral"),

)

TRANSLATION_OPTIONS = (
    ("af", "afrikaans"),
    ("sq", "albanian"),
    ("am", "amharic"),
    ("ar", "arabic"),
    ("hy", "armenian"),
    ("az", "azerbaijani"),
    ("eu", "basque"),
    ("be", "belarusian"),
    ("bn", "bengali"),
    ("bs", "bosnian"),
    ("bg", "bulgarian"),
    ("ca", "catalan"),
    ("ceb", "cebuano"),
    ("ny", "chichewa"),
    ("co", "corsican"),
    ("hr", "croatian"),
    ("cs", "czech"),
    ("da", "danish"),
    ("nl", "dutch"),
    ("en", "english"),
    ("eo", "esperanto"),
    ("et", "estonian"),
    ("tl", "filipino"),
    ("fi", "finnish"),
    ("fr", "french"),
    ("fy", "frisian"),
    ("gl", "galician"),
    ("ka", "georgian"),
    ("de", "german"),
    ("el", "greek"),
    ("gu", "gujarati"),
    ("ha", "hausa"),
    ("haw", "hawaiian"),
    ("iw", "hebrew"),
    ("hi", "hindi"),
    ("hmn", "hmong"),
    ("hu", "hungarian"),
    ("is", "icelandic"),
    ("ig", "igbo"),
    ("id", "indonesian"),
    ("ga", "irish"),
    ("it", "italian"),
    ("ja", "japanese"),
    ("jw", "javanese"),
    ("kn", "kannada"),
    ("kk", "kazakh"),
    ("km", "khmer"),
    ("ko", "korean"),
    ("ky", "kyrgyz"),
    ("lo", "lao"),
    ("la", "latin"),
    ("lv", "latvian"),
    ("lt", "lithuanian"),
    ("lb", "luxembourgish"),
    ("mk", "macedonian"),
    ("mg", "malagasy"),
    ("ms", "malay"),
    ("ml", "malayalam"),
    ("mt", "maltese"),
    ("mi", "maori"),
    ("mr", "marathi"),
    ("mn", "mongolian"),
    ("ne", "nepali"),
    ("no", "norwegian"),
    ("ps", "pashto"),
    ("fa", "persian"),
    ("pl", "polish"),
    ("pt", "portuguese"),
    ("pa", "punjabi"),
    ("ro", "romanian"),
    ("ru", "russian"),
    ("sm", "samoan"),
    ("st", "sesotho"),
    ("sn", "shona"),
    ("sd", "sindhi"),
    ("si", "sinhala"),
    ("sk", "slovak"),
    ("sl", "slovenian"),
    ("so", "somali"),
    ("es", "spanish"),
    ("su", "sundanese"),
    ("sw", "swahili"),
    ("sv", "swedish"),
    ("tg", "tajik"),
    ("ta", "tamil"),
    ("te", "telugu"),
    ("th", "thai"),
    ("tr", "turkish"),
    ("uk", "ukrainian"),
    ("ur", "urdu"),
    ("uz", "uzbek"),
    ("vi", "vietnamese"),
    ("cy", "welsh"),
    ("xh", "xhosa"),
    ("yi", "yiddish"),
    ("yo", "yoruba"),
    ("zu", "zulu"),
    ("fil", "Filipino"),
    ("he", "Hebrew"),
)

class Answer(models.Model):
    question = models.ForeignKey(Policy, on_delete=models.CASCADE)
    comment_language = models.CharField(max_length=30,choices=TRANSLATION_OPTIONS,default="en")
    comment = models.TextField(blank=True)
    answer = models.CharField(max_length=10,choices=ANSWER_CHOICE,default="Yes")
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default="male")
    age = models.IntegerField(default=18)
    region = models.CharField(max_length= 30,choices = STATE_CHOICE,default="Telangana")
    def __str__(self):
        return self.answer