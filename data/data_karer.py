import numpy as np
import datetime
class slot_data:
    '''
    def get_date_of_order(self):
        return self._get_date_of_order
    def set_date_of_order(self, a):
        self._get_date_of_order = a

    def get_region(self):
        return self._region
    def set_region(self, a):
        self._region = a

    def get_address(self):
        return self._address
    def set_address(self, a):
        self._address = a

    def get_person(self):
        return self._person
    def set_person(self, a):
        self._person = a

    def get_tel(self):
        return self._tel
    def set_tel(self, a):
        self._tel = a

    def get_order_details(self):
        return self._order_details
    def set_order_details(self, a):
        self._order_details = a

    def get_commissioned(self):
        return self._commissioned
    def set_commissioned(self, a):
        self._commissioned = a

    def get_paid(self):
        return self._paid
    def set_paid(self, a):
        self._paid = a
    '''
    def __init__(self,):
        self.date_of_order = datetime.datetime.today()
        self.region = ""
        self.address = ""
        self.person = ""
        self.tel = ""
        self.order_details = ""
        self.commissioned = False
        self.paid = False

class day_data:

    def add_slot(self,date_of_order,region,address,person,tel,order_details,commissioned,paid):
        temp_day = slot_data()
        temp_day.date_of_order = date_of_order
        temp_day.region = region
        temp_day.address = address
        temp_day.person = person
        temp_day.tel = tel
        temp_day.order_details = order_details
        temp_day.commissioned = commissioned
        temp_day.paid = paid
        self.slot_arr.append(temp_day)

    def __init__(self,date):
        self.slot_arr = []
        self.date_of_data = date

class team_data:
    def add_day(self,date):
        self.day_arr.append(day_data(date))

    def __init__(self):
        self.day_arr = []
        self.team_name = ""

class karer_data:

    def add_team(self,team_name):
        temp_team_data = team_data()
        temp_team_data.team_name = team_name #decide team name
        self.all_teams_data.append(temp_team_data)

    def remove_team(self, index):
        try:
            self.all_teams_data.pop(index)
        except:
            print("out of bounds")

    def add_an_unallocated_team(self,region,address,person,tel,order_details):
        temp_day = slot_data()
        temp_day.date_of_order = datetime.datetime.today()
        temp_day.region = region
        temp_day.address = address
        temp_day.person = person
        temp_day.tel = tel
        temp_day.order_details = order_details
        temp_day.commissioned = False
        temp_day.paid = False
        self.unallocated_orders.append(temp_day)

    def __init__(self):
        self.all_teams_data = []
        self.unallocated_orders = []

        self.regions = ["Lefkoşa", "Girne", "Batı", "Doğu"]

        self.add_team("Delta")
        self.add_team("Gama")


        '''
        self.add_team("Delta")
        print(self.all_teams_data[0].team_name)
        self.all_teams_data[0].add_day(datetime.date.today())
        print(self.all_teams_data[0].day_arr[0].date_of_data)
        self.all_teams_data[0].add_day(datetime.date.today() + datetime.timedelta(days=1))
        print(self.all_teams_data[0].day_arr[1].date_of_data)
        self.all_teams_data[0].day_arr[1].add_slot(datetime.datetime.today(),"WEST","Guzelyurt, gotume girdi sokak","Adnan Ertay","0000","bir klima",False ,True)
        self.all_teams_data[0].day_arr[0].add_slot(datetime.datetime.today(),"WEST", "Guzelyurt, gotume girdi sokak","Serife Ertay", "0000", "bir klima", False, True)
        print(self.all_teams_data[0].day_arr[0].slot_arr[0].person)
        print(self.all_teams_data[0].day_arr[1].slot_arr[0].person)
        '''