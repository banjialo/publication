
import requests
import json

from . models import Subscription


#Get access token from PayPal's API
def get_access_token ():
    
    data = {'grant_type' : 'client_credentials'}
    
    headers = {'Accept' : 'application/json', 'Accept-Language' : 'en_US'}
    
    client_id = 'AZGBZuEnLVibql2s8X_fzU0GVWLaVSkO4poVJhHGIRLA9l902ZUrew3K0vDNw7TLcAQ7r8ooDruxGZvF'
    
    secret_id = 'EGDx-HvA0A41vsflS-9vWblGonPZJsShBlqP5NXAMO0OOpWrfSkZxUcr9_TGKGIJpTDN5YMtrFHa19u_'
    
    url = 'https://api.sandbox.paypal.com/v1/oauth2/token'
    
    r = requests.post (url, 
                       auth = (client_id, secret_id), 
                       headers = headers,
                       data = data
                       ).json()
    
    access_token = r['access_token']
    
    return access_token
    
    
#Cancel subscription
def cancel_subscription_paypal(access_token, subID):
    
    bearer_token = 'Bearer ' + access_token
    
    headers = {
        
        'Content-Type' : 'application/json',
        'Authorization' :  bearer_token
        
    }
    
    url = 'https://api.sandbox.paypal.com/v1/billing/subscriptions/' + subID + '/cancel'
    
    r = requests.post (url, headers = headers)
    
    print(r.status_code)
    
    
    








































