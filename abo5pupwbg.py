import streamlit as st
import logging
import os
from PIL import Image as PILImage
from pupdatabase import update_product
from abo5s3 import *
import time
import datetime
from rembg import remove


url="https://abo5.s3.eu-central-1.amazonaws.com/"


#Header
st.title('Abo5 Product Collection Portal')

#initiating a form
productform=st.form("product", clear_on_submit=True)

#container

Productnameen = productform.container()
productnamear = productform.container()
Tags = productform.container()
category = productform.container()
subcategory = productform.container()
Retail_outlet = productform.container()
price = productform.container()
Upload = productform.container()

#Image Upload

urllist=[]
urllistp=[]
uploaded_files = Upload.file_uploader("Take Pictures or browse", type=["png","jpg","jpeg"], accept_multiple_files=True)
for uploaded_file in uploaded_files:
    img1 = PILImage.open(r"bgimage.png")
    bytes_data = uploaded_file.read()
    name=save_uploadedfile(uploaded_file)
    st.write(name)
    #upload R to s3
    s3.Bucket('abo5').upload_file(Filename=name, Key=name)
    #BG Removal
    img2 = PILImage.open(name)
    st.image(img2)
    img2=remove(img2)
    #Rotating the image to correct orientation
    img2=img2.rotate(270,expand=True)

    #Cropping the image to correct size
    img2 = img2.crop(img2.getbbox())

    #scaling the BG image to the size of the product image
    maxsize=int(max(img2.size)*1.5)
    img1=(img1.resize((maxsize,maxsize),PILImage.ANTIALIAS))
    img_w, img_h = img2.size
    bg_w, bg_h = img1.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    img1.paste(img2, offset, mask = img2)
    img1=img1.resize((1200,1200),PILImage.ANTIALIAS)
    st.image(img1,width=300)
    img1.save("converted.png", format="png")
    #upload P to s3
    #name=save_uploadedfile(img1)
    namep="processed"+name
    s3.Bucket('abo5').upload_file(Filename="converted.png", Key=name)
    urllist.append(url+name)
    urllistp.append(url+namep)
links = ", ".join(urllist)
linksp=", ".join(urllistp)
st.write(links)

#Select Category
Pro_category = category.selectbox(
    'Select Product Category',
    ('Occasions & Holidays', 'Household Gears', 'Antiques & Gifts','Cleaning & Plastics','Personal Care','Stationery & School Supplies','Accessories','MISCELLANEOUS','CLOTHES','FOOD'))

#Pro_subcategory = subcategory.selectbox(
#    'Select Product Sub-Category',
#    ('Utensils', 'Food', 'kitchenware'))

Pro_price = price.text_input('Product-Price', '')

Pro_Retail= Retail_outlet.selectbox('Select Retail Outlet',
                                    ('Store1', 'Store2', 'Store3','Store4'))


#Product Name textbox    
Pro_nameen = Productnameen. text_input('Product Name English', '')
Pro_namear = productnamear.text_input('Product Name Arabic', '')
Pro_Tags = Tags.text_input('Tags', '')

#submit button
if productform.form_submit_button("upload"):
    update_product(Product_Entry_Timestamp=datetime.datetime.now(), Product_Name_en=Pro_nameen, 
                    Product_Name_ar=Pro_namear, Product_Category=Pro_category,Tags=Pro_Tags,Retail_outlet=Pro_Retail,
                    Product_price=0.00, Product_image_R_url=links, Product_image_P_url=linksp)
    st.success("Updated")
    st.balloons()
    #   status=False

