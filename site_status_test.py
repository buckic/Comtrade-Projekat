import requests
import constants



def is_site_online(siteUrl):
    response = requests.get(siteUrl, timeout=10)
    if(response.status_code==200):
        return True
    else:
        return False

if is_site_online(constants.BASE_URL):
    print('Website je online')
else:
    print('Website nije online')


if is_site_online(f"{constants.BASE_URL}{constants.LOGIN_PAGE}"):
    print('Login stranica je online')
else:
    print('Login stranica nije online')