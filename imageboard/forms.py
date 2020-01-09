from django.forms import ModelForm, Textarea, CharField, FileField, ClearableFileInput
from django.forms.widgets import HiddenInput
from .models import Thread, Post, FilePost, FileThread


# from captcha.fields import CaptchaField
class ThreadForm(ModelForm):
    # captcha = CaptchaField()
    title = CharField(label=False, widget=Textarea(attrs={'class': 'newthread',
                                                          'placeholder': 'Название треда', 'rows': 1}))
    name = CharField(label=False, widget=Textarea(attrs={'class': 'newthread', 'placeholder': 'Имя',
                                                         'rows': 1, }), max_length=50, initial='Аноним')
    content = CharField(label=False,
                        widget=Textarea(attrs={'rows': 10,
                                               'placeholder': 'Содержимое. Макс. длина 15000',
                                               'class': 'newthread'}), max_length=15000)

    class Meta:
        model = Thread
        fields = ['name', 'title', 'content', 'board']
        widgets = {
            'content': Textarea(attrs={'rows': 10, 'placeholder': 'Содержимое. Макс. длина 15000',
                                       'style': 'background-color: #ccc; fo'}),
            'board': HiddenInput(),
        }


class PostForm(ThreadForm):
    title = None

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'board': HiddenInput(),
            'thread': HiddenInput(),
        }


class PostFileForm(ModelForm):
    file = FileField(required=False, allow_empty_file=False, widget=ClearableFileInput(attrs={'multiple': True}), label=False)

    class Meta:
        widgets = {
            'post': HiddenInput()
        }
        model = FilePost
        fields = '__all__'


class ThreadFileForm(PostFileForm):
    class Meta:
        widgets = {
            'thread': HiddenInput()
        }
        model = FileThread
        fields = '__all__'
