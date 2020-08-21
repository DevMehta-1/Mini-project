import re

def valemail(mail):
    e='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(e,mail):
        return False
    else:
        return True

def valmobile(mob):
    m=re.compile(r'\d{10,12}')
    if re.match(m,str(mob)):
        return False
    else:
        return True
    