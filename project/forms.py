from django import forms
import datetime

class LoginForm(forms.Form):
	username = forms.CharField(max_length=40)
	password = forms.CharField(widget=forms.PasswordInput())

class PromotionForm(forms.Form):
	mon = forms.BooleanField(required=False)
	tue = forms.BooleanField(required=False)
	wed = forms.BooleanField(required=False)
	thu = forms.BooleanField(required=False)
	fri = forms.BooleanField(required=False)
	sat = forms.BooleanField(required=False)
	sun = forms.BooleanField(required=False)
	min_num = forms.DecimalField()
	max_num = forms.DecimalField()
	expires = forms.DateField(initial=datetime.date.today)
	expires.widget.attrs.update(attrs={'class': 'form-contrl'})
	desc = forms.CharField(widget=forms.Textarea({'class': 'form-control'}))

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=40)
	establishment = forms.CharField(max_length=40)
	password = forms.CharField(widget=forms.PasswordInput())

