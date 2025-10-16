import csv
import tkinter as tk
from tkinter import Frame, Label, Button, messagebox
from datetime import datetime

purchase_dict = {} 
client = ''

def get_product_list():
 """
 This function reads the product.csv file and populates a dictionary with the information it contains
 """      
 try:           
    product_list = {}
   
    with open('products.csv','r') as csv_file:
   
         
     reader = csv.reader(csv_file,delimiter=',')

     next(reader)

     for row in reader:
            if len(row) !=0:
                key = row[1] #getting key as the product name and not key[0] that is the product id 
                product_list[key] = row
     return product_list       
     
 except FileNotFoundError as file_err:
        #message box will create an Alert Window 
        messagebox.showinfo("Atention", "Product File was not found. Please verify that before continuing!")  
def get_purchase_sum(product_price,products_amount):
      """
      This function gets the result from a purchase multiplying amount of products per price and converting that 
      into a float number
      """
      purchase_sum = float(product_price*products_amount)
      return purchase_sum


def main():
    """
    This is the main function that creates the main frame of the program to be worked later by the 
    setup_main function
    """  
    root= tk.Tk()
    root.option_add("*Font","Arial 14")
   
    frm_main=Frame(root, bg='#abccd4')
    frm_main.master.title('Supermarket Ticket Maker')
    
    frm_main.pack(padx=3,pady=3,fill= tk.BOTH,expand=True)
    

    setup_main(frm_main)

    frm_main.mainloop() #keep program runing until the user closes it 




