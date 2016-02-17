from django.forms import Form, CharField


class LoginForm(Form):
    username = CharField(label='Username', max_length=50)
    document = CharField(label='Document', max_length=20)
    password = CharField(label='Password', max_length=50)
