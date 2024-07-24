from . models import Article

from account.models import CustomUser #how to import from another app

from django.forms import ModelForm


class ArticleForm(ModelForm):
    
    class Meta:
        
        model = Article
        fields = ['title', 'content', "is_premium",]
        
        

#Add form for profile updates
class UpdateUserForm(ModelForm):
    
    password = None
    
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name',]
        exclude = ['password1', 'password2',]