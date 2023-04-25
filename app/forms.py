from django import forms


def check_for_r(value):
    if value[0].upper()=='r':
        raise forms.ValidationError('name should not start with r')



# def check_for_len(value):
#     if len(value)<5:
#         raise forms.ValidationError('value must be lesser than 5 vlaues')



def check_for_length(value):
    if len(value)<5:
        raise forms.ValidationError('value must be greater than 8 values')


class Studentform(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_r])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('not matched')
        
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot')
        
        
    
