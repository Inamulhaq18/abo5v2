from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float 
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
import datetime
from sqlalchemy import delete

#Connecting to the database
engine = create_engine("postgresql://hkmuctkbhmlhsr:59563300aab6c650f8bbc9cc4153df6a42054b71e9be00dda420f40bbbf791b2@ec2-54-76-43-89.eu-west-1.compute.amazonaws.com:5432/dd8a5bspvhrk8c", echo = False)

#establishing a session 
Session=sessionmaker(bind=engine)
session=Session
Base=declarative_base()

class product(Base):
    __tablename__ = 'master_product_table'

    Product_id = Column(Integer, primary_key=True,autoincrement=True)
    start_time = Column(String(50),default="NA")
    user = Column(String(50),default="NA")
    Product_Name_en=Column(String(50),default="NA")
    Product_Name_ar=Column(String(50),default="NA")
    Product_Entry_Timestamp=Column(String(50),default="NA")
    Product_Category=Column(String(50),default="NA")
    Product_subcategory=Column(String(50),default="NA")
    Product_describtion_en=Column(String(500),default="NA")
    Product_describtion_ar=Column(String(500),default="NA")
    Tags=Column(String(500),default="NA")
    Retail_outlet=Column(String(50),default="NA")
    Product_image_R_url=Column(String(500),default="NA")
    Product_image_P_url=Column(String(500),default="NA")
    Product_review_status=Column(Integer,default=0)
    Product_review_TimeStamp=Column(String(50),default="NA")
    Product_approval_status=Column(Integer,default=0)
    Product_approval_TimeStamp=Column(String(50),default="NA")
    Product_live_status=Column(Integer,default=0)
    Product_live_TimeStamp=Column(String(50),default="NA")
    Product_price=Column(Float(50),default=0.00)



def update_product(Product_Name_en="NA",Product_Name_ar="NA",Product_Category="NA",
                 Product_subcategory="NA",Product_describtion_en="NA", Product_describtion_ar="NA",
                  Tags="NA",Retail_outlet="NA",Product_price=0.00, Product_image_R_url="NA",
                  Product_Entry_Timestamp=datetime.datetime.now(),Product_review_status=0,Product_image_P_url="NA",user="NA"):
    #hours_added = datetime.timedelta(hours = 3)
    row1=product( Product_Name_en=Product_Name_en, Product_Name_ar=Product_Name_ar,
                  Product_Entry_Timestamp=datetime.datetime.now() ,Product_Category=Product_Category, Product_subcategory=Product_subcategory, Product_describtion_en=Product_describtion_en, Product_describtion_ar=Product_describtion_ar, Tags=Tags, Retail_outlet=Retail_outlet, Product_price=Product_price, Product_image_R_url=Product_image_R_url, Product_image_P_url=Product_image_P_url, user=user)
    with Session() as session:
        session.add(row1) 
        session.commit()

