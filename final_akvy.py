import streamlit as st
from PIL import Image
import sys
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
sns.set()
import random
import pymongo
from pymongo import MongoClient
client =MongoClient("mongodb+srv://Vijaya:Vijju123@retailstore.7lvrs.mongodb.net/RetailStore_DB?retryWrites=true&w=majority")
d=client["RetailStore_DB"]
tp=d["Temp_perBasket"]
p=d["Product"]
cb=d["Cust_book"]
s=d["Sales"]
c=d["Customer"]
Modules=["Home","Customers","Category","Products","Customer Bookings","Sales"]
cat=["Home","Gadgets","Home Decors","Appliances","Toys","Clothes","Accessories"]
image = Image.open('./mainpage.jpeg')
selectbox = st.sidebar.selectbox("Modules",Modules)
if selectbox==Modules[0]:
    st.header("Welcome to AKVY Store" )
    st.image(image, caption='', width=800, use_column_width=800, clamp=False, channels='RGB')
elif selectbox==Modules[1]:
    st.title("CUSTOMERS")
    image = Image.open('./customers.jpeg')
    st.image(image,width=500, use_column_width=200)
    fr=c.find({},{"ID":1,"Name":1,"Email":1,"Mobile_No":1,"Status":1,"_id":0,"Date":1})
    d = pd.DataFrame(
        columns=["ID","Name","Email","Phone No","Status","Date"])
    res = c.find({})
    for i in res:
        d = d.append({"ID":i["ID"],"Name":i["Name"],"Email":i["Email"],"Phone No":i["Phone No"],
                      "Status":i["Status"],"Date":i["Date"]}, ignore_index=True)
    d.index = np.arange(1, len(d) + 1)
    st.dataframe(d)

