class User:
    def __init__(self, username, user_type, name, dob, email,gender,street,province,country,phonenumber):
        self.username = username
        self.user_type = user_type
        self.name = name
        self.dob = dob
        self.email = email
        self.gender = gender
        self.street = street
        self.province = province
        self.country = country
        self.phonenumber = phonenumber
    
    def getUserDetails(self):
        user_details = {
            "name":self.name,
            "dob":self.dob,
            "email":self.email,
            "gender":self.gender,
            "phonenumber":self.phonenumber,
            "address":getAddress
        }
        return user_details
    
    def getAddress(self):
        address = {
            "street":self.street,
            "province":self.province,
            "country":self.country,
        }
        return address