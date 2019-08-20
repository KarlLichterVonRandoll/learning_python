from django import forms


class MyRegForm(forms.Form):
    username = forms.CharField()
    # age = forms.IntegerField()
    password = forms.CharField(label='密码')
    password2 = forms.CharField(label='密码(重复)')

    def clean_username(self):
        """此方法限定username必须大于等于6个字符"""
        uname = self.cleaned_data['username']
        if len(uname) < 6:
            raise forms.ValidationError('用户名太短')
        return uname

    def clean(self):
        passwd1 = self.cleaned_data['password']
        passwd2 = self.cleaned_data['password2']
        if passwd1 != passwd2:
            raise forms.ValidationError('密码不一致')
        return self.cleaned_data
