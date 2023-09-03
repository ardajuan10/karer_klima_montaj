from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from datetime import date
from datetime import timedelta
import data.data_karer as data_class
'''
#command=lambda w=widget: self.on_start(index)
class DragManager():
  def add_dragable(self, widget, win):
    widget.bind("<ButtonPress-1>", self.on_start)
    widget.bind("<B1-Motion>", self.on_drag)
    widget.bind("<ButtonRelease-1>", self.on_drop)
    #Label(win, text="Arda", font=("Arial Bold", 15), background="Light Blue", width=20).place(x=600,y=600)
    #widget.configure(cursor="hand1")

  def on_start(self, event):
    # you could use this method to create a floating window
    # that represents what is being dragged.

    print("started")
    pass

  def on_drag(self, event):
    # you could use this method to move a floating window that
    # represents what you're dragging
    print("dragged")
    event.widget.place(x=event.x_root - event.x,y=event.y_root - event.y)
    print("x= " +str(event.x_root)+ " y= " + str(event.y_root))
    #Label(w, text="x= " +event.x+ " y= " + event.y , font=("Arial Bold", 15), background="Light Blue", width=20).place(x=600, y=600)
    #pass

  def on_drop(self, event):
    # find the widget under the cursor
    print("dropped")
    x, y = event.widget.winfo_pointerxy()
    target = event.widget.winfo_containing(x, y)
    try:
      target.configure(image=event.widget.cget("image"))
    except:
      pass
'''
class karer_Calendar_HMI:
  def add_dragable(self, widget):
    widget.bind("<ButtonPress-1>", self.on_start)
    widget.bind("<B1-Motion>", self.on_drag)
    widget.bind("<ButtonRelease-1>", self.on_drop)
    #Label(win, text="Arda", font=("Arial Bold", 15), background="Light Blue", width=20).place(x=600,y=600)
    #widget.configure(cursor="hand1")

  def on_start(self, event):
    # you could use this method to create a floating window
    # that represents what is being dragged.

    print("started")
    pass

  def on_drag(self, event):
    # you could use this method to move a floating window that
    # represents what you're dragging
    print("dragged")

    event.widget.place(x=self.window.winfo_pointerx() - self.window.winfo_rootx(), y=self.window.winfo_pointery() - self.window.winfo_rooty())
    print("x= " +str(event.x_root)+ " y= " + str(event.y_root))
    #Label(w, text="x= " +event.x+ " y= " + event.y , font=("Arial Bold", 15), background="Light Blue", width=20).place(x=600, y=600)
    #pass

  def on_drop(self, event):
    # find the widget under the cursor
    print("dropped")
    x, y = event.widget.winfo_pointerxy()
    target = event.widget.winfo_containing(x, y)
    try:
      target.configure(image=event.widget.cget("image"))
    except:
      pass

  def __place_unallocated_orders(self):


    lbl_unalloc_order = Label(self.window, text= "Tahsis Edilmemiş\nSiparişler", font=("Arial Bold", 15), background = "Light Blue", width= 20)
    lbl_unalloc_order.configure(anchor="w")
    lbl_unalloc_order.place(x=1300,y=95)

    for i in range(len(self.unallocated_order_canv)):
      try:
        #self.unallocated_order_label[i].destroy()
        #self.unallocated_order_detail_button[i].destroy()
        self.unallocated_order_canv[i].destroy()
      except:
        print("table setroy err")

    #self.unallocated_order_label = []
    #self.unallocated_order_detail_button = []
    self.unallocated_order_canv = []
    #canvas = Canvas(self.window)

    start_x_rec = 1300
    start_y_rec = 160
    rect_w = 160
    rect_h = 80
    start_x_con = 1310
    start_y_con = 170
    button_offset = 40
    label_offset = 85

    for i in range(len(self.calendar_data.unallocated_orders)):
      #self.unallocated_order_label.append(Label(self.window, text= self.calendar_data.unallocated_orders[i].person + "\n" + self.calendar_data.unallocated_orders[i].region, font=("Arial", 11),background="Light Blue"))
      #self.unallocated_order_detail_button.append(Button(self.window, text= "Detaylar"))

      self.unallocated_order_canv.append(Canvas(self.window,width=rect_w,height=rect_h,bg="Beige",bd=0,highlightthickness=0,))




      #self.unallocated_order_rect[i].create_rectangle(start_x_rec,start_y_rec + i*label_offset, start_x_rec + rect_w, start_y_rec + rect_h, fill="Green")
      #self.unallocated_order_rect[i].pack(fill=BOTH,expand=1)
      #self.unallocated_order_rect[i].place(x=start_x_rec, y=start_y_rec + i*label_offset)
      #self.unallocated_order_rect[i].create_rectangle(1,1,rect_w,rect_h,fill="Green")
      #canvas.create_text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
      #canvas.pack()

      self.unallocated_order_canv[i].place(x=start_x_rec, y=start_y_rec + i * label_offset)
      self.add_dragable(self.unallocated_order_canv[i])
      #self.unallocated_order_canv[i].create_text(30,22,text= self.calendar_data.unallocated_orders[i].person + "\n" + self.calendar_data.unallocated_orders[i].region, font=("Arial", 11),)
      #det_button = Button(self.unallocated_order_canv[i], text="Detaylar")
      Label(self.unallocated_order_canv[i], text= self.calendar_data.unallocated_orders[i].person + "\n" + self.calendar_data.unallocated_orders[i].region, font=("Arial", 11),background= "Beige").place(x=5,y=5)
      Button(self.unallocated_order_canv[i], text="Detaylar").place(x=40,y=50)
      #self.unallocated_order_label[i].place(x=start_x_con, y=start_y_con + i*label_offset)
      #self.unallocated_order_detail_button[i].place(x=start_x_con, y=start_y_con + i*label_offset + button_offset)

  def __place_in_table(self, row, column, content, back):
    start_x = 170
    start_y = 95
    gap_x = 150
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
      #self.__place_in_table(1, i, self.dates_arr[i])

      if i == which_day_is_today:
        self.__place_in_table(1, i, self.dates_arr[i], "light green")
      else:
        self.__place_in_table(1, i, self.dates_arr[i], "Light Blue")

  def __go_one_week_back(self):

    for i in range(self.no_of_days):
      self.dates_arr[i] = self.dates_arr[i] - timedelta(days= 7)
      if self.dates_arr[i] == date.today():
        self.__place_in_table(1, i, self.dates_arr[i], "light green")
      else:
        self.__place_in_table(1, i, self.dates_arr[i], "Light Blue")

  def __go_one_week_forward(self):


    for i in range(self.no_of_days):
      self.dates_arr[i] = self.dates_arr[i] + timedelta(days=7)
      if self.dates_arr[i] == date.today():
        self.__place_in_table(1, i, self.dates_arr[i], "light green")
      else:
        self.__place_in_table(1, i, self.dates_arr[i], "Light Blue")

  def __forward_backward_today_buttons(self):
    Backwards = Button(self.window, text="<", command = self.__go_one_week_back)
    Backwards.place(x=500, y=30)

    Today = Button(self.window, text="Bu gün", command=self.__place_the_dates_according_to_today)
    Today.place(x=600, y=30)

    Forwards = Button(self.window, text=">", command=self.__go_one_week_forward)
    Forwards.place(x=700, y=30)

  def __change_team_name(self,index):
    self.calendar_data.all_teams_data[index].team_name = self.new_team_name_text.get(1.0, 'end-1c')
    self.ammend_team.destroy()
    self.__list_team_names()
    self.__present_team_name()


  def __delete_team(self,index):
    #self.__clear_the_team_names_from_the_list()
    self.calendar_data.all_teams_data.pop(index)
    self.ammend_team.destroy()
    self.__list_team_names()
    if self.current_team_index >= len(self.calendar_data.all_teams_data):
      self.current_team_index = len(self.calendar_data.all_teams_data) - 1
    if self.current_team_index < 0:
      self.current_team_index = 0
    self.__present_team_name()

  def __select_team(self,index):
    self.current_team_index = index
    self.ammend_team.destroy()
    #self.team_window.destroy()
    self.__present_team_name()


  def __delete_or_select_team(self,team_index):
    self.ammend_team = Tk()
    self.ammend_team.title("Takımı Düzenle")
    self.ammend_team.geometry('700x300')
    self.ammend_team.config(background="Light Blue")

    lbl_team = Label(self.ammend_team, text=str(team_index + 1) + ". " + self.calendar_data.all_teams_data[team_index].team_name, font=("Arial", 12))
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

    for i in range(len(self.calendar_data.all_teams_data)):
      self.lbl_team_list.append(Button(self.team_window, text= str(i+1) + ". " + self.calendar_data.all_teams_data[i].team_name, command=lambda team_index=i: self.__delete_or_select_team(team_index)))
      self.lbl_team_list[i].place(x=20, y=40 + i * 25)

  def __add_team(self):
    self.calendar_data.add_team(self.team_to_add_text.get(1.0,'end-1c'))
    self.__list_team_names()
    self.__present_team_name()

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

  def __teams_button(self):
    Teams = Button(self.window, text="Takımlar", command=self.__manage_teams_window)
    Teams.place(x=350, y=30)

  def __present_team_name(self):
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

  def __add_the_order(self):

    if self.text_adr.get(1.0, 'end-1c') != "" and self.text_Person.get(1.0, 'end-1c') != "" and self.text_tel.get(1.0, 'end-1c') != "" and self.text_order_details.get(1.0, 'end-1c') != "":
      self.calendar_data.add_an_unallocated_team(region= self.value_inside_region.get(), address= self.text_adr.get(1.0, 'end-1c'), person= self.text_Person.get(1.0, 'end-1c'), tel= self.text_tel.get(1.0, 'end-1c'), order_details= self.text_order_details.get(1.0, 'end-1c'))
      #last_elem = len(self.calendar_data.unallocated_orders) - 1
      #print(self.calendar_data.unallocated_orders[last_elem].region)
      #print(self.calendar_data.unallocated_orders[last_elem].address)
      #print(self.calendar_data.unallocated_orders[last_elem].person)
      #print(self.calendar_data.unallocated_orders[last_elem].tel)
      #print(self.calendar_data.unallocated_orders[last_elem].order_details)
      self.take_order_window.destroy()
      self.__place_unallocated_orders()

    else:
      current_team_label = Label(self.take_order_window, text="Bütün boşlukları doldurunuz", font=("Arial Bold", 12), background="Light Blue", foreground= "Red")
      current_team_label.place(x=50,y=200)


  def __take_order(self):
    self.take_order_window = Tk()
    self.take_order_window.title("Sipariş Al")
    self.take_order_window.geometry('500x300')
    self.take_order_window.config(background="Light Blue")

    current_team_label = Label(self.take_order_window, text="Bölge:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=17)
    current_team_label.grid(row=0, column=0)

    current_team_label = Label(self.take_order_window, text="Adres:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=17)
    current_team_label.grid(row=1, column=0)

    current_team_label = Label(self.take_order_window, text="Şahıs:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=17)
    current_team_label.grid(row=2, column=0)

    current_team_label = Label(self.take_order_window, text="Telefon:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=17)
    current_team_label.grid(row=3, column=0)

    current_team_label = Label(self.take_order_window, text="Sipariş Detayları:", font=("Arial Bold", 12), background="Light Blue",anchor="e",width=17)
    current_team_label.grid(row=4, column=0)

    #text_region = Text(take_order_window, width=30, height=1, font=("Arial",12))
    #text_region.grid(row=0, column=1)
    # Create Dropdown menu
    # datatype of menu text
    self.value_inside_region = StringVar(self.take_order_window)
    self.value_inside_region.set(self.calendar_data.regions[0])
    self.drop_region = OptionMenu(self.take_order_window, self.value_inside_region, self.calendar_data.regions[0], *self.calendar_data.regions)
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
    take_order.place(x=350, y=150)

  def __take_order_button(self):
    take_order = Button(self.window, text="Sipariş Al", command=self.__take_order)
    take_order.place(x=250, y=30)

  def __init__(self):
    self.calendar_data = data_class.karer_data()

    #self.dnd = DragManager()

    self.window = Tk()
    self.window.title("Karer Montaj Takvimi")
    self.window.geometry('1500x1000')
    self.window.config(background="Light Blue")

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
    self.lbl_team_list = []  # list of teams

    self.__place_unallocated_orders()

    self.__place_the_days_of_week()

    self.__place_the_dates_according_to_today()

    self.__forward_backward_today_buttons()

    self.__teams_button()

    self.__present_team_name()

    self.__take_order_button()

    self.window.mainloop()



