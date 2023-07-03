#importin Module
from tkinter import *
from tkinter import messagebox
import re

# function for get all customers
def get_all_customers():
    with open("all_customers.txt","r") as f:
        a=f.read()
        r=a.split("|")
    if len(r)==1:
        messagebox.showwarning("Not Found",f"There is no Customer available or stored.")
    elif len(r)>1:
        root2=Tk()
        root2.title("All Customers")
        root2.geometry("400x555")
        l1=Label(root2,text="Dev Designer",fg="white",bg="#551fbd",font=("Helvetica",16,"bold"),width=30)
        l1.grid(row=1,column=1,pady=10)
        main_frame=Frame(root2)
        main_frame.grid(row=5,column=1)

        my_canvas=Canvas(main_frame,height=500)
        my_canvas.grid(row=0,column=0)

        my_scrollbar=Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
        my_scrollbar.grid(row=0,column=2,sticky=NS)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind("<Configure>",lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        
        second_frame=Frame(my_canvas)
        my_canvas.create_window((0,0),window=second_frame,anchor="nw")
        counter=1
        for i in r[1:]:
            count_label=Label(second_frame,text=f"{counter : }",font=("Helvetica",11))
            count_label.grid(row=counter,column=2,padx=20,pady=6,ipadx=20,ipady=5)
            name_label=Label(second_frame,text=f"{i}",font=("Helvetica",11,"bold"))
            name_label.grid(row=counter,column=3,padx=20,pady=6,ipadx=20,ipady=5)
            counter+=1


# Function for Storing Data
def store_data():
    with open("data.txt","a") as f:
        f1=open("all_customers.txt","a")
        f1.write(f"|{name_entry.get()}")
        text_format=f"Name :{name_entry.get()} | {address_entry.get()} | {district_entry.get()} | {length_text.get()} | {shoulder_text.get()} | {sleave_length_text.get()} | {round_sleave_text.get()} | {arm_hole_text.get()} | {bust_text.get()} | {waist_text.get()} | {hips_text.get()} | {hips_round_text.get()} | {knee_round_text.get()} | {shoulder_hips_length_text.get()} | {shoulder_to_waist_length_text.get()} | {waist_to_knee_length_text.get()} | {shoulder_to_knee_length.get()} | {neck_text.get()} | {back_text.get()} | {shoulder_size.get()} | {hook_patti_back_text.get()} | {shoulder_to_ankle_text.get()} | {hips_to_ankle_text.get()} | {ankle_round_text.get()} |\n"
        f.write(text_format)


#Fucntion for creating result of search
def create_search_result(p):
    root1=Tk()
    root1.title(f"Search Result for {p[0]}")
    root1.geometry("400x555")
    l1=Label(root1,text="Dev Designer",fg="white",bg="#551fbd",font=("Helvetica",16,"bold"),width=30)
    l1.grid(row=1,column=1,pady=10)
    main_frame=Frame(root1)
    main_frame.grid(row=5,column=1)

    my_canvas=Canvas(main_frame,height=500)
    my_canvas.grid(row=0,column=0)

    my_scrollbar=Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.grid(row=0,column=2,sticky=NS)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    second_frame=Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")
    name_label=Label(second_frame,text="Name : ",font=("Helvetica",11))
    name_label.grid(row=2,column=1,padx=20,pady=6)
    name_ans=Label(second_frame,text=f"{p[0]}")
    name_ans.grid(row=2,column=2)
    address_label=Label(second_frame,text="Address : ",font=("Helvetica",11))
    address_label.grid(row=3,column=1,padx=20,pady=6)
    address_ans=Label(second_frame,text=f"{p[1]}")
    address_ans.grid(row=3,column=2)
    district_label=Label(second_frame,text="District : ",font=("Helvetica",11))
    district_label.grid(row=4,column=1,padx=20,pady=6)
    district_ans=Label(second_frame,text=f"{p[2]}")
    district_ans.grid(row=4,column=2)
    distription_label=Label(second_frame,text="Discription",font=("Helvetica",16,"bold"),bg="#551fbd",fg="yellow",width=10)
    distription_label.grid(row=5,column=1,padx=10)
    measurment_label=Label(second_frame,text="Measurment",font=("Helvetica",15,"bold"),bg="#551fbd",fg="yellow",width=10)
    measurment_label.grid(row=5,column=2)

    length_label=Label(second_frame,text="Length :",font=("times",13))
    length_label.grid(row=6,column=1)
    length_ans=Label(second_frame,text=f"{p[3]}")
    length_ans.grid(row=6,column=2)

    shoulder_label=Label(second_frame,text="Shoulder :",font=("times",13))
    shoulder_label.grid(row=7,column=1)
    shoulder_ans=Label(second_frame,text=f"{p[4]}")
    shoulder_ans.grid(row=7,column=2)


    sleave_length_label=Label(second_frame,text="Sleave length :",font=("times",13))
    sleave_length_label.grid(row=8,column=1)
    sleave_length_ans=Label(second_frame,text=f"{p[5]}")
    sleave_length_ans.grid(row=8,column=2)

    round_sleave_label=Label(second_frame,text="Round Sleave :",font=("times",13))
    round_sleave_label.grid(row=9,column=1)
    round_sleave_ans=Label(second_frame,text=f"{p[6]}")
    round_sleave_ans.grid(row=9,column=2)

    arm_hole_label=Label(second_frame,text="Arm Hole :",font=("times",13))
    arm_hole_label.grid(row=10,column=1)
    arm_hole_ans=Label(second_frame,text=f"{p[7]}")
    arm_hole_ans.grid(row=10,column=2)

    bust_label=Label(second_frame,text="Bust :",font=("times",13))
    bust_label.grid(row=11,column=1)
    bust_ans=Label(second_frame,text=f"{p[8]}")
    bust_ans.grid(row=11,column=2)

    waist_label=Label(second_frame,text="Waist :",font=("times",13))
    waist_label.grid(row=12,column=1)
    waist_ans=Label(second_frame,text=f"{p[9]}")
    waist_ans.grid(row=12,column=2)

    hips_label=Label(second_frame,text="Hips :",font=("times",13))
    hips_label.grid(row=13,column=1)
    hips_ans=Label(second_frame,text=f"{p[10]}")
    hips_ans.grid(row=13,column=2)

    hips_round_label=Label(second_frame,text="Hips Round :",font=("times",13))
    hips_round_label.grid(row=14,column=1)
    hips_round_ans=Label(second_frame,text=f"{p[11]}")
    hips_round_ans.grid(row=14,column=2)

    knee_round_label=Label(second_frame,text="Knee Round :",font=("times",13))
    knee_round_label.grid(row=15,column=1)
    knee_round_ans=Label(second_frame,text=f"{p[12]}")
    knee_round_ans.grid(row=15,column=2)

    shoulder_hips_length_label=Label(second_frame,text="Shoulder hips Length :",font=("times",13))
    shoulder_hips_length_label.grid(row=16,column=1)
    shoulder_hips_length_ans=Label(second_frame,text=f"{p[13]}")
    shoulder_hips_length_ans.grid(row=16,column=2)

    shoulder_to_waist_length_label=Label(second_frame,text="Shoulder to Waist Length :",font=("times",13))
    shoulder_to_waist_length_label.grid(row=17,column=1)
    shoulder_to_waist_length_ans=Label(second_frame,text=f"{p[14]}")
    shoulder_to_waist_length_ans.grid(row=17,column=2)

    waist_to_knee_label=Label(second_frame,text="Waist to Knee :",font=("times",13))
    waist_to_knee_label.grid(row=18,column=1)
    waist_to_knee_ans=Label(second_frame,text=f"{p[15]}")
    waist_to_knee_ans.grid(row=18,column=2)

    shoulder_to_knee_length_label=Label(second_frame,text="Shoulder to Knee Length :",font=("times",13))
    shoulder_to_knee_length_label.grid(row=19,column=1)
    shoulder_to_knee_length_ans=Label(second_frame,text=f"{p[16]}")
    shoulder_to_knee_length_ans.grid(row=19,column=2)

    neck_label=Label(second_frame,text="Neck :",font=("times",13))
    neck_label.grid(row=20,column=1)
    neck_ans=Label(second_frame,text=f"{p[17]}")
    neck_ans.grid(row=20,column=2)

    back_label=Label(second_frame,text="Back :",font=("times",13))
    back_label.grid(row=21,column=1)
    back_ans=Label(second_frame,text=f"{p[18]}")
    back_ans.grid(row=21,column=2)

    shoulder_size_label=Label(second_frame,text="Shoulder Size :",font=("times",13))
    shoulder_size_label.grid(row=22,column=1)
    shoulder_size_ans=Label(second_frame,text=f"{p[19]}")
    shoulder_size_ans.grid(row=22,column=2)

    hook_patti_back_label=Label(second_frame,text="Hook Patti Back :",font=("times",13))
    hook_patti_back_label.grid(row=23,column=1)
    hook_patti_back_ans=Label(second_frame,text=f"{p[20]}")
    hook_patti_back_ans.grid(row=23,column=2)

    shoulder_to_ankle_label=Label(second_frame,text="Shoulder to Ankle :",font=("times",13))
    shoulder_to_ankle_label.grid(row=24,column=1)
    shoulder_to_ankle_ans=Label(second_frame,text=f"{p[21]}")
    shoulder_to_ankle_ans.grid(row=24,column=2)

    hips_to_ankle_label=Label(second_frame,text="Hips to Ankle :",font=("times",13))
    hips_to_ankle_label.grid(row=25,column=1)
    hips_to_ankle_ans=Label(second_frame,text=f"{p[22]}")
    hips_to_ankle_ans.grid(row=25,column=2)

    ankle_round_label=Label(second_frame,text="Ankle Round :",font=("times",13))
    ankle_round_label.grid(row=26,column=1)
    ankle_round_ans=Label(second_frame,text=f"{p[23]}")
    ankle_round_ans.grid(row=26,column=2)

    root1.mainloop()

#Function for find and print data according to name
def find_and_print(details):
    a=details[0]
    p=a.split("|")
    create_search_result(p)
    
#Function for finding data from name
def find_by_name():
    search_name=find_text.get()
    if search_name!="":
        f=open("data.txt","r")
        a=f.read().upper()
        r=re.findall(f"{search_name.upper()}.+",a)
        if len(r)==0:
            messagebox.showwarning("Not Found",f"There is no data for Name : {search_name}")
        elif len(r)>0:
            find_and_print(r)
    elif search_name=="":
        messagebox.showwarning("Empty field","Please Enter data in Find box")

#Function for reseting values
def reset_values():
    name_entry.delete(0,'end')
    address_entry.delete(0,'end')
    district_entry.delete(0,'end')
    length_text.delete(0,'end')
    shoulder_text.delete(0,'end')
    sleave_length_text.delete(0,'end')
    round_sleave_text.delete(0,'end')
    arm_hole_text.delete(0,'end')
    bust_text.delete(0,'end')
    waist_text.delete(0,'end')
    hips_text.delete(0,'end')
    hips_round_text.delete(0,'end')
    knee_round_text.delete(0,'end')
    shoulder_to_waist_length_text.delete(0,'end')
    waist_to_knee_length_text.delete(0,'end')
    shoulder_to_knee_length_text.delete(0,'end')
    neck_text.delete(0,'end')
    back_text.delete(0,'end')
    shoulder_hips_length_text.delete(0,'end')
    shoulder_size_text.delete(0,'end')
    hook_patti_back_text.delete(0,'end')
    shoulder_to_ankle_text.delete(0,'end')
    hips_to_ankle_text.delete(0,'end')
    ankle_round_text.delete(0,'end')
    amount_text1.delete(0,'end')
    amount_text2.delete(0,'end')
    amount_text3.delete(0,'end')
    amount_text4.delete(0,'end')
    amount_text5.delete(0,'end')
    amount_text6.delete(0,'end')
    amount_text7.delete(0,'end')
    amount_text8.delete(0,'end')
    amount_text9.delete(0,'end')
    amount_text10.delete(0,'end')
    amount_text11.delete(0,'end')
    name_entry.focus_force()






#Creating Window
root=Tk()

# root.configure(bg="#0f0fff")
#Setting Title of Window
root.title("Measuarment Storing Software")

#Setting Size of Window
root.geometry('943x633')
bg=PhotoImage(file="BG1.png")
my_label=Label(root,image=bg)
my_label.place(x=0,y=0)


# Creating Label Widgets

l1=Label(root,text="Dev Designer",fg="white",bg="#335F87",font=("Helvetica",16,"bold"),width=13)
l1.grid(row=1,column=2,pady=10,padx=20)






#String Variable For Name
name=StringVar()
name_label=Label(root,text="Name :",font=("",10))
name_label.grid(row=2,column=1,pady=6)
name_entry=Entry(root,textvariable=name,justify = CENTER,bd=2)
name_entry.focus_force()
name_entry.grid(row=2,column=2,pady=6)


# String Variable for Address
address=StringVar()
address_label=Label(root,text="Address :",font=("",10))
address_label.grid(row=3,column=1,pady=6)
address_entry=Entry(root,textvariable=address,justify = CENTER,bd=2)
address_entry.grid(row=3,column=2,pady=6)

# String Variable for District
district=StringVar()
district_label=Label(root,text="District :",font=("",10))
district_label.grid(row=4,column=1,pady=6)
district_entry=Entry(root,textvariable=district,justify = CENTER,bd=2)
district_entry.grid(row=4,column=2,pady=6)

#Creating Heading for Columns

# Discription Heading
distription_label=Label(root,text="Discription",font=("Helvetica",16,"bold"),bg="#551fbd",fg="white",width=8)
distription_label.grid(row=5,column=1,pady=8,ipadx=0,padx=5)


distription_label=Label(root,text="Discription",font=("Helvetica",16,"bold"),bg="#551fbd",fg="white")
distription_label.grid(row=5,column=3,pady=8)


# Measurment Heading
measurment_label=Label(root,text="Measurment",font=("Helvetica",16,"bold"),bg="#551fbd",fg="white")
measurment_label.grid(row=5,column=2,pady=6)


measurment_label=Label(root,text="Measurment",font=("Helvetica",16,"bold"),bg="#551fbd",fg="white")
measurment_label.grid(row=5,column=4,pady=6)



# String Variable for Length
length=StringVar()
length_label=Label(root,text="Length :",font=("",10))
length_label.grid(row=6,column=1)
length_text=Entry(root,textvariable=length,justify = CENTER,bd=2)
length_text.grid(row=6,column=2)

# String Variable for shoulder
shoulder=StringVar()
shoulder_label=Label(root,text="Shoulder :",font=("",10))
shoulder_label.grid(row=7,column=1,pady=6)
shoulder_text=Entry(root,textvariable=shoulder,justify = CENTER,bd=2)
shoulder_text.grid(row=7,column=2,pady=6)


# String Variable for sleave_Length
sleave_length=StringVar()
sleave_length_label=Label(root,text="Sleave Length :",font=("",10))
sleave_length_label.grid(row=8,column=1,pady=6)
sleave_length_text=Entry(root,textvariable=sleave_length,justify = CENTER,bd=2)
sleave_length_text.grid(row=8,column=2,pady=6)


# String Variable for round_sleave
round_sleave=StringVar()
round_sleave_label=Label(root,text="Round Sleave :",font=("",10))
round_sleave_label.grid(row=9,column=1,pady=6)
round_sleave_text=Entry(root,textvariable=round_sleave,justify = CENTER,bd=2)
round_sleave_text.grid(row=9,column=2,pady=6)


# String Variable for arm_hole
arm_hole=StringVar()
arm_hole_label=Label(root,text="Arm Hole :",font=("",10))
arm_hole_label.grid(row=10,column=1,pady=6)
arm_hole_text=Entry(root,textvariable=arm_hole,justify = CENTER,bd=2)
arm_hole_text.grid(row=10,column=2,pady=6)


# String Variable for bust
bust=StringVar()
bust_label=Label(root,text="Bust :",font=("",10))
bust_label.grid(row=11,column=1,pady=6)
bust_text=Entry(root,textvariable=bust,justify = CENTER,bd=2)
bust_text.grid(row=11,column=2,pady=6)


# String Variable for waist
waist=StringVar()
waist_label=Label(root,text="Waist :",font=("",10))
waist_label.grid(row=12,column=1,pady=6)
waist_text=Entry(root,textvariable=waist,justify = CENTER,bd=2)
waist_text.grid(row=12,column=2,pady=6)


# String Variable for hips
hips=StringVar()
hips_label=Label(root,text="Hips :",font=("",10))
hips_label.grid(row=13,column=1,pady=6)
hips_text=Entry(root,textvariable=hips,justify = CENTER,bd=2)
hips_text.grid(row=13,column=2,pady=6)


# String Variable for hips_round
hips_round=StringVar()
hips_round_label=Label(root,text="Hips Round :",font=("",10))
hips_round_label.grid(row=14,column=1,pady=6)
hips_round_text=Entry(root,textvariable=hips_round,justify = CENTER,bd=2)
hips_round_text.grid(row=14,column=2,pady=6)


# String Variable for knee_round
knee_round=StringVar()
knee_round_label=Label(root,text="Knee Round :",font=("",10))
knee_round_label.grid(row=15,column=1,pady=6)
knee_round_text=Entry(root,textvariable=knee_round,justify = CENTER,bd=2)
knee_round_text.grid(row=15,column=2,pady=6)


# String Variable for shoulder_hips_length
shoulder_hips_length=StringVar()
shoulder_hips_length_label=Label(root,text="Shoulder Hips Length :",font=("",10))
shoulder_hips_length_label.grid(row=6,column=3,pady=6)
shoulder_hips_length_text=Entry(root,textvariable=shoulder_hips_length,justify = CENTER,bd=2)
shoulder_hips_length_text.grid(row=6,column=4,pady=6)


# String Variable for shoulder_to_waist_length
shoulder_to_waist_length=StringVar()
shoulder_to_waist_length_label=Label(root,text="Shoulder to Waist Length :",font=("",10))
shoulder_to_waist_length_label.grid(row=7,column=3,pady=6)
shoulder_to_waist_length_text=Entry(root,textvariable=shoulder_to_waist_length,justify = CENTER,bd=2)
shoulder_to_waist_length_text.grid(row=7,column=4,pady=6)


# String Variable for waist_to_knee_length
waist_to_knee_length=StringVar()
waist_to_knee_length_label=Label(root,text="Waist to Knee Length :",font=("",10))
waist_to_knee_length_label.grid(row=8,column=3,pady=6)
waist_to_knee_length_text=Entry(root,textvariable=waist_to_knee_length,justify = CENTER,bd=2)
waist_to_knee_length_text.grid(row=8,column=4,pady=6)


# String Variable for shoulder_to_knee_length
shoulder_to_knee_length=StringVar()
shoulder_to_knee_length_label=Label(root,text="Shoulder to Knee Length :",font=("",10))
shoulder_to_knee_length_label.grid(row=9,column=3,pady=6)
shoulder_to_knee_length_text=Entry(root,textvariable=shoulder_to_knee_length,justify = CENTER,bd=2)
shoulder_to_knee_length_text.grid(row=9,column=4,pady=6)


# String Variable for neck
neck=StringVar()
neck_label=Label(root,text="Neck :",font=("",10))
neck_label.grid(row=10,column=3,pady=6)
neck_text=Entry(root,textvariable=neck,justify = CENTER,bd=2)
neck_text.grid(row=10,column=4,pady=6)


# String Variable for back
back=StringVar()
back_label=Label(root,text="Back :",font=("",10))
back_label.grid(row=11,column=3,pady=6)
back_text=Entry(root,textvariable=back,justify = CENTER,bd=2)
back_text.grid(row=11,column=4,pady=6)


# String Variable for shoulder_size
shoulder_size=StringVar()
shoulder_size_label=Label(root,text="Shoulder Size :",font=("",10))
shoulder_size_label.grid(row=12,column=3,pady=6)
shoulder_size_text=Entry(root,textvariable=shoulder_size,justify = CENTER,bd=2)
shoulder_size_text.grid(row=12,column=4,pady=6)


# String Variable for hook_patti_back
hook_patti_back=StringVar()
hook_patti_back_label=Label(root,text="Hook Patti Back :",font=("",10))
hook_patti_back_label.grid(row=13,column=3,pady=6)
hook_patti_back_text=Entry(root,textvariable=hook_patti_back,justify = CENTER,bd=2)
hook_patti_back_text.grid(row=13,column=4,pady=6)


# String Variable for shoulder_to_ankle
shoulder_to_ankle=StringVar()
shoulder_to_ankle_label=Label(root,text="Shoulder to Ankle :",font=("",10))
shoulder_to_ankle_label.grid(row=14,column=3,pady=6)
shoulder_to_ankle_text=Entry(root,textvariable=shoulder_to_ankle,justify = CENTER,bd=2)
shoulder_to_ankle_text.grid(row=14,column=4,pady=6)


# String Variable for hips_to_ankle
hips_to_ankle=StringVar()
hips_to_ankle_label=Label(root,text="Hips to Ankle :",font=("",10))
hips_to_ankle_label.grid(row=15,column=3,pady=6)
hips_to_ankle_text=Entry(root,textvariable=hips_to_ankle,justify = CENTER,bd=2)
hips_to_ankle_text.grid(row=15,column=4,pady=6)

# String Variable for ankle_round
ankle_round=StringVar()
ankle_round_label=Label(root,text="Ankle Round :",font=("",10))
ankle_round_label.grid(row=16,column=3,pady=6)
ankle_round_text=Entry(root,textvariable=ankle_round,justify = CENTER,bd=2)
ankle_round_text.grid(row=16,column=4,pady=6)


# Submit Button 
submit_button=Button(root,text="Submit",font=("Helvetica",10,"bold"),command=store_data,fg="green")
submit_button.config(highlightbackground = "red", highlightcolor= "red")
submit_button.grid(row=17,column=3,pady=6,ipadx=10,ipady=2)

#Find Button
find_variable=StringVar()
find_label=Label(root,text="Find Data by Name : ",font=("Helvetica",10,"bold"),bg="#551fbd",fg="white")
find_label.grid(row=2,column=4,padx=3)
find_text=Entry(root,textvariable=find_variable,justify = CENTER,bd=2)
find_text.grid(row=2,column=5,ipadx=2,ipady=3)
find_button=Button(root,text="Find",width=10,font=("Helvetica",10,"bold"),command=find_by_name,fg="orange")
find_button.grid(row=3,column=5,pady=6)

# View all Customers Button
all_customers_button=Button(root,text="All Customers",font=("Helvetica",10,"bold"),command=get_all_customers,fg="blue")
all_customers_button.config(highlightbackground = "red", highlightcolor= "red")
all_customers_button.grid(row=17,column=2,pady=6,ipadx=10,ipady=2)

# Reset Values Button
reset_values_button=Button(root,text="Reset",font=("Helvetica",10,"bold"),command=reset_values,fg="red")
reset_values_button.grid(row=17,column=4,ipadx=10,ipady=2)
#String Variable for Amount
amount_label=Label(root,text="Amount",font=("Helvetica",16,"bold"),bg="#551fbd",fg="white",width=10)
amount_label.grid(row=5,column=6,padx=10)

amount_variable1=StringVar()
amount_text1=Entry(root,textvariable=amount_variable1,width=23,justify = CENTER,bd=2)
amount_text1.grid(row=6,column=6,pady=6)

amount_variable2=StringVar()
amount_text2=Entry(root,textvariable=amount_variable2,width=23,justify = CENTER,bd=2)
amount_text2.grid(row=7,column=6,pady=6)

amount_variable3=StringVar()
amount_text3=Entry(root,textvariable=amount_variable3,width=23,justify = CENTER,bd=2)
amount_text3.grid(row=8,column=6,pady=6)

amount_variable4=StringVar()
amount_text4=Entry(root,textvariable=amount_variable4,width=23,justify = CENTER,bd=2)
amount_text4.grid(row=9,column=6,pady=6)

amount_variable5=StringVar()
amount_text5=Entry(root,textvariable=amount_variable5,width=23,justify = CENTER,bd=2)
amount_text5.grid(row=10,column=6,pady=6)

amount_variable6=StringVar()
amount_text6=Entry(root,textvariable=amount_variable6,width=23,justify = CENTER,bd=2)
amount_text6.grid(row=11,column=6,pady=6)

amount_variable7=StringVar()
amount_text7=Entry(root,textvariable=amount_variable7,width=23,justify = CENTER,bd=2)
amount_text7.grid(row=12,column=6,pady=6)

amount_variable8=StringVar()
amount_text8=Entry(root,textvariable=amount_variable8,width=23,justify = CENTER,bd=2)
amount_text8.grid(row=13,column=6,pady=6)

amount_variable9=StringVar()
amount_text9=Entry(root,textvariable=amount_variable9,width=23,justify = CENTER,bd=2)
amount_text9.grid(row=14,column=6,pady=6)

amount_variable10=StringVar()
amount_text10=Entry(root,textvariable=amount_variable10,width=23,justify = CENTER,bd=2)
amount_text10.grid(row=15,column=6,pady=6)

amount_variable11=StringVar()
amount_text11=Entry(root,textvariable=amount_variable11,width=23,justify = CENTER,bd=2)
amount_text11.grid(row=16,column=6,pady=6)



root.mainloop()