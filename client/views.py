from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from writer.models import Article

from . models import Subscription

from account.models import CustomUser

# Create your views here.

""" @login_required(login_url='my-login')
def client_dashboard (request):
    
    try:
        subDetails = Subscription.objects.get(user=request.user)
        
        Subscription_plan = subDetails.subscription_plan
        
        context = {'SubPlan' : Subscription_plan}
        
        return render(request, 'client/client-dashboard.html', context)
    
    except:
        
        Subscription_plan = None
        
        context = {'SubPlan' : Subscription_plan}
    
        return render(request, 'client/client-dashboard.html') """

@login_required(login_url='my-login')
def client_dashboard(request):

    try:

        subDetails = Subscription.objects.get(user=request.user)

        subscription_plan = subDetails.subscription_plan

        context = {'SubPlan':subscription_plan}

        return render(request, 'client/client-dashboard.html', context)

    except:

        subscription_plan = "None"

        context = {'SubPlan':subscription_plan}

        return render(request, 'client/client-dashboard.html', context)


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

#Create a subscription view
@login_required(login_url='my-login')
def account_management (request):
    return render (request, 'client/account-management.html')

""" 
@login_required(login_url='my-login')
def create_subscription (request, subID, plan):
    custom_user = CustomUser.object.get(email=request.user)
    firstName = custom_user.first_name
    lastName = custom_user.last_name
    
    fullName = firstName + " " + lastName
    
    selected_sub_plan = plan
    
    if selected_sub_plan == "Standard":
        sub_cost ="4.99"
        
    elif selected_sub_plan == "Premium": 
        sub_cost ="9.99"
        
    subscription = Subscription.objects.create(
    subscriber_name=fullName, subscription_plan=selected_sub_plan,
    subscription_cost=sub_cost, paypal_subscription_id=subID,
    is_active=True, user=request.user)
    
    context = {'SubscriptionPlan': selected_sub_plan}
    
    return render(request, 'client/create_subscription.html', context)"""
    
@login_required(login_url='my-login')
def create_subscription(request, subID, plan):

    custom_user = CustomUser.objects.get(email=request.user)

    if not Subscription.objects.filter(user=request.user).exists():

        firstName = custom_user.first_name
        lastName = custom_user.last_name

        fullName = firstName + " " + lastName

        selected_sub_plan = plan

        if selected_sub_plan == "Standard":

            sub_cost = "4.99"

        elif selected_sub_plan == "Premium":

            sub_cost = "9.99"

        subscription = Subscription.objects.create(
        subscriber_name=fullName, subscription_plan=selected_sub_plan,
        subscription_cost=sub_cost, paypal_subscription_id=subID,
        is_active=True, user=request.user)

        context = {'SubscriptionPlan': selected_sub_plan}

        return render(request, 'client/create-subscription.html', context)