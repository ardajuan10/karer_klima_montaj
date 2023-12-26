from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
from datetime import date
from datetime import timedelta
import data.data_karer as data_class

class manage_teams_popup:
  def __change_team_name(self,index):
    self.karer_hmi.calendar_data.all_teams_data[index].team_name = self.new_team_name_text.get(1.0, 'end-1c')
    self.ammend_team.destroy()
    self.__list_team_names()
    self.karer_hmi.present_team_name()
    self.karer_hmi.place_dates_and_allocated_orders()


  def __delete_team(self,index):
    #self.__clear_the_team_names_from_the_list()
    self.karer_hmi.calendar_data.all_teams_data.pop(index)
    self.ammend_team.destroy()
    self.__list_team_names()
    if self.karer_hmi.current_team_index >= len(self.karer_hmi.calendar_data.all_teams_data):
      self.karer_hmi.current_team_index = len(self.karer_hmi.calendar_data.all_teams_data) - 1
    if self.karer_hmi.current_team_index < 0:
      self.karer_hmi.current_team_index = 0
    self.karer_hmi.present_team_name()
    self.karer_hmi.place_dates_and_allocated_orders()

  def __select_team(self,index):
    self.karer_hmi.current_team_index = index
    self.ammend_team.destroy()
    #self.team_window.destroy()
    self.karer_hmi.present_team_name()
    self.karer_hmi.place_dates_and_allocated_orders()


  def __delete_or_select_team(self,team_index):
    self.ammend_team = Tk()
    self.ammend_team.title("Takımı Düzenle")
    self.ammend_team.geometry('700x300')
    self.ammend_team.config(background="Light Blue")

    lbl_team = Label(self.ammend_team, text=str(team_index + 1) + ". " + self.karer_hmi.calendar_data.all_teams_data[team_index].team_name, font=("Arial", 12))
    lbl_team.place(x=20, y=20)

    self.new_team_name_text = Text(self.ammend_team, width=15, height=1, font=("Arial", 12))
    self.new_team_name_text.place(x=20, y=100)
    add_Team = Button(self.ammend_team, text="Takım adını degiştir", command=lambda index=team_index: self.__change_team_name(index))
    add_Team.place(x=20, y=125)

    delete_Team = Button(self.ammend_team, text="Takımı sil", command=lambda index=team_index: self.__delete_team(index))
    delete_Team.place(x=200, y=125)

    select_team = Button(self.ammend_team, text="Takımı seç", command=lambda index=team_index: self.__select_team(index))
    select_team.place(x=400, y=125)



  def __list_team_names(self):
    self.lbl_team_header = Label(self.team_window, text="Takımlar", font=("Arial Bold", 12))
    self.lbl_team_header.place(x=20, y=10)

    for i in range(len(self.lbl_team_list)):
      try:
        self.lbl_team_list[i].after(10, self.lbl_team_list[i].destroy())
      except:
        print("list teams err")

    self.lbl_team_list = []  # empty list

    for i in range(len(self.karer_hmi.calendar_data.all_teams_data)):
      self.lbl_team_list.append(Button(self.team_window, text= str(i+1) + ". " + self.karer_hmi.calendar_data.all_teams_data[i].team_name, command=lambda team_index=i: self.__delete_or_select_team(team_index)))
      self.lbl_team_list[i].place(x=20, y=40 + i * 25)

  def __add_team(self):
    self.karer_hmi.calendar_data.add_team(self.team_to_add_text.get(1.0,'end-1c'))
    self.__list_team_names()
    self.karer_hmi.present_team_name()
    self.karer_hmi.place_dates_and_allocated_orders()

  def __manage_teams_window(self):
    self.team_window = Tk()
    self.team_window.title("Karer Takım Penceresi")
    self.team_window.geometry('700x300')
    self.team_window.config(background="Light Blue")

    self.__list_team_names()

    self.team_to_add_text = Text(self.team_window, width=15, height=1, font=("Arial",12))
    self.team_to_add_text.place(x=200,y=40)

    add_Team = Button(self.team_window, text="Takımı Ekle", command=self.__add_team)
    add_Team.place(x=200, y=65)

  def teams_button(self):
    Teams = Button(self.karer_hmi.window, text="Takımlar", command=self.__manage_teams_window)
    Teams.place(x=350, y=30)

  def __init__(self, hmi):
    self.karer_hmi = hmi

    self.lbl_team_list = []  # empty list

