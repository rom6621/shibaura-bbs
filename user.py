class User:
    id: str
    mailAddress: str
    
    def __init__(self, userId, userMailAddress):
        self.id = userId
        self.mailAddress = userMailAddress