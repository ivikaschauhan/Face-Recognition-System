search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        reset_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=4,padx=4)
