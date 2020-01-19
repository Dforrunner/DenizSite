from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'id': 'name'}))
    email = forms.EmailField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                           'id': 'email'}))
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'id': 'subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control md-textarea',
                                                           'id': 'message',
                                                           'rows': 2}))
