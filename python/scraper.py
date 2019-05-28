
from requests_html import HTMLSession

def check_google(inp):
    bad = False
    for i in range(len(inp)):
        if inp[i:i+10] == 'google.com':
            bad = True
    return bad

def parse_links(inp):
    search = inp.replace(" ","+")
    googleurl = 'https://www.google.com/search?q='+search+'&rlz=1C1CHBF_enUS850US850&tbm=nws&source=lnt&tbs=qdr:m&sa=X&ved=0ahUKEwjQ3e2horniAhUKxVkKHS_AC34QpwUIIQ&biw=1536&bih=754&dpr=2.5'

    session = HTMLSession()

    r = session.get(googleurl)

    r1 = [i for i in list(r.html.links) if i[0] != '/' and not check_google(i)]

    return r1
