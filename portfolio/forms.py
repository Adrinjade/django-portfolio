from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(label='Your email')
    message = forms.CharField(widget=forms.Textarea, label='Message')
