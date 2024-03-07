import pandas as pd
import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',database='ADMIN')
cursor=db.cursor()

query="select * from ADMIN"
cursor.execute(query)

myalldata=cusor.fetchall()

all_product_id=[]
all_product_name=[]
all_product_brand=[]
all_product_price=[]
all_product_quantity=[]
all_product_description=[]
all_product_image=[]

for product_id,product_name,product_brand,product_price,product_quantity,product_description,product_image in myalldata():
    
    all_product_id.append(product_id)
    all_product_name.append(product_name)
    all_product_brand.append(product_brand)
    all_product_price.append(product_price)
    all_product_quantity.append(product_quantity)
    all_product_description.append(product_description)
    all_product_image.append(product_image)

dic={'product_id':all_product_id , 'product_name':all_product_name, 'product_brand':all_product_brand, 'product_price':all_product_price, 'product_quantity':all_product_quantity, 'product_description':all_product_description,'product_image':all_product_image)
df=pd.DataFrame(dic)
df_csv=df.to_csv('\E:main_file.csv')
