from urllib.parse import urlparse


#get domain name
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''



#Get sub domain name
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

print((get_domain_name('https://mobile.mail.levante.kz/page.php')))
