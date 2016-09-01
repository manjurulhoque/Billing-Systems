from tkinter import *
from tkinter import messagebox
import random
import time
import datetime

root = Tk()
root.geometry('1350x700+0+0')
root.title("Billing Systems")

Tops = Frame(root, width=1350, height=100, bd=2, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, bd=2, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=700, bd=2, relief="raise")
f2.pack(side=LEFT)

f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=8, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=8, relief="raise")
f2ab.pack(side=LEFT)

lblInfo = Label(Tops, font=("Arial", 60, 'bold'), text="      Online Billing Systems      ", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

# Calculator
text_Input = StringVar()
operator = ""
PaymentRef = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Carpets = StringVar()
Fabric = StringVar()
Blinds = StringVar()
HomeDelivery = StringVar()
OrderDate = StringVar()
CostofCarpets = StringVar()
CostofFabric = StringVar()
CostofBlinds = StringVar()
CostofDelivery = StringVar()

OrderDate.set(time.strftime("%d/%m/%y"))


def Exit():
    qExit = messagebox.askyesno("Billing systems", "Do you want to really exit?")
    if qExit > 0:
        root.destroy()
        return


def reset():
    PaymentRef.set("")
    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Carpets.set("")
    Fabric.set("")
    Blinds.set("")
    HomeDelivery.set("")
    OrderDate.set(time.strftime("%d/%m/%y"))
    CostofCarpets.set("")
    CostofFabric.set("")
    CostofBlinds.set("")
    CostofDelivery.set("")


def costoforeder():
    carpetprice = float(Carpets.get())
    blindsprice = float(Blinds.get())
    fabricprice = float(Fabric.get())
    deliverycost = float(HomeDelivery.get())

    carpetcost = "$ ", str('%.2f' % (carpetprice * 15.49))
    CostofCarpets.set(carpetcost)

    blindcost = "$ ", str('%.2f' % (blindsprice * 15.49))
    CostofBlinds.set(blindcost)

    fabriccost = "$ ", str('%.2f' % (fabricprice * 15.49))
    CostofFabric.set(fabriccost)

    delivery = "$ ", str('%.2f' % ((deliverycost * 15.49)))
    CostofDelivery.set(delivery)

    ToC = "$ ", str(
        '%.2f' % ((carpetprice * 15.50) + (blindsprice * 7.49) + (fabricprice * 5.50) + (deliverycost * 4.50)))
    SubTotal.set(ToC)
    Tax = "$ ", str(
        '%.2f' % (((carpetprice * 15.50) + (blindsprice * 7.49) + (fabricprice * 5.50) + (deliverycost * 4.50)) * 0.2))

    PaidTax.set(Tax)
    TaxPay = (((carpetprice * 15.50) + (blindsprice * 7.49) + (fabricprice * 5.50) + (deliverycost * 4.50)) * 0.2)
    Cost = ((carpetprice * 15.50) + (blindsprice * 7.49) + (fabricprice * 5.50) + (deliverycost * 4.50))
    CostOfItems = "$ ", str('%.2f' % (TaxPay + Cost))
    TotalCost.set(CostOfItems)

    payreference()


def payreference():
    x = random.randint(10034, 699812)
    randomRef = str(x)
    PaymentRef.set("BILL " + randomRef)


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=6, insertwidth=6, justify='left')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7",
              command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8",
              command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9",
              command=lambda: btnClick(9)).grid(row=1, column=2)
btnPlus = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+",
                 command=lambda: btnClick("+")).grid(row=1, column=3)

btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4",
              command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5",
              command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6",
              command=lambda: btnClick(6)).grid(row=2, column=2)
btnSub = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-",
                command=lambda: btnClick("-")).grid(row=2, column=3)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1",
              command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2",
              command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3",
              command=lambda: btnClick(3)).grid(row=3, column=2)
btnMulti = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*",
                  command=lambda: btnClick("*")).grid(row=3, column=3)

btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0",
              command=lambda: btnClick(0)).grid(row=4, column=0)
btnClear = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C",
                  command=btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=",
                   command=btnEqualInput).grid(row=4, column=2)
btnDiv = Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/",
                command=lambda: btnClick("/")).grid(row=4, column=3)

# -------------- f1aa------------

lblSalesReference = Label(f1aa, font=('arial', 16, 'bold'), text="Sales Reference", bd=16, justify="left")
lblSalesReference.grid(row=0, column=0)
txtSalesReference = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=PaymentRef, bd=10, insertwidth=2,
                          justify="left")
txtSalesReference.grid(row=0, column=1)

