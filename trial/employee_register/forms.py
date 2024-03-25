from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model=Employee
        fields = ('full_name','emp_code','mobile_number','position')
        #this can also be given as
        #fields=('fullname','emp_code','mobile','position')
        labels={
            'full_name':'FullName',
            'emp_code':'EmployeeCode',
        }

        def __init__(self,*args,**kwargs):
            super(EmployeeForm,self).__init__(*args,**kwargs)
            self.fields['position'].empty_label ="SELECT"
            # self.fields['emp_code'].required= False
            #this removes the requirement which is a part of form validation