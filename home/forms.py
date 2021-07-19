from django import forms


QUERIES = (
    ('', 'Select Option'),
    ('Best Comics to start with', 'Best Comics to start with'),
    ('Order and shipping details', 'Order and shipping details'),
    ('I want a comic added to the shop', 'I want a comic added to the shop'),
    ('Something strange', 'Something strange'),
)


class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Full Name', max_length=100,
                                   widget=forms.TextInput())
    contact_email = forms.EmailField(label='Email Address',
                                     widget=forms.TextInput())
    query = forms.ChoiceField(label='What does your question relate to?',
                              choices=QUERIES)
    message = forms.CharField(label='What is your message?',
                              widget=forms.Textarea(
                                  attrs={'style': 'height:6em'}))