lblCarpets = Label(f1aa, font=('arial', 16, 'bold'), text="Carpets", bd=16, justify="left")
lblCarpets.grid(row=1, column=0)
txtCarpets = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=Carpets, bd=10, insertwidth=2, justify="left")
txtCarpets.grid(row=1, column=1)

lblFabric = Label(f1aa, font=('arial', 16, 'bold'), text="Fabric", bd=16, justify="left")
lblFabric.grid(row=2, column=0)
txtFabric = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=Fabric, bd=10, insertwidth=2, justify="left")
txtFabric.grid(row=2, column=1)

lblBlinds = Label(f1aa, font=('arial', 16, 'bold'), text="Blinds", bd=16, justify="left")
lblBlinds.grid(row=3, column=0)
txtBlinds = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=Blinds, bd=10, insertwidth=2, justify="left")
txtBlinds.grid(row=3, column=1)

lblHomeDelivery = Label(f1aa, font=('arial', 16, 'bold'), text="Home Delivery", bd=16, justify="left")
lblHomeDelivery.grid(row=4, column=0)
txtHomeDelivery = Entry(f1aa, font=('arial', 16, 'bold'), textvariable=HomeDelivery, bd=10, insertwidth=2,
                        justify="left")
txtHomeDelivery.grid(row=4, column=1)

# ----------------------f1ab------------

lblOrderDate = Label(f1ab, font=('arial', 16, 'bold'), text="Order Date", bd=16, justify="left")
lblOrderDate.grid(row=0, column=0)
txtOrderDate = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=OrderDate, bd=10, insertwidth=2,
                     justify="left")
txtOrderDate.grid(row=0, column=1)

lblCostOfCarpets = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Carpets", bd=16, justify="left")
lblCostOfCarpets.grid(row=1, column=0)
txtCostOfCarpets = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=CostofCarpets, bd=10, insertwidth=2,
                         justify="left")
txtCostOfCarpets.grid(row=1, column=1)

lblCostOfFabric = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Fabric", bd=16, justify="left")
lblCostOfFabric.grid(row=2, column=0)
txtCostOfFabric = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=CostofFabric, bd=10, insertwidth=2,
                        justify="left")
txtCostOfFabric.grid(row=2, column=1)

lblCostOfBlinds = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Blinds", bd=16, justify="left")
lblCostOfBlinds.grid(row=3, column=0)
txtCostOfBlinds = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=CostofBlinds, bd=10, insertwidth=2,
                        justify="left")
txtCostOfBlinds.grid(row=3, column=1)

lblCostOfDelivery = Label(f1ab, font=('arial', 16, 'bold'), text="Cost of Delivery", bd=16, justify="left")
lblCostOfDelivery.grid(row=4, column=0)
txtCostOfDelivery = Entry(f1ab, font=('arial', 16, 'bold'), textvariable=CostofDelivery, bd=10, insertwidth=2,
                          justify="left")
txtCostOfDelivery.grid(row=4, column=1)

# ----f2aa------

lblPaidTax = Label(f2aa, font=('arial', 16, 'bold'), text="Paid Tax", bd=16, justify="left")
lblPaidTax.grid(row=1, column=0)
txtPaidTax = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=PaidTax, bd=10, insertwidth=2, justify="left")
txtPaidTax.grid(row=1, column=1)

lblSubTotal = Label(f2aa, font=('arial', 16, 'bold'), text="Sub Total", bd=16, justify="left")
lblSubTotal.grid(row=2, column=0)
txtSubTotal = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=2, justify="left")
txtSubTotal.grid(row=2, column=1)

lblTotalCost = Label(f2aa, font=('arial', 16, 'bold'), text="Total Cost", bd=16, justify="left")
lblTotalCost.grid(row=3, column=0)
txtTotalCost = Entry(f2aa, font=('arial', 16, 'bold'), textvariable=TotalCost, bd=10, insertwidth=2, justify="left")
txtTotalCost.grid(row=3, column=1)

# ---- f2ab -------
btnTotal = Button(f2ab, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), width=15,
                  text="Total Cost", command=costoforeder).grid(row=0, column=0)
btnRefer = Button(f2ab, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), width=15,
                  text="Sales Reference", command=payreference).grid(row=0, column=1)
btnReset = Button(f2ab, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), width=15,
                  text="Reset", command=reset).grid(row=1, column=0)
btnExit = Button(f2ab, padx=16, pady=16, bd=4, fg="black", font=('arial', 20, 'bold'), width=15,
                 text="Exit", command=Exit).grid(row=1, column=1)

root.mainloop()
