def find_url(string):
    # findall() has been used  
    # with valid conditions for urls in string 
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 
    
def find_email(string):
    regex = r"[\w\.-]+@[\w\.-]+"
    email = re.findall(regex,string)       
    return email

def find_numbers(string):
   
    regex = r"[-+]?\d*\.?\,?\d+|[-+]?\d+"
    number = re.findall(regex,string)
 
    return number