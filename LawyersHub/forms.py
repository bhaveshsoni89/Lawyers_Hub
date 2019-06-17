from django import forms


class LawyerForm(forms.Form):
    username = forms.CharField(max_length=20)
    name = forms.CharField(max_length=30)
    gender = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=50)
    mobile = forms.IntegerField()
    password = forms.CharField(max_length=50)
    age = forms.IntegerField()
    exp = forms.IntegerField()
    language = forms.CheckboxSelectMultiple()
    category = forms.CheckboxSelectMultiple()
    picture = forms.FileField()
    degree = forms.FileField()
    certificate = forms.FileField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=50)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=15)
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=250)
    gender = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
    confirm = forms.CharField(max_length=50)


class ContactForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField(max_length=250)
    Subject = forms.CharField(max_length=250)


class TalkForm(forms.Form):
    Area = forms.CharField(max_length=30)
    City = forms.CharField(max_length=30)
    Email = forms.EmailField(max_length=250)
    Subject = forms.CharField(max_length=250)
    Lawyer = forms.CharField()