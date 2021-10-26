class Tools:
    """
    This model is to help in management of the tools being used 
    in the farm, record keeping of this assets prevents loss and therefore
    it is necessary to keep track or progress of this information
    """
    def __init__(self,name,keeper,price,user,date_of_borrow,
                date_of_return,person_borrowing,person_lending):
        
        self.name = name
        self.keeper = keeper
        self.price = price
        self.user = user
        self.date_of_borrow = date_of_borrow
        self.date_of_return = date_of_return
        self.person_borrowing = person_borrowing
        self.person_lending = person_lending

"""
below is the testing procedure of the above class
"""
if __name__=='__main__':
    slasher = Tools('slasher','David',700,'Kevin',0,0,None,None)
    panga = Tools('panga','David',700,'David','2021-10-25',
                '2021-10-27','Nzioki','Mutisya')

    print(panga.user)

