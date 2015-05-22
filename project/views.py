from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from forms import LoginForm, PromotionForm, SignUpForm
import requests
import json

API_ENDPOINT = "http://idrivedjango-env-qrs5vkxvvi.elasticbeanstalk.com/api"

def home(request):
	return render_to_response('home.html', {}, RequestContext(request))

def business(request):
	return render_to_response('business.html', {}, RequestContext(request))

def promotions(request):
	url = API_ENDPOINT + '/promotion/'
	res = requests.get(url)
	promotionData = res.json()
	promotionData = promotionData[::-1]
	url = API_ENDPOINT + '/baruser/'
	res = requests.get(url)
	barData = res.json()
	barMap = dict()
	for bar in barData:
		barMap[bar['id']] = bar['description']

	promotionData = promotionData[0:10]
	for p in promotionData:
		p['bar_name'] = barMap[p['bar']]
	return render_to_response('promotions.html', {'data': promotionData}, RequestContext(request))

def create_promotion(request):
	if request.method == 'POST':
		form = PromotionForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			url = API_ENDPOINT + '/promotion/'
			header = {'content-type': 'application/json'}
			payload = dict()
			payload['active_monday'] = formData['mon']
			payload['active_tuesday'] = formData['tue']
			payload['active_wednesday'] = formData['wed']
			payload['active_thursday'] = formData['thu']
			payload['active_friday'] = formData['fri']
			payload['active_saturday'] = formData['sat']
			payload['active_sunday'] = formData['sun']
			payload['expire_date'] = str(formData['expires'])
			payload['description'] = formData['desc']
			payload['bar'] = request.session['bar_id']
			payload['min_amount'] = str(formData['min_num'])
			payload['max_amount'] = str(formData['max_num'])
			res = requests.post(url, data=json.dumps(payload), headers = header)
			return redirect('current_promotions')
	else:
		form = PromotionForm()
	return render_to_response('create_promotion.html', {'form': form}, RequestContext(request))

def current_promotions(request):
	url = API_ENDPOINT + '/promotion/'
	res = requests.get(url)
	data = res.json()
	bar_id = request.session['bar_id'] 
	data = filter(lambda d: d['bar'] == bar_id, data)
	return render_to_response('current_promotions.html', {'promotions': data}, RequestContext(request))

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			return redirect('create_promotion')
	else:
		form = LoginForm()
	return render_to_response('login.html', {'form': form}, RequestContext(request))

def logout(request):
	request.session["signed_in"] = False
	return redirect("home")

def sign_up(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			url = API_ENDPOINT + '/baruser/'
			header = {'content-type': 'application/json'}
			payload = {'description': formData['establishment'], 'geo_lat': '13', 'geo_long': '34'}
			res = requests.post(url, data=json.dumps(payload), headers = header)
			data = res.json()
			request.session["signed_in"] = True;
			request.session["bar_id"] = data['id']
			return redirect('current_promotions')
	else:
		form = SignUpForm()
	return render_to_response('sign_up.html', {'form': form}, RequestContext(request))


