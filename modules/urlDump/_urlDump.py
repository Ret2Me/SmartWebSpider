from urllib.parse import urlparse
import re 
import requests
import modules.urlDump.config as config

def urlDump(self):
    ac_url = self.targets[0]
    try:
        resp = requests.get(ac_url, verify=False, timeout=5)



        for url in re.findall(r"(?P<url>https?://[^\s]+[\"|\'])", str(resp.content)):
            if url[-1] == "\"":
                url = url[:-1]
            elif url[-1] == "\'":
                url = url[:-1]
            url_domain = urlparse(url).netloc

                
            if ((any((url_domain in target) or (target in url_domain) for target in self.targets) or \
                any((url_domain in target) or (target in url_domain) for target in self.past_websites)) or \
                all(tld not in url_domain for tld in config.TLD)):
                
                continue
            else:
                self.targets.append(urlparse(url).scheme + "://" + urlparse(url).netloc)
    
    except Exception as e:
        print(e)
        pass

