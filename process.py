from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer
import json

def clean_text(text):
	"""
	This function takes as input a text on which several 
	NLTK algorithms will be applied in order to preprocess it
	"""
	tokens = word_tokenize(text)
	# Remove the punctuations
	tokens = [word for word in tokens if word.isalpha()]
	# Lower the tokens
	tokens = [word.lower() for word in tokens]
	# Remove stopword
	tokens = [word for word in tokens if not word in stopwords.words("english")]
	# Lemmatize
	lemma = WordNetLemmatizer()
	tokens = [lemma.lemmatize(word, pos = "v") for word in tokens]
	tokens = [lemma.lemmatize(word, pos = "n") for word in tokens]


	countlookup = {}

	for w in tokens:
		if len(w) == 1:
			continue

		if w not in countlookup:
			countlookup[w] = 0

		countlookup[w]+=1

	return countlookup



da_data = {'d':[],'r':[]}

dems = json.load(open('democrats.json'))

all_tokens = {}
for dem in dems:

	print(dem['date'])
	tokens = clean_text(dem['text'])

	new = {}
	
	for k in tokens:

		

		if k not in all_tokens:
			new[k] = tokens[k]
			all_tokens[k] = tokens[k]

		else:
			all_tokens[k] = all_tokens[k] + tokens[k]

	# what percentage of the words are the new words
	if len(new) == len(tokens):
		new_percent = 100
	else:
		new_percent = int(len(new) / len(tokens) * 100)
	
	new_sorted = sorted(new.items(), key=lambda x: x[1], reverse=True) 
	this_year_sorted = sorted(tokens.items(), key=lambda x: x[1], reverse=True) 

	url = f'https://www.presidency.ucsb.edu/documents/{dem["date"].split(",")[1].strip()}-democratic-party-platform'

	da_data['d'].append({'date': dem['date'].strip(), 'url':url, 'year':int(dem['date'].split(',')[1].strip()), 'newPercent': new_percent, 'new':new_sorted[0:10],'top':this_year_sorted[0:10]})





json.dump(da_data,open('top.json','w'))


repubs = json.load(open('republicans.json'))

all_tokens = {}
for repub in repubs:

	print(repub['date'])
	tokens = clean_text(repub['text'])

	new = {}
	

	for k in tokens:
		if k not in all_tokens:
			new[k] = tokens[k]
			all_tokens[k] = tokens[k]

		else:
			
			all_tokens[k] = all_tokens[k] + tokens[k]

	# what percentage of the words are the new words
	if len(new) == len(tokens):
		new_percent = 100
	else:
		new_percent = int(len(new) / len(tokens) * 100)
	
	new_sorted = sorted(new.items(), key=lambda x: x[1], reverse=True) 
	this_year_sorted = sorted(tokens.items(), key=lambda x: x[1], reverse=True) 

	rep = int(repub["date"].split(",")[1].strip())


	url = f'https://www.presidency.ucsb.edu/documents/republican-party-platform-{rep}'

	if rep == 2020:
		url = 'https://www.presidency.ucsb.edu/documents/resolution-regarding-the-republican-party-platform'
	elif rep > 1996:
		url = f'https://www.presidency.ucsb.edu/documents/{rep}-republican-party-platform'		

	da_data['r'].append({'date': repub['date'].strip(), 'url':url, 'year':rep, 'newPercent': new_percent,'new':new_sorted[0:10],'top':this_year_sorted[0:10]})

json.dump(da_data,open('top.json','w'))
print(da_data)