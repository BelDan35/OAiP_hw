from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        super().__init__()

        group_1 = LabelFrame(self, padx=10, pady=10, text="Input")
        group_2 = LabelFrame(self, padx=10, pady=10, text="         Confidence Interval")
        group_3 = LabelFrame(self, padx=10, pady=10, text="Estimation")
        group_4 = LabelFrame(self, padx=10, pady=10, text="Output")

        group_1.grid(row=0, column=0, padx=5, pady=5)
        group_2.grid(row=0, column=1, padx=5, pady=5)
        group_3.grid(row=1, column=0, padx=5, pady=5)
        group_4.grid(row=1, column=1, padx=5, pady=5, sticky=N)

        ttk.Label(group_1, text="Data file").grid(row=0, sticky=EW, padx=5, pady=5)
        ttk.Label(group_1, text="Field X").grid(row=1, sticky=EW, padx=5, pady=5)
        ttk.Label(group_1, text="Field").grid(row=2, sticky=EW, padx=5, pady=5)
        ttk.Entry(group_1).grid(row=0, column=1, sticky=EW, padx=5, pady=5)
        ttk.Combobox(group_1).grid(row=1, column=1, sticky=EW, padx=5, pady=5, columnspan=2)
        ttk.Combobox(group_1).grid(row=2, column=1, sticky=EW, padx=5, pady=5, columnspan=2)
        ttk.Button(group_1, text="...", width=4).grid(row=0, column=2, sticky=EW)

        Label(group_2, text="Method").grid(row=0, sticky=EW, padx=5, pady=5)
        Label(group_2, text="Intervals").grid(row=1, sticky=EW, padx=5, pady=5)
        Label(group_2, text="Repeats").grid(row=2, sticky=EW,padx=5, pady=5)
        ttk.Combobox(group_2).grid(row=0, column=1, sticky=EW, padx=5, pady=5)
        ttk.Combobox(group_2).grid(row=1, column=1, sticky=EW, padx=5, pady=5)
        ttk.Spinbox(group_2, from_=1.0, to=100.0).grid(row=2, column=1, sticky=EW, padx=5, pady=5)
        Checkbutton(text="").place(x = 275, y = 2, anchor=NW)

        Label(group_3, text="Residuals").grid(row=0, sticky=NW, padx=5, pady=5)
        Label(group_3, text="Function").grid(row=1, sticky=NW, padx=5, pady=5)
        Label(group_3, text="Parameters:").grid(row=2, sticky=NW, padx=5, pady=5)
        ttk.Combobox(group_3).grid(row=0, column=1, sticky=NW, padx=5, pady=5)
        ttk.Combobox(group_3).grid(row=1, column=1, sticky=NW, padx=5, pady=5)


        self.people = [("A", 38, Checkbutton(text="")), ("k", 42, Checkbutton(text="")), ("x_0", 28, Checkbutton(text="")), ("y_0", 28, Checkbutton(text=""))]
 
        self.columns = ("Parameter", "Value", "Fixed")
        self.tree = ttk.Treeview(group_3, columns=self.columns, show="headings")
        self.tree.grid(row=3, column=0, columnspan=2, sticky=NW, padx=5, pady=5)
        
        self.tree.heading("Parameter", text="Parameter")
        self.tree.heading("Value", text="Value")
        self.tree.heading("Fixed", text="Fixed")

        self.tree.column("#1", stretch=NO, width=73)
        self.tree.column("#2", stretch=NO, width=73)
        self.tree.column("#3", stretch=NO, width=73)
        
        # добавляем данные
        for person in self.people:
            self.tree.insert("", END, values=person)


        ttk.Checkbutton(group_4, text="File").grid(row=0, column=0, sticky=EW, padx=5, pady=5)
        ttk.Entry(group_4).grid(row=0, column=1, sticky=EW, padx=5, pady=5)
        ttk.Button(group_4, text="...", width=4).grid(row=0, column=2, sticky=EW, padx=5, pady=5)
        ttk.Checkbutton(group_4, text="Auto-scale").grid(column=0, row=1, sticky=EW, padx=5, pady=5)
        ttk.Label(group_4, text="X min").grid(column=0, row=2, sticky=E, padx=5, pady=5)
        ttk.Label(group_4, text="X max").grid(column=0, row=3, sticky=E, padx=5, pady=5)
        ttk.Entry(group_4).grid(column=1, row=2, sticky=EW, padx=5, pady=5, columnspan=2)
        ttk.Entry(group_4).grid(column=1, row=3, sticky=EW, padx=5, pady=5, columnspan=2)
        ttk.Label(group_4, text="Legend location").grid(column=0, row=4, sticky=EW, padx=5, pady=5)
        ttk.Combobox(group_4).grid(column=1, row=4, sticky=EW, padx=5, pady=5, columnspan=2)


        ttk.Button(self, text="Close Plots").grid(column=0, row=3, padx=5, pady=5, sticky=W)
        ttk.Button(self, text="Close").grid(column=1, row=3, padx=85, pady=5, sticky=E)
        ttk.Button(self, text="Plot").grid(column=1, row=3, padx=5, pady=5, sticky=E)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()