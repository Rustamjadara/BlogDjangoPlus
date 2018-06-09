from django import forms
from .models import Post
from pagedown.widgets import PagedownWidget
from datetimewidget.widgets import DateTimeWidget

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget)
	publish = forms.DateTimeField(widget=DateTimeWidget())
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"draft",
			"publish"
		]
		dateTimeOptions = {
		'format': 'dd/mm/yyyy',
		'autoclose': False,
		'showMeridian' : True
		}
		widgets = {
			#NOT Use localization and set a default format
			'datetime': DateTimeWidget(options = dateTimeOptions)
			}