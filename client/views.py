from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from writer.models import Article

from .models import Subscription

# Create your views here.

@login_required(login_url='my-login')
def client_dashboard (request):
    
    try:
        subDetails = Subscription.objects.get(user=request.user)
        
        Subscription_plan = subDetails.subscription_plan
        
        context = {'SubPlan' : Subscription_plan}
        
        return render(request, 'client/client-dashboard.html', context)
    
    except:
        
        Subscription_plan = "None"
        
        context = {'SubPlan' : Subscription_plan}
    
        return render(request, 'client/client-dashboard.html')


@login_required(login_url='my-login')
def browse_articles (request):
    
    try:        
        subDetails = Subscription.objects.get(user=request.user, is_active=True)
        
    except:
        return render (request, 'client/subscription-locked.html')
    
    #id eevrything works fine in the try statement, do this:
    current_subscription_plan = subDetails.subscription_plan
    
    if current_subscription_plan == 'Standard':
        articles = Article.objects.all().filter(is_premium=False)
        
    elif current_subscription_plan == 'Premium':
        articles = Article.objects.all ()
        
    context = {'AllClientArticles' : articles}
    
    return render (request, 'client/browse-articles.html', context )


@login_required(login_url='my-login')
def subscription_locked (request):
    return render (request, 'client/subscription-locked.html')

@login_required(login_url='my-login')
def subscription_plans (request):
    return render (request, 'client/subscription-plans.html')