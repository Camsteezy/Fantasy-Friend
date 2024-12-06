from yahoo_oauth import OAuth2
import yahoo_fantasy_api as FantasyFriend

#connect to yahoo api
sc = OAuth2( None ,None, from_files= 'oauth2.json') 

if not oauth.token_is_valid():
    oauth.refresh_access_token()
#python3.13 Oauth2.py