from tkinter import *
from tkinter import ttk
#import customtkinter as ctk
import ttkthemes
from datetime import datetime
import time
from PIL import ImageTk , Image
import pytz

class Clock:

    def __init__(self,root):

        self.root = root

    # defining the body of the window.

        self.root.title("Digital Clock")

        # Full screen resolution or  choosing specific dimensions

        #width = root.winfo_screenwidth()
        #height = root.winfo_screenheight()

        width = img2.width()
        height = img2.height()

        self.root.geometry(f"{width}x{height}")

        #self.root.geometry(f"1280x720")
        
        self.root.minsize(750,200)
        self.root.wm_attributes('-transparentcolor', '#ab23ff')

        #Theming the window. Using TTK Themes module.

        style = ttkthemes.ThemedStyle(self.root)
        style.set_theme("elegance")


        #defining and setting up the buttons frames and labels.(Functions of Tkinter module.)

        f1=Button(self.root,width=110, height=10,bg='#001524',command= self.toggle_sidebar)
        f1.place(x=390,y=310)


        self.sidebar = ttk.Frame(self.root,style="Sidebar.TFrame")
        style = ttkthemes.ThemedStyle(self.sidebar)

        self.sidebar.place(x=-500, y=0, relwidth=0.2, relheight=1)
        self.sidebar_visible = False

        scrollbar = ttk.Scrollbar(self.sidebar, orient='vertical')
        scrollbar.pack(side='right', fill='y')

        self.listbox = Listbox(self.sidebar, yscrollcommand=scrollbar.set , bg="#001524", fg="#FA7070")
        self.listbox.pack(fill='both', expand=True)

        self.populate_time_zones()



        # Using Datetime module to get Day.

        a = datetime.today().strftime("%A").upper()

        # Displaying only the first three letters of the day and adding a separator.

        b = ''+ a[0:3] + "|"

        # defining a function to keep the clock running every 1000 ms
        def curr_time():
            a = time.strftime("   %H  :  %M  :  %S")
            Clock_label.config(text=a)
            Clock_label.after(1000,curr_time)

        # Making the Clock Label(background where time is being displayed.) using Tkinter.
        Clock_label = Label(self.root, font=("Century Gothic",60), bg="#001524", fg="#FA7070")
        Clock_label.place(x=585,y=320)


        # Calling out the curr_time function.
        curr_time()

        def curr_date():
            qw = datetime.today()
            datetoday = qw.date()
            date_label.config(text = f"{datetoday}")

        date_label = Label(self.root, font=("Century Gothic",16), bg="#001524", fg="#d3d3d3",height=2 )
        date_label.place(x=440, y=405)
        curr_date()

        Day_label = Label(self.root, text=f"{b}" ,font=("Century Gothic",60), bg="#001524", fg="#d3d3d3")
        Day_label.place(x=400,y=320)


        #Date_label = Label(self.root, text=)

        def name_labels():
            nameday_label = Label(self.root , text="DAY", font=("Century Gothic" ,12), bg="#001524", fg="#d3d3d3")
            nameday_label.place(x=150+325,y=440)
            namehour_label = Label(self.root , text="HOURS", font=("Century Gothic" ,12), bg="#001524", fg="#d3d3d3")
            namehour_label.place(x=370+300,y=440)
            namemin_label = Label(self.root , text="MINS", font=("Century Gothic" ,12), bg="#001524", fg="#d3d3d3")
            namemin_label.place(x=585+280,y=440)
            namesec_label = Label(self.root , text="SECS", font=("Century Gothic" ,12), bg="#001524", fg="#d3d3d3")
            namesec_label.place(x=770+300,y=440)

        name_labels()

        self.sidebar.bind("<ButtonPress-1>", self.on_drag_start)
        self.sidebar.bind("<B1-Motion>", self.on_drag_motion)

        def get_all_time_zones_time():
            all_time_zones_time = {}
            current_time = datetime.now()
            for tz_name in pytz.all_timezones:
                timezone = pytz.timezone(tz_name)
                current_time_in_tz = current_time.astimezone(timezone)
                all_time_zones_time[tz_name] = current_time_in_tz.strftime('   %H  :  %M  :  %S')
            return all_time_zones_time
        
        def get_all_time_zones_day():
            all_time_zones_day = {}
            current_time = datetime.now()
            for tz_name in pytz.all_timezones:
                timezone = pytz.timezone(tz_name)
                current_time_in_tz = current_time.astimezone(timezone)
                all_time_zones_day[tz_name] = current_time_in_tz.strftime('%Y - %M - %D')
            return all_time_zones_day
        
        alltimezonetime_dict=get_all_time_zones_time()
        alltimezoneday_dict=get_all_time_zones_day()
    def toggle_sidebar(self):
        target_x = 0 if not self.sidebar_visible else -500
        current_x = int(self.sidebar.place_info()['x'])

        step = 15  # Adjust the step value based on the desired animation smoothness
        direction = 1 if target_x > current_x else -1

        def animate():
            nonlocal current_x
            current_x += direction * step
            self.sidebar.place(x=current_x)
            if (direction == 1 and current_x < target_x) or (direction == -1 and current_x > target_x):
                self.root.after(10, animate)
            else:
                self.sidebar_visible = not self.sidebar_visible

        animate()


    def populate_time_zones(self):
        for tz_name in pytz.all_timezones:
            self.listbox.insert(END, tz_name)        

    def on_drag_start(self, event):
        self._drag_data = {'x': event.x, 'y': event.y}

    def on_drag_motion(self, event):
        delta_x = event.x - self._drag_data['x']
        delta_y = event.y - self._drag_data['y']
        x = self.sidebar.winfo_x() + delta_x
        y = self.sidebar.winfo_y() + delta_y
        self.sidebar.place(x=x, y=y)
        self._drag_data['x'] = event.x
        self._drag_data['y'] = event.y  


        
# Calling the functions. This method also helps in calling out functions and modules for other codes.


if __name__ == "__main__":

    # making a GUI window using Tkinter's Tk() function.
    root = Tk()
    #Setting Back Wallpaper/solid.


    if str("01") <=time.strftime("%H")<= str("04") :
        img1=Image.open("pxfuel.jpg")
    elif str("05") <=time.strftime("%H")<= str("08") :
        img1=Image.open("Early morning.jpg")
    elif str("09") <=time.strftime("%H")<=str("12") :
        img1=Image.open("morning.jpg")
    elif str("13") <=time.strftime("%H")<=str("16") :
        img1=Image.open("noon.jpg")
    elif str("17") <=time.strftime("%H")<=str("20") :
        img1=Image.open("evening.jpg")
    else :
        img1=Image.open("noon.jpg")

    
    img2= ImageTk.PhotoImage(img1)
    Label(root,image=img2).place(x=-2,y=0)

    # calling the Clock Class.
    Clock(root)
    root.pack_propagate()
    #looping the app so as to keep the window running.
    root.mainloop()