elif selectbox==Modules[2]:
    select=st.sidebar.selectbox("Category",cat)
    if select==cat[0]:
        image = Image.open('./homepage.jpeg')
        st.image(image, caption='', width=800, use_column_width=800, clamp=False, channels='RGB')

    if select==cat[1]:
        st.title("GADGETS")
        st.write("         ")
        col1, col2 = st.beta_columns(2)

        image=Image.open("./vivophn.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Vivo V5s")
        col1.write("Display 5.50-inch (720x1280) · Processor MediaTek MT6750 · Front Camera 20MP · Rear Camera 13MP · RAM 4GB · Storage 64GB")
        col1.write("Price: 25000")
        

        image=Image.open("./laptop.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Inspiron Lenovo 14 Laptop")
        col1.write("11th Generation Intel ® Core ™ i5-1135G7 Processor (8MB Cache, up to 4.2 GHz)")
        col1.write("Price: 75000")

        image=Image.open("./tab.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Sony Tablet")
        col1.write("FHD plus Tablet ,S-pen in box")
        col1.write("Price: 20000")

        image=Image.open("./headphones.jpeg")
        col2.image(image,width=200, use_column_width=200)
        col2.header("BOAT Rockerz 400")
        col2.write("Bluetooth Headset with Mic for Phone Calls, 30 Hours Battery Life, Quick Charge, Touch Control & Alexa Voice Control – (Black)")
        col2.write("Price: 2500")

        image=Image.open("./musicsys.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("iBall Tarang Classic 2.1")
        col2.write("Multimedia Speaker with Bluetooth, USB, FM Radio & Remote Control (Black)")
        col2.write("Price: 60000")

        image=Image.open("./camera.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Camera")
        col2.write("Canon Lens RF 24-105")
        col2.write("Price: 45000")

    if select==cat[2]:
        st.title("HOME DECORS")
        st.write("         ")
        col1, col2 = st.beta_columns(2)

        image=Image.open("./beads.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Glass Beads")
        col1.write("Crystal glass beads long for living room")
        col1.write("Price: 2000")
            

        image=Image.open("./buddha.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Budhha  Statue")
        col1.write("Polyresin Budhha figurine")
        col1.write("Price: 3000")

        image=Image.open("./wallhanger.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Pink Dream Catcher")
        col1.write("pink dream catcher with long feathers ")
        col1.write("Price: 400")

        image=Image.open("./wall.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Wall painting")
        col2.write("Canvas print wall painting ")
        col2.write("Price: 5000")

        image=Image.open("./wallclk.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Wall Clock")
        col2.write("Designer metal wall clock")
        col2.write("Price: 4000")

        image=Image.open("./vase.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Fancy Flower Vase")
        col2.write("White glassed flower vase")
        col2.write("Price: 600")

    if select==cat[3]:
        st.title("APPLIANCES")
        st.write("         ")
        col1, col2 = st.beta_columns(2)

        image=Image.open("./fridge.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Samsung Refrigerator")
        col1.write("Samsung 668 L wi-Fi inverter side-by-side Refrigerator")
        col1.write("Price: 150000")
            

        image=Image.open("./oven.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Microwave Oven")
        col1.write("Philips HD6975/00 25 litre Metal Coated Digital Oven Toaster Grill")
        col1.write("Price: 25000")

        image=Image.open("./tv.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Digital TV")
        col1.write("Sony Bravia 55 inches HD smart LED")
        col1.write("Price: 57000")

        image=Image.open("./washingmac.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("LG Washing Machine")
        col2.write("LG 8 kg 5 star fully-Automatic front loading washing machine")
        col2.write("Price: 35000")

        image=Image.open("./dishwasher.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Premium Dishwasher")
        col2.write("Voltas Beko purple Dishwasher")
        col2.write("Price: 27000")

        image=Image.open("./coffee.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Coffee Maker")
        col2.write("Rohnson R-972 coffee maker")
        col2.write("Price: 4700")

        

    if select==cat[4]:
        st.title("TOYS")
        st.write("         ")
        col1, col2 = st.beta_columns(2)

        image=Image.open("./teddy.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Giant Soft Teddy")
        col1.write("Sterling giant creamy  teddy")
        col1.write("Price: 5500")
            

        image=Image.open("./car.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Red Racing Car")
        col1.write("Remote control racing car")
        col1.write("Price: 5000")

        image=Image.open("./tom.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Talking Tom")
        col1.write("White coloured Cy talking tom toy")
        col1.write("Price: 4000")

        image=Image.open("./avengers.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Avengers Toy")
        col2.write("Endgame Shield blast kit")
        col2.write("Price: 2500")

        image=Image.open("./barbie.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Pink Barbie")
        col2.write("Fairytale fashion barbie kit with bag")
        col2.write("Price: 1500")

        image=Image.open("./train.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Train Toy")
        col2.write("Remote control train")
        col2.write("Price: 3000")

    if select==cat[5]:
        st.title("CLOTHES")
        st.write("         ")
        col1, col2 = st.beta_columns(2)

        image=Image.open("./lehenga.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Rose Lehenga Choli")
        col1.write("Flaunt Enriching Fancy pink net lehenga choli ")
        col1.write("Price: 5000")
            

        image=Image.open("./frock.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Daisy Knotted Frock")
        col1.write("Dew drops sleeveless Cream frock")
        col1.write("Price: 1500")

        image=Image.open("./saree.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Exclusive Pink Saree")
        col1.write("Kanchipuram saree with Golden boarder")
        col1.write("Price: 15000")

        image=Image.open("./suit.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Cocktail Attire Suit ")
        col2.write("Formal attire suit for men")
        col2.write("Price: 4000")

        image=Image.open("./smallboy.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Zolari Boys Suit")
        col2.write("Full sleeve white and red suit")
        col2.write("Price: 2000")

        image=Image.open("./tshirt.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Tshirt")
        col2.write("Green coloured flexible t-shirt")
        col2.write("Price: 600")

    if select==cat[6]:
        st.title("ACCESSORIES")
        st.write("         ")
        col1, col2 = st.beta_columns(2)

        image=Image.open("./jewellery.jpeg")
        col1.image(image,width=250, use_column_width=200)
        col1.header("Bridal Jewellery Set")
        col1.write("Gold plated kundan jewellery set")
        col1.write("Price: 8000")
            

        image=Image.open("./cosmetics.jpeg")
        col1.image(image,width=300, use_column_width=200)
        col1.header("Makeup Kit")
        col1.write("Sugar Cosmetics all in one kit")
        col1.write("Price: 5000")

        image=Image.open("./handbag.jpeg")
        col1.image(image,width=250, use_column_width=200)
        col1.header("Gray fancy Handbag")
        col1.write("Floral nevenka handbag")
        col1.write("Price: 2000")

        image=Image.open("./wallet.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Wallet")
        col2.write("Carrken leather wallet for men")
        col2.write("Price: 1700")

        image=Image.open("./specs.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Glasses for Men")
        col2.write("Modern premium frame glasses with black ray cut")
        col2.write("Price: 1500")

        image=Image.open("./watch.jpeg")
        col2.image(image,width=300, use_column_width=200)
        col2.header("Digital Watch")
        col2.write("Realme digital black coated watch")
        col2.write("Price: 5000")

elif selectbox==Modules[3]:
    st.title("PRODUCTS")
    image = Image.open('./products.jpeg')
    st.image(image,width=500, use_column_width=200)
    fr=p.find({},{"_id":0})
    d = pd.DataFrame(columns=["ID", "Category","Model", "Name","Description","Price", "Quantity", "Ratings","Reviewer Name","Review"])
    res = p.find({})
    for i in res:
        d = d.append({"ID": i["ID"],"Category":i["Category"],"Model":i["Model"], "Name":i["Name"],"Description": i["Description"],
                      "Price": i["Price"],"Quantity":i["Quantity"],"Ratings":i["Ratings"],"Reviewer Name":i["Reviewer Name"],"Review":i["Review"]}, ignore_index=True)
    d.index = np.arange(1, len(d) + 1)
    st.dataframe(d)
elif selectbox==Modules[4]:
    st.title("CUSTOMER BOOKINGS")
    image = Image.open('./cust_bookings.jpeg')
    st.image(image,width=500, use_column_width=200)
    fr = cb.find({},{"_id":0})
    st.dataframe(fr)
elif selectbox==Modules[5]:
    st.title("SALES")
    image = Image.open('./sales.jpeg')
    st.image(image,width=500, use_column_width=200)
    #st.header("Sales")
    d = pd.DataFrame(columns=["ID", "Model", "Name", "Quantity", "Revenue"])
    res = s.find({})
    for i in res:
        d = d.append({"ID": i["ID"], "Model": i["Model"], "Name": i["Name"],
                      "Quantity": i["Quantity Sold"], "Revenue": i["Revenue"]}, ignore_index=True)
    d.index = np.arange(1, len(d) + 1)
    d = d.append(d[['Revenue']].sum().rename('TOTAL')).fillna('')
    st.dataframe(d)
    st.header("Revenue Chart")
    data = pd.DataFrame(columns=['Revenue'])
    fr = s.find({}, {"_id": 0})
    l=[]
    for i in fr:

        data = data.append({'Revenue':i["Revenue"]}, ignore_index=True)
        l.append(i["ID"])
    data.index = l

    st.bar_chart(data)
    st.header("Revenue Vs Quantity")
    df =pd.DataFrame(columns = ["ID", "Quantity", "Revenue"])
    res = s.find({})
    for i in res:
        df = df.append({"ID": i["ID"],"Quantity": i["Quantity Sold"], "Revenue": i["Revenue"]}, ignore_index = True)
    fig1 = plt.figure()
    sns.scatterplot(data=df ,x='Quantity' ,y='Revenue', hue='ID')
    st.pyplot(fig1)