class add_order_popup:
  def __add_the_order(self):

    if self.text_adr.get(1.0, 'end-1c') != "" and self.text_Person.get(1.0, 'end-1c') != "" and self.text_tel.get(1.0, 'end-1c') != "" and self.text_order_details.get(1.0, 'end-1c') != "":
      self.karer_hmi.calendar_data.add_an_unallocated_slot(region= self.value_inside_region.get(), address= self.text_adr.get(1.0, 'end-1c'), person= self.text_Person.get(1.0, 'end-1c'), tel= self.text_tel.get(1.0, 'end-1c'), order_details= self.text_order_details.get(1.0, 'end-1c'))
      #last_elem = len(self.calendar_data.unallocated_orders) - 1
      #print(self.calendar_data.unallocated_orders[last_elem].region)
      #print(self.calendar_data.unallocated_orders[last_elem].address)
      #print(self.calendar_data.unallocated_orders[last_elem].person)
      #print(self.calendar_data.unallocated_orders[last_elem].tel)
      #print(self.calendar_data.unallocated_orders[last_elem].order_details)
      self.take_order_window.destroy()
      self.karer_hmi.place_unallocated_orders()

    else:
      current_team_label = Label(self.take_order_window, text="Bütün boşlukları doldurunuz", font=("Arial Bold", 12), background="Light Blue", foreground= "Red")
      current_team_label.place(x=50,y=200)


  def __take_order(self):
    self.take_order_window = Tk()
    self.take_order_window.title("Sipariş Al")
    self.take_order_window.geometry('500x300')
    self.take_order_window.config(background="Light Blue")

    current_team_label = Label(self.take_order_window, text="Bölge:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=0, column=0)

    current_team_label = Label(self.take_order_window, text="Adres:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=1, column=0)

    current_team_label = Label(self.take_order_window, text="Şahıs:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=2, column=0)

    current_team_label = Label(self.take_order_window, text="Telefon:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=3, column=0)

    current_team_label = Label(self.take_order_window, text="Sipariş Detayları:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=25)
    current_team_label.grid(row=4, column=0)

    current_team_label = Label(self.take_order_window, text="9 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=5, column=0)

    current_team_label = Label(self.take_order_window, text="12 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=6, column=0)

    current_team_label = Label(self.take_order_window, text="18 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=7, column=0)

    current_team_label = Label(self.take_order_window, text="24 kBtu/h klima miktarı:", font=("Arial Bold", 12), background="Light Blue", anchor="e", width=25)
    current_team_label.grid(row=8, column=0)

    #text_region = Text(take_order_window, width=30, height=1, font=("Arial",12))
    #text_region.grid(row=0, column=1)
    # Create Dropdown menu
    # datatype of menu text
    self.value_inside_region = StringVar(self.take_order_window)
    self.value_inside_region.set(self.karer_hmi.calendar_data.regions[0])
    self.drop_region = OptionMenu(self.take_order_window, self.value_inside_region, self.karer_hmi.calendar_data.regions[0], *self.karer_hmi.calendar_data.regions)
    self.drop_region.config(width= 30)
    self.drop_region.grid(row=0, column=1)

    self.text_adr = Text(self.take_order_window, width=30, height=1, font=("Arial",12))
    self.text_adr.grid(row=1, column=1)

    self.text_Person = Text(self.take_order_window, width=30, height=1, font=("Arial",12))
    self.text_Person.grid(row=2, column=1)

    self.text_tel = Text(self.take_order_window, width=30, height=1, font=("Arial",12))
    self.text_tel.grid(row=3, column=1)

    self.text_order_details = Text(self.take_order_window, width=30, height=2, font=("Arial",12))
    self.text_order_details.grid(row=4, column=1)

    take_order = Button(self.take_order_window, text="Onayla", command=self.__add_the_order)
    take_order.place(x=350, y=350)

  def take_order_button(self):
    take_order = Button(self.karer_hmi.window, text="Sipariş Al", command=self.__take_order)
    take_order.place(x=250, y=30)

  def __init__(self, hmi):
    self.karer_hmi = hmi

class drag_n_drop:
    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        # Label(win, text="Arda", font=("Arial Bold", 15), background="Light Blue", width=20).place(x=600,y=600)
        # widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        self.x_coordinates_of_button_click = event.x
        self.y_coordinates_of_button_click = event.y

        #Find which unallocated order canvas has been moved
        self.unallocated_order_found = FALSE
        self.unallocated_order_found_no = 0
        for i in range(len(self.karer_hmi.unallocated_order_canv)):
          if self.karer_hmi.unallocated_order_canv[i] == event.widget:
            print("Unallocated Order " + str(i) + " is being moved")
            self.unallocated_order_found = TRUE
            self.unallocated_order_found_no = i

        # Find which allocated order canvas has been moved
        self.allocated_order_found = FALSE
        allocated_order_canvas_found_no = 0
        self.allocated_order_found_no = 0
        self.allocated_order_found_date = 0
        if self.unallocated_order_found == FALSE:
          for i in range(len(self.karer_hmi.allocated_order_canv)):
            if self.karer_hmi.allocated_order_canv[i] == event.widget:
              self.allocated_order_found = TRUE
              allocated_order_canvas_found_no = i

        #Map allocated order canvas to the data
        slot_arr = []
        inspected_allocated_order = 0
        if self.allocated_order_found:
          for col in range(self.karer_hmi.no_of_days):
            try:
              slot_arr = self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].get_slots_for_the_day(self.karer_hmi.dates_arr[col])
            except:
              print("no team present")

            for row in range(len(slot_arr)):
              if allocated_order_canvas_found_no == inspected_allocated_order:
                print("Allocated Order day " + str(self.karer_hmi.dates_arr[col]) + " row " + str(row) + " is being moved.")
                self.allocated_order_found_no = row
                self.allocated_order_found_date = self.karer_hmi.dates_arr[col]
              inspected_allocated_order = inspected_allocated_order + 1


        # print("started")
        pass

    def on_drag(self, event):

        event.widget.place(
            x=self.window.winfo_pointerx() - self.window.winfo_rootx() - self.x_coordinates_of_button_click,
            y=self.window.winfo_pointery() - self.window.winfo_rooty() - self.y_coordinates_of_button_click)
        print(self.window.winfo_pointerx() - self.window.winfo_rootx() - self.x_coordinates_of_button_click + 90)

    def on_drop(self, event):
        # find the widget under the cursor
        print("dropped")
        allocated_start_x = 170
        allocated_gap_x = 180
        canvas_last_x_coordinate = self.window.winfo_pointerx() - self.window.winfo_rootx() - self.x_coordinates_of_button_click + allocated_gap_x/2
        unallocated_start_x = 1450
        unallocated_gap_x = 180

        destination_is_allocated = FALSE
        destination_allocated_day = 0
        destination_is_unallocated = FALSE


        ##CHECK IF THE DESTINATION IS IN ALLOCATED REGION
        for col in range(self.karer_hmi.no_of_days):
          if canvas_last_x_coordinate > allocated_start_x + col * allocated_gap_x and canvas_last_x_coordinate <= allocated_start_x + (col+1) * allocated_gap_x:
            print('Moving the slot to day ' + str(self.karer_hmi.dates_arr[col]))
            destination_is_allocated = TRUE
            destination_allocated_day = self.karer_hmi.dates_arr[col]

        ##CHECK IF THE DESTINATION IS IN UNALLOCATED REGION
        if destination_is_allocated == FALSE:
          if canvas_last_x_coordinate > unallocated_start_x and canvas_last_x_coordinate <= unallocated_start_x + unallocated_gap_x:
            destination_is_unallocated = TRUE

        if (self.allocated_order_found or self.unallocated_order_found) and (destination_is_allocated or destination_is_unallocated):
          ##PREPARE THE SLOT TO BE MOVED and delete the dragged slot
          if self.allocated_order_found == TRUE:
            slot_to_move = self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].remove_slot_from_the_team(self.allocated_order_found_date,self.allocated_order_found_no)
          elif self.unallocated_order_found == TRUE:
            slot_to_move = self.karer_hmi.calendar_data.unallocated_orders.pop(self.unallocated_order_found_no)
          else:
            return

          ##Move the DRAGGED SLOT TO ITS NEW LOCATION
          if destination_is_allocated == TRUE:
            self.karer_hmi.calendar_data.all_teams_data[self.karer_hmi.current_team_index].add_slot_to_the_team(slot_to_move,destination_allocated_day)
          elif destination_is_unallocated == TRUE:
            self.karer_hmi.calendar_data.unallocated_orders.append(slot_to_move)
          else:
            return


        self.karer_hmi.refresh_page()

    def __init__(self,win,hmi):
        self.window = win
        self.karer_hmi = hmi

class karer_Calendar_HMI:

  def place_canvas(self, x_axis, y_axis, slot_data):
    rect_w = 160
    rect_h = 80
    canvas_out = Canvas(self.window, width=rect_w, height=rect_h, bg="Beige", bd=0, highlightthickness=0, )
    canvas_out.place(x=x_axis, y=y_axis)
    self.drag.add_dragable(canvas_out)
    Label(canvas_out, text=slot_data.person + "\n" + slot_data.region, font=("Arial", 11), background="Beige").place(x=5, y=5)
    Button(canvas_out, text="Detaylar").place(x=40, y=50)

    return canvas_out

  def place_unallocated_orders(self):

    start_x_rec = 1450
    start_y_rec = 160

    label_offset = 85

    lbl_unalloc_order = Label(self.window, text= "Tahsis Edilmemiş\nSiparişler", font=("Arial Bold", 15), background = "Light Blue", width= 20)
    lbl_unalloc_order.configure(anchor="w")
    lbl_unalloc_order.place(x=start_x_rec,y=95)

    for i in range(len(self.unallocated_order_canv)):
      try:
        self.unallocated_order_canv[i].destroy()
      except:
        print("table setroy err")


    self.unallocated_order_canv = []



    for i in range(len(self.calendar_data.unallocated_orders)):
      self.unallocated_order_canv.append(self.place_canvas(x_axis = start_x_rec, y_axis = start_y_rec + i * label_offset, slot_data = self.calendar_data.unallocated_orders[i]))

  def __place_in_table(self, row, column, content, back):
    start_x = 170
    start_y = 95
    gap_x = 180
    gap_y = 30
    width_x = 12
    try:
      self.lbl_table_header[row][column].destroy()
    except:
      print("table setroy err")
    self.lbl_table_header[row][column] = Label(self.window, width= width_x, text=content, font=("Arial Bold", 15), background = back)
    self.lbl_table_header[row][column].place(x=start_x + gap_x * column, y=start_y + gap_y * row)

  def __place_logo(self):
    ## PUT THE IMAGE ON THE TOP LEFT CORNER
    # Load the image
    image_karer = Image.open('logo_karer.png')
    # Resize the image in the given (width, height)
    image_karer_R = image_karer.resize((150, 75))
    # Conver the image in TkImage
    my_img_karer = ImageTk.PhotoImage(image_karer_R)
    # Display the image with label
    lbl_karer = Label(self.window, image=my_img_karer)
    lbl_karer.place(x=10, y=10)
    lbl_karer.image = my_img_karer

  def __place_the_days_of_week(self):
    self.__place_in_table(0, 0, "Pazartesi", "Light Blue")
    self.__place_in_table(0, 1, "Salı", "Light Blue")
    self.__place_in_table(0, 2, "Çarşamba", "Light Blue")
    self.__place_in_table(0, 3, "Perşembe", "Light Blue")
    self.__place_in_table(0, 4, "Cuma", "Light Blue")
    self.__place_in_table(0, 5, "Cumartesi", "Light Blue")
    self.__place_in_table(0, 6, "Pazar", "Light Blue")

  def __place_the_allocated_orders_for_the_week(self):


    start_x = 170
    start_y = 160
    gap_x = 180
    gap_y = 85

    for temp in self.allocated_order_canv:
      try:
        temp.destroy()
      except:
        print("couldnt destroy allocated canvas")

    #empty the allocated order arr
    self.allocated_order_canv = []

    #finally place the canvases one by one
    for col in range(self.no_of_days):
      try:
        slot_arr = self.calendar_data.all_teams_data[self.current_team_index].get_slots_for_the_day(self.dates_arr[col])
      except:
        print("no team present")

      for row in range(len(slot_arr)):
        self.allocated_order_canv.append(self.place_canvas(x_axis = start_x + col * gap_x, y_axis = start_y + row * gap_y, slot_data = slot_arr[row]))





  def place_dates_and_allocated_orders(self):
    for i in range(self.no_of_days):
      if self.dates_arr[i] == date.today():
        self.__place_in_table(1, i, self.dates_arr[i], "light green")
      else:
        self.__place_in_table(1, i, self.dates_arr[i], "Light Blue")

    self.__place_the_allocated_orders_for_the_week()

  def __place_the_dates_according_to_today(self):
    ##FIND TODAYS DATE
    days_arr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = date.today()
    which_day_is_today = 0
    ##SPOT WHAT DAY IS TODAY
    for i in range(self.no_of_days):
      if today.strftime('%A') == days_arr[i]:
        which_day_is_today = i
    ##PLACE THE DATES TO 1st COLUMN
    for i in range(self.no_of_days):
      self.dates_arr[i] = today + timedelta(days=i - which_day_is_today)

    self.place_dates_and_allocated_orders()

  def __go_one_week_back(self):

    for i in range(self.no_of_days):
      self.dates_arr[i] = self.dates_arr[i] - timedelta(days= 7)

    self.place_dates_and_allocated_orders()

  def __go_one_week_forward(self):


    for i in range(self.no_of_days):
      self.dates_arr[i] = self.dates_arr[i] + timedelta(days=7)

    self.place_dates_and_allocated_orders()

  def __forward_backward_today_buttons(self):
    Backwards = Button(self.window, text="<", command = self.__go_one_week_back)
    Backwards.place(x=500, y=30)

    Today = Button(self.window, text="Bu gün", command=self.__place_the_dates_according_to_today)
    Today.place(x=600, y=30)

    Forwards = Button(self.window, text=">", command=self.__go_one_week_forward)
    Forwards.place(x=700, y=30)



  def present_team_name(self):
    try:
      text_temp = "Seçilen takım: " + str(self.current_team_index + 1) + ". " + self.calendar_data.all_teams_data[self.current_team_index].team_name
    except:
      text_temp = "Takım yok"

    try:
      self.current_team_label.destroy()
    except:
      print("presented team err")
    self.current_team_label = Label(self.window, text=text_temp, font=("Arial Bold", 12), background= "Light Blue")
    self.current_team_label.place(x=800, y=30)



  def refresh_page(self):
    self.place_unallocated_orders()
    self.place_dates_and_allocated_orders()
    self.present_team_name()

  def __init__(self):
    self.calendar_data = data_class.karer_data()


    #self.dnd = DragManager()
    #self.x_coordinates_of_button_click = 0
    #self.y_coordinates_of_button_click = 0



    self.window = Tk()
    self.window.title("Karer Montaj Takvimi")
    self.window.geometry("800x600")
    #window_temp.attributes('-fullscreen', True)  # make main window full-screen
    self.window.config(background="Light Blue")

    '''
    #Create frame
    frame_temp = Frame(window_temp)
    frame_temp.pack(fill=BOTH, expand=1)

    #Create canvas
    my_canvas = Canvas(frame_temp, bg='Light Blue', highlightthickness=0)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=True)  # configure canvas to occupy the whole main window

    #ADD a scrollbar to canvas
    my_scrollbar = ttk.Scrollbar(frame_temp, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    #create a second frame you will put everything
    second_frame = Frame(my_canvas)

    #Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    #window will be used by all the code
    self.window = my_canvas
    '''
    self.mng_teams_popup = manage_teams_popup(self)

    self.drag = drag_n_drop(self.window, self)

    self.add_ordr_popup = add_order_popup(self)

    self.current_team_index = 0

    self.__place_logo()

    ##INITIALISE THE TABLE
    self.no_of_days = 7
    self.total_col_header = 7
    self.total_row_header = 2
    self.lbl_table_header = [[0 for x in range(self.total_col_header)] for y in range(self.total_row_header)]
    self.dates_arr = [0 for x in range(self.no_of_days)]

    #self.unallocated_order_label = []
    #self.unallocated_order_detail_button = []
    self.unallocated_order_canv = []
    self.allocated_order_canv = []
    #self.lbl_team_list = []  # list of teams

    self.place_unallocated_orders()

    self.__place_the_days_of_week()

    self.__place_the_dates_according_to_today()

    self.__forward_backward_today_buttons()

    self.mng_teams_popup.teams_button()

    self.present_team_name()

    self.add_ordr_popup.take_order_button()

    self.window.mainloop()



