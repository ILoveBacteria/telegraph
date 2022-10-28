from django import forms
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return mark_safe('\n'.join([f'<div class="invalid-feedback">{e}</div>' for e in self]))


class MyForm(forms.Form):
    def update_validation(self):
        for name, field in self.fields.items():
            if name in self.errors:
                field.widget.attrs.update({'class': 'form-control is-invalid'})
            else:
                field.widget.attrs.update({'class': 'form-control is-valid'})


class LoginForm(MyForm):
    phone = forms.RegexField(
        label='Phone number',
        help_text='912345678',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel'}),
        strip=True,
        regex=r'^9\d{9}$'
    )


class LoginCodeForm(MyForm):
    code = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Code'
    )


class LoginPasswordForm(MyForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )
