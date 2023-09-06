import numpy as np
import datetime
class slot_data:

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

    def __init__(self, date, first_slot):
        self.slot_arr = []
        self.slot_arr.append(first_slot)
        self.date_of_data = date

class team_data:


    def __init__(self):
        self.day_arr = []
        self.team_name = ""

    def add_slot_to_the_team(self, slot_data_to_insert, date):

        for i in range(len(self.day_arr)):
            if date < self.day_arr[i].date_of_data:  # date is already passed, insert the day date object, after that add the slot
                temp_day = day_data(date, slot_data_to_insert)
                self.day_arr.insert(i, temp_day)
                return
            elif date == self.day_arr[i].date_of_data:  # same date is reached, the date object already exist, just add the slot
                self.day_arr[i].slot_arr.append(slot_data_to_insert)  # add the slot when the correct date is reached
                return
        # if it comes here, it means that the date is bigger than all the dates in the array
        temp_day = day_data(date, slot_data_to_insert)
        self.day_arr.append(temp_day)

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

    def add_an_unallocated_slot(self,region,address,person,tel,order_details):
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

        slot_temp = slot_data()
        slot_temp.tel = "3166"
        self.all_teams_data[0].add_slot_to_the_team(slot_temp, datetime.date.today())

        slot_temp_a = slot_data()
        slot_temp_a.tel = "3366"
        self.all_teams_data[0].add_slot_to_the_team(slot_temp_a, datetime.date.today() + datetime.timedelta(days=2))
        print(self.all_teams_data[0].day_arr[0].slot_arr[0].tel)
        print(self.all_teams_data[0].day_arr[1].slot_arr[0].tel)

        '''
        slot_temp.tel = "3266"
        self.all_teams_data[0].add_slot_to_the_team(slot_temp, datetime.date.today() + datetime.timedelta(days=1))
        print(self.all_teams_data[0].day_arr[0].slot_arr[0].tel)
        print(self.all_teams_data[0].day_arr[1].slot_arr[0].tel)
        print(self.all_teams_data[0].day_arr[2].slot_arr[0].tel)
        '''
        '''
        slot_temp.tel = "3466"
        self.all_teams_data[0].add_slot_to_the_team(slot_temp, datetime.date.today() + datetime.timedelta(days=3))
        slot_temp.tel = "3066"
        self.all_teams_data[0].add_slot_to_the_team(slot_temp, datetime.date.today() - datetime.timedelta(days=3))
        slot_temp.tel = "326669"
        self.all_teams_data[0].add_slot_to_the_team(slot_temp, datetime.date.today() + datetime.timedelta(days=1))

        print(self.all_teams_data[0].day_arr[0].slot_arr[0].tel)
        '''

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