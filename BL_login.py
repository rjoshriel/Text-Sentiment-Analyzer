from DAL.DAL_login import DAL_login

class BL_login(object):
    
    def __init__(self):
        #print ("init")
        user = ""
    def check_user(self, uLine):
        found = False
        DA_user = DAL_login()
        user = DA_user.get_user(uLine)
        if user is None:
            return found
        else:
            found = True
            return found
    def add_user(self,uLine):
        DA_user = DAL_login()
        user = DA_user.get_user(uLine)
        if user is None:
            DA_user.add_User(uLine)
        else:
            print("There must be an Error!")
        
        