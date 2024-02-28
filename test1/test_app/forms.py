from django import forms

from test_app.models import TestModel

class searchForm(forms.Form):
    search_q = forms.CharField(max_length=100)


class testForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = ['name','student_id']