def setup_main(frm):
    """
    This function will contain all the labels, buttons and entry fields as well as some functions to make 
    it work
    """
    lbl_welcome = Label(frm, text="", background='#abccd4')
    lbl_welcome.grid(row=0,column=0, pady=20)
    lbl_client = Label(frm,text="Enter Client ID", bg= '#abccd4')
    lbl_client.grid(row=1,column=0, padx=3 , pady=3)
    client_entry = tk.Entry(frm,width=30)
    client_entry.grid(row=1,column=1, padx=3, pady=3)
    
  
    lbl_item = Label(frm,text="Enter the Item ordered ", bg= '#abccd4')
    lbl_item.grid(row=2,column=0, padx=3 , pady=3)
    product_entry = tk.Entry(frm,width=30)
    product_entry.grid(row=2,column=1,padx=3,pady=3)


    lbl_count = Label(frm,text="Enter de amount of items ordered " ,bg= '#abccd4')
    lbl_count.grid(row=3,column=0)
    quantity_entry = tk.Entry(frm,width=30)
    quantity_entry.grid(row=3,column=1)
    
   

    

    def get_purchase_list():
      """
      This function populates a dictionary with the products and amount of products given by the 
      user  
      """    
      try:     
        current_purchase = ''
        product_name = product_entry.get()
        amount_product = quantity_entry.get()
   #     
        isEmpty = False
    
        while product_name !='' and amount_product !='':  
          isEmpty = True
          
  
          purchase_dict.update({product_name:amount_product})
       
          

 
          for key, value in purchase_dict.items():
                current_purchase += f'{key} {value}\n'
                lbl_purchase.config(text=f'{current_purchase}')  
          break    
   
       
        return purchase_dict 

      
      except TypeError as type_err:      
           messagebox.showinfo("Atention", "Please enter a valid Entry")  
      except ValueError as value_err:
           messagebox.showinfo("Atention", "Please enter a right value!")  
   
          
           
    def welcome_message(filename):
         """
         This function evaluates if the Client ID already exists in the Database of Clients
         In this case the clients csv file given when the function is called 
         """
         integer_id = client_entry.get()
         with open(filename,'rt') as csv_file:
            
            reader = csv.reader(csv_file,delimiter=',')
            
            for row in reader:
                     
                if len(row)!=0:
                  
                   id = row[0]   
                   name = row[1]
                   surname = row[2]
                   full_name = name + surname
                if integer_id ==id:
                     lbl_welcome.config(text=f'Welcome {full_name}')   
                     return
            if integer_id !=id:  
                lbl_welcome.config(text='Welcome for the first time!')       
                       
 

    def clear_entry(product_entry,quantity_entry):
                """
                This function clears the entry of product and amount of products when user adds a new
                item using the delete method
                """
                product_entry.delete(0,tk.END)
                quantity_entry.delete(0,tk.END)   
 
   

    def calculate_total(product_list, purchase_dict): 
     """
     This function calculates the price of the purchase of the client
     """
     try:   
       
       purchase_sum = 0
  
       for key, value in purchase_dict.items():
          products_amount = int(value)  #the value is the amount of items purchased
          if key in product_list:
            product_price = float(product_list[key][2])

            purchase_sum += get_purchase_sum(product_price,products_amount)
            product_subtotal = get_purchase_sum(product_price,products_amount)
            """
            This could work too without the get_purchase_sum() function 
            purchase_sum += float(product_price*products_amount)
            product_subtotal = float(product_price*products_amount)   #getting total price per product
            """
          
          else:
                
            lbl_total.config(text=f'Please enter a valid product')        
       lbl_total.config(text=f'Total price: ${purchase_sum}')  
    
       def print_ticket():
          """
          This function creates or modify a txt file with the purchase information
          """   
          purchase_list = get_purchase_list()
          
          current_purchase = ''
          for key, value in purchase_list.items():
                
                            
              current_purchase += f'{value} {key} Individual Price: ${product_price} Total per Product: ${product_subtotal}\n'
              total = f'{purchase_sum}'
              now = datetime.now() 
              new_ticket = 'ticket.txt'
              with open(new_ticket,'w') as ticket:
               ticket.write('*********************************************************\n')
               ticket.write('Supermarket Inc\n')
               ticket.write('*********************************************************\n')
               
               ticket.write(current_purchase) 
               ticket.write(f'Total price is ${total}\n') 
               ticket.write('********************************************************\n')
               ticket.write(f'{now.ctime()}\n') 
               ticket.write('********************************************************\n')    
       print_ticket() 
     
       return purchase_sum    
     except ValueError as value_err:
        messagebox.showinfo("Atention", "Please enter a right value!")  
     except NameError as name_err:
         messagebox.showinfo("Atention", "Please enter a valid product!")  
   
    # Buttons that use a lamda function are meant to avoid the execution of the function until user clicks 
    btn_add_items = Button(frm,text="Add Items", command=lambda: (get_purchase_list(),clear_entry(product_entry,quantity_entry)))
    btn_add_items.grid(pady=20)
    result = tk.Label(frm, text="")
    result.grid(pady=5)
    btn_add_items.grid(row=4 ,column=0)
    lbl_purchase= Label(frm,text="")
    lbl_purchase.grid(row=5,column=0) 
   

    btn_finish_purchase = Button(frm,text="Calculate Total", command= lambda: calculate_total(product_list=get_product_list(),purchase_dict=get_purchase_list()))
    btn_finish_purchase.grid(row=6,column=0, pady=20)
    lbl_total = Label(frm,text='')
    lbl_total.grid(row=6,column=1,pady=20)
    btn_enter_client_id = Button(frm,text='Confirm Client ID', command=lambda: (welcome_message('clients.csv')),padx=20)
    btn_enter_client_id.grid(row=1,column=2)
    btn_enter_new__client = Button(frm,text="New Client/Reset" , command= lambda: clear_entries(purchase_dict=get_purchase_list()))
    btn_enter_new__client.grid(row=7, column=0, pady=20 )

    def clear_entries(purchase_dict):
        """
        This function will clear txt file information and all entries to start again with a new client
        or by re-entering data after a mistake
        """       
        purchase_dict.clear()  
        client_entry.delete(0,tk.END) 
        lbl_total.config(text='')
        lbl_purchase.config(text='')
        lbl_welcome.config(text='')

        new_ticket = 'ticket.txt'
        with open(new_ticket,'w') as ticket:
               ticket.write('*********************************************************\n')
               ticket.write('Supermarket Inc\n')
               ticket.write('*********************************************************\n')
               
               ticket.write('') 
               ticket.write(f'') 
               ticket.write('********************************************************\n')
               ticket.write(f'') 
               ticket.write('********************************************************\n')  

  


   


            
    





if __name__ == "__main__":
    main()
