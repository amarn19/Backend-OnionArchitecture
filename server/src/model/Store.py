class Store():
    def __init__(self, establishedon, name, dob, email,gender,street,province,country,phonenumber):
        self.name = name
        self.establishedon = establishedon
        self.email = email
        self.size = gender
        self.street = street
        self.province = province
        self.country = country
        self.phonenumber = phonenumber

    def getStoreDetails(self):
        store_details ={
        "name":self.name,
        "established_on":self.establishedon,
        "email":self.email,
        "store_size":self.size,
        "phone_no":self.phonenumber,
        "address":self.getAddress()
        }
        return store_details
    
    def getAddress(self):
        address = {
            "street":self.street,
            "province":self.province,
            "country":self.country,
        }
        return address