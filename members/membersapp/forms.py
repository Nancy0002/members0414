from django import forms

class PostForm(forms.Form):
	Name = forms.CharField(max_length=20,initial='')
	Sex = forms.CharField(max_length=2,initial='M')	
	Birthday = forms.DateField()
	Email = forms.EmailField(max_length=100,initial='',required=False)
	Phone = forms.CharField(max_length=50,initial='',required=False)
	Addr = forms.CharField(max_length=255,initial='',required=False)
