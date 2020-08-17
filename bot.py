import random
import nltk
#import inte

text = ''
intent = ''

BOT_CONFIG = {
	'intents': {
		'hello': {
			'examples' : ['Привет', 'Добрый день!', 'Шалом'],
			'responses' : ['Привет, человек', 'Добрый времени суток!'],
		},
		'bye': {
			'examples' : ['Пока', 'Досвидания', 'Прощай'],
			'responses' : ['Всего доброго!', 'Счастливо!'],
		},
		'thanks': {
			'examples' : ['Спасибо', 'Спасибо большое', 'Сенкс', 'Благодарю'],
			'responses' : ['Вам спасибо!'],
		},
		'whatcanyoudo': {
			'examples' : ['Что ты умеешь?', 'Расскажи, что умеешь'],
			'responses' : ['Отвечать на вопросы. Просто напиши :)'],
		},
		'name': {
			'examples' : ['Как тебя зовут?', 'Твое имя?'],
			'responses' : ['Меня зовут Бот. Просто Бот.'],
		},
		'weather': {
			'examples' : ['Какая погода в Москве?', 'Какая погода?'],
			'responses' : ['Погода так себе...'],
		},
	},
	'failure_phrase': [
	'Я вас не поняла',
	'Перефразируйте? пожалуйста',
	'Я не знаю, что ответить']
}

def get_intent(text):
	for intent, intent_data in BOT_CONFIG['intents'].items():
		for exaple in intent_data['examples']:
			#print('\t', exaple)
			edit_distance = nltk.edit_distance(text.lower(), exaple.lower())
			#print('\t', exaple, edit_distance)
			if edit_distance / len(exaple) < 0.40:
				return intent

def get_response_by_intent(intent):
	pharases = BOT_CONFIG['intents'][intent]['responses']
	return random.choice(pharases)

def get_generative_response(text):
	return

def get_philure_phrase():
	pharases = BOT_CONFIG['failure_phrase']
	return random.choice(pharases)

def go_bot(text):
	"""Генерация реплик"""
	# NLU
	intent = get_intent(text)

	# Generate answer

	# reles
	if intent:
		return get_response_by_intent(intent)

	# use generative model
	response = get_generative_response(text)
	if response:
		return response

	# stub
	return get_philure_phrase()	

while intent != 'bye': 
	text = input()
	response = go_bot(text)
	intent = get_intent(text)
	print(response)	