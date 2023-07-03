from tkinter import *
root1=Tk()
root1.geometry("400x555")
l1=Label(root1,text="Dev Designer",fg="white",bg="#551fbd",font=("Helvetica",16,"bold"),width=30)
l1.grid(row=1,column=1,pady=10)
p=[]
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
name_ans=Label(second_frame,text=f"{p}")
name_ans.grid(row=2,column=2)
address_label=Label(second_frame,text="Address : ",font=("Helvetica",11))
address_label.grid(row=3,column=1,padx=20,pady=6)
address_ans=Label(second_frame,text=f"{p}")
address_ans.grid(row=3,column=2)
district_label=Label(second_frame,text="District : ",font=("Helvetica",11))
district_label.grid(row=4,column=1,padx=20,pady=6)
district_ans=Label(second_frame,text=f"{p}")
district_ans.grid(row=4,column=2)
distription_label=Label(second_frame,text="Discription",font=("Helvetica",16,"bold"),bg="#551fbd",fg="yellow",width=10)
distription_label.grid(row=5,column=1,padx=10)
measurment_label=Label(second_frame,text="Measurment",font=("Helvetica",15,"bold"),bg="#551fbd",fg="yellow",width=10)
measurment_label.grid(row=5,column=2)

length_label=Label(second_frame,text="Length :",font=("times",13))
length_label.grid(row=6,column=1)
length_ans=Label(second_frame,text=f"{p}")
length_ans.grid(row=6,column=2)

shoulder_label=Label(second_frame,text="Shoulder :",font=("times",13))
shoulder_label.grid(row=7,column=1)
shoulder_ans=Label(second_frame,text=f"{p}")
shoulder_ans.grid(row=7,column=2)


sleave_length_label=Label(second_frame,text="Sleave length :",font=("times",13))
sleave_length_label.grid(row=9,column=1)
sleave_length_ans=Label(second_frame,text=f"{p}")
sleave_length_ans.grid(row=9,column=2)

round_sleave_label=Label(second_frame,text="Round Sleave :",font=("times",13))
round_sleave_label.grid(row=10,column=1)
round_sleave_ans=Label(second_frame,text=f"{p}")
round_sleave_ans.grid(row=10,column=2)

arm_hole_label=Label(second_frame,text="Arm Hole :",font=("times",13))
arm_hole_label.grid(row=11,column=1)
arm_hole_ans=Label(second_frame,text=f"{p}")
arm_hole_ans.grid(row=11,column=2)

bust_label=Label(second_frame,text="Bust :",font=("times",13))
bust_label.grid(row=12,column=1)
bust_ans=Label(second_frame,text=f"{p}")
bust_ans.grid(row=12,column=2)

waist_label=Label(second_frame,text="Waist :",font=("times",13))
waist_label.grid(row=13,column=1)
waist_ans=Label(second_frame,text=f"{p}")
waist_ans.grid(row=13,column=2)

hips_label=Label(second_frame,text="Hips :",font=("times",13))
hips_label.grid(row=14,column=1)
hips_ans=Label(second_frame,text=f"{p}")
hips_ans.grid(row=14,column=2)

hips_round_label=Label(second_frame,text="Hips Round :",font=("times",13))
hips_round_label.grid(row=15,column=1)
hips_round_ans=Label(second_frame,text=f"{p}")
hips_round_ans.grid(row=15,column=2)

knee_round_label=Label(second_frame,text="Knee Round :",font=("times",13))
knee_round_label.grid(row=16,column=1)
knee_round_ans=Label(second_frame,text=f"{p}")
knee_round_ans.grid(row=16,column=2)

shoulder_hips_length_label=Label(second_frame,text="Shoulder hips Length :",font=("times",13))
shoulder_hips_length_label.grid(row=17,column=1)
shoulder_hips_length_ans=Label(second_frame,text=f"{p}")
shoulder_hips_length_ans.grid(row=17,column=2)

shoulder_to_waist_length_label=Label(second_frame,text="Shoulder to Waist Length :",font=("times",13))
shoulder_to_waist_length_label.grid(row=18,column=1)
shoulder_to_waist_length_ans=Label(second_frame,text=f"{p}")
shoulder_to_waist_length_ans.grid(row=18,column=2)

waist_to_knee_label=Label(second_frame,text="Waist to Knee :",font=("times",13))
waist_to_knee_label.grid(row=19,column=1)
waist_to_knee_ans=Label(second_frame,text=f"{p}")
waist_to_knee_ans.grid(row=19,column=2)

shoulder_to_knee_length_label=Label(second_frame,text="Shoulder to Knee Length :",font=("times",13))
shoulder_to_knee_length_label.grid(row=20,column=1)
shoulder_to_knee_length_ans=Label(second_frame,text=f"{p}")
shoulder_to_knee_length_ans.grid(row=20,column=2)

neck_label=Label(second_frame,text="Neck :",font=("times",13))
neck_label.grid(row=21,column=1)
neck_ans=Label(second_frame,text=f"{p}")
neck_ans.grid(row=21,column=2)

back_label=Label(second_frame,text="Back :",font=("times",13))
back_label.grid(row=22,column=1)
back_ans=Label(second_frame,text=f"{p}")
back_ans.grid(row=22,column=2)

shoulder_size_label=Label(second_frame,text="Shoulder Size :",font=("times",13))
shoulder_size_label.grid(row=23,column=1)
shoulder_size_ans=Label(second_frame,text=f"{p}")
shoulder_size_ans.grid(row=23,column=2)

hook_patti_back_label=Label(second_frame,text="Hook Patti Back :",font=("times",13))
hook_patti_back_label.grid(row=24,column=1)
hook_patti_back_ans=Label(second_frame,text=f"{p}")
hook_patti_back_ans.grid(row=24,column=2)

shoulder_to_ankle_label=Label(second_frame,text="Shoulder to Ankle :",font=("times",13))
shoulder_to_ankle_label.grid(row=25,column=1)
shoulder_to_ankle_ans=Label(second_frame,text=f"{p}")
shoulder_to_ankle_ans.grid(row=25,column=2)

hips_to_ankle_label=Label(second_frame,text="Hips to Ankle :",font=("times",13))
hips_to_ankle_label.grid(row=26,column=1)
hips_to_ankle_ans=Label(second_frame,text=f"{p}")
hips_to_ankle_ans.grid(row=26,column=2)

ankle_round_label=Label(second_frame,text="Ankle Round :",font=("times",13))
ankle_round_label.grid(row=6,column=1)
ankle_round_ans=Label(second_frame,text=f"{p}")
ankle_round_ans.grid(row=6,column=2)

root1.mainloop()