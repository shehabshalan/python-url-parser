import sys
url = sys.argv[1]


def urlParser(url):
    dic = {}
    findprotocol = url.find("://")
    scheme = url[:findprotocol]
    dic['Scheme/Protocol'] = scheme
    if '://' in url:
        hostName = url.split('://', 1)[1]
        if ':' in hostName:
            temp = hostName.split(':', 1)[0]
            hostName = temp
        elif '/' in hostName:
            temp2 = hostName.split('/', 1)[0]
            hostName = temp2
        dic['Host name'] = hostName

# subdomain
    if '://' in url:
        subdomain = url.split('://', 1)[1]
        if '/' in subdomain:
            subdomain = subdomain.split('/')[0]
            if '.' in subdomain:
                subdomain = subdomain.split('.')
                if len(subdomain) > 3:
                    subdomain = subdomain[0]+"."+subdomain[1]
                elif len(subdomain) == 3:
                    subdomain = subdomain[0]
                elif len(subdomain) < 3:
                    subdomain = ''
        elif '@' in subdomain:
            subdomain = subdomain.split('@')[1]
            if '.' in subdomain:
                subdomain = subdomain.split('.')[0]
            print(subdomain)
        elif '.' in subdomain:
            subdomain = ''
        dic['Subdomain'] = subdomain


# domain
    if '://' in url:
        domain = url.split('://', 1)[1]
        if ':' in domain:
            domain = domain.split(':')[0]
            if '.' in domain:
                domain = domain.split('.')
                if len(domain) > 3:
                    domain = domain[2]+"."+domain[3]
                else:
                    domain = domain[1]+"."+domain[2]

        elif '/' in domain:
            domain = domain.split('/')[0]
            if '.' in domain:
                domain = domain.split('.')
                if len(domain) > 2:
                    domain = domain[1] + "."+domain[2]
                else:
                    domain = domain[0] + "."+domain[1]
        elif '.' in domain:
            domain = domain.split('.')
            if len(domain) > 2:
                domain = domain[2]+"."+domain[3]
            else:
                domain = domain[0]+"."+domain[1]
        dic['Domain'] = domain
    # TLD
    if '/' in url:
        tld = url.split('/')[2]
        if '.' in tld:
            temp = tld.split('.')
            if len(temp) == 4:
                if ':' in temp[3]:
                    temp2 = temp[3].split(':')[0]
                    tld = temp2
                elif '/' in temp[3]:
                    temp2 = temp.split('/')[0]
                    tld = temp2
                else:
                    tld = temp[3]
            else:
                if '.' in tld:
                    tld = tld.split('.')
                    if len(tld) == 3:
                        tld = tld[2]
                        if ':' in tld:
                            tld = tld.split(':')[0]
                    else:
                        tld = tld[1]
        dic['TLD'] = tld

    if ':' in url:
        temp = url.split(':', 2)
        if len(temp) > 2:
            port = url.split(':', 2)[2]
            if '/' in port:
                temp = port.split('/', 1)[0]
                port = temp
                dic['Port'] = port

    if '?' in url:
        query = url.split('?', 1)[1]
        if '#' in query:
            temp = query.split('#', 1)[0]
            query = temp
        dic['Query String'] = query

    if '#' in url:
        frag = "#"+url.split('#', 1)[1]
        if '/' in frag:
            frag = ''
        dic['Fragment ID'] = frag
    # FULL PATH
    if '/' in url:
        temp = url.split('/', 3)
        if len(temp) > 3:
            fullPath = "/" + url.split('/', 3)[3]
            dic['Full path of resources'] = fullPath

    return dic


urlparser = urlParser(url)
print(urlparser)
