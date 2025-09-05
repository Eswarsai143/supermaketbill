from datetime import datetime
n=input("enter customer name:")
lists='''
onion        RS 50/kg
chocolates   RS 20/each
Buttermilk   Rs 20/each
coconutwater RS 50/bottle
Maggi Packet RS 80/packet
Toys         RS 200/each
Milk         RS 35/li
'''
print(lists)
price=0
pricelist=[]
totalprice=0
finalprice=0
Ilist=[]
qlist=[]
plist=[]
items={'onion':50,'chocolates':20,'Buttermilk':20,'coconutwate':50,'Maggi Packet':80,'Toys':200,'Milk':35}
option=int(input("for list press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy  press 1 or to exit press 2:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("what  do you want to buy:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity * (items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            Ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("entered items are not available")
    else:
        print("ypu entered wrong number")
    inp=input("can  i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25 * "=" "eswar supermarket" ,25 *"=")
            print(28 * "=" "wanaparthy")
            print("Name:",n,30* " ","Date:",datetime.now())
            print(75 *"-")
            print("sno",8*" ",'items',8* " ",'quantity',3*" ","price")
            for i in range(len(pricelist)):
                print(i,5* ' ',Ilist[i], 3* " ",qlist[i],8 *" ",  plist[i])
            print(75*"-")
            print(50*'',"Totalaamount:","RS",totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*" -")
            print(50 *" ", 'finalamount:',"Rs",totalprice)
            print(75*" -")
            print(50*" -" ,"Thanks for visiting")

        
