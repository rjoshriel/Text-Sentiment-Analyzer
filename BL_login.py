from DAL.DAL_login import DAL_login

class BL_login(object):
    
    def __init__(self):
        #print ("init")
        user = ""
    def check_user(self, uLine):
        DA_user = DAL_login()
        user = DA_user.get_user(uLine)
        if user is None:
            return 0
        else:
            return 1
        