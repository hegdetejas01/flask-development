import json

class Database:
    
    def __init__(self):
        pass

    def checkUserPresence(self, email):
        dbLoc = "E:/flask-development/nlpapp/db.json"
        with open(dbLoc,'r') as rf:
            data = json.load(rf)

        if email in data:
            return 1, data
        else: return 0, data

    def addData(self, name, email, password):
        dbLoc = "E:/flask-development/nlpapp/db.json"
        response, data = self.checkUserPresence(email)
        
        if response == 1:
            return 0

        else:
            data[email] = [name, password]
            with open(dbLoc, 'w') as wf:
                json.dump(data, wf)
            return 1
        

    def userLogin(self, email, password):
        """
        return 1 if email is present and password matches
        return -1 if email is present and password is incorrect
        return 0 if emial i not present
        """
        response, data = self.checkUserPresence(email)
        if response == 1:
            if data[email][1] == password:
                return 1
            else: return -1
        else: return 0
