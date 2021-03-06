# Small Business Assistant
Multi-tenant web application, which helps small business owners to record their business activities and analyze business performance. Multiple users use the same instance of this application and only see their own data. This application contains three main parts: maintaining product catalog, transactions batch upload, and analysis reports.
![Homepage-User's Dashboard](/static/readme/SBA-home.png)



## Table of Contents
* [Technologies Used](#technologiesused)
* [How to maintain product catalog](#catalog)
* [How to batch upload transactions](#upload)
* [How to show business performance](#reports)
* [Data Model](#datamodel)


## <a name="technologiesused"></a>Technologies Used

* Flask
* Python
* Postgres
* SQLAlchemy
* Javascript(JQuery, Ajax)
* Chart.js
* HTML
* Bootstrap



## <a name="catalog"></a>How to maintain product catalog

User can add one product by filling in the form. A product is a type of item users sale, and each product has different attribute. In additon, users can add and remove as many user-defined attributes as they want. The reason why it’s possible is that all attributes are not stored as columns in the product table but as rows in separate child table.

![Users maintain product](/static/readme/add-product.png)




## <a name="upload"></a>How to batch upload transactions

After having this product, Users can record its purchase and sales transactions. Choose a csv file to upload. The content of the file will be read by the system and return the result as a Flash massage. If some row upload failed, users can use the flash massage to correct it.

![Users upload transcations CSV file](/static/readme/upload-purchase1.png)
![Users upload transcations CSV file](/static/readme/upload-purchase2.png)
![Users upload transcations CSV file](/static/readme/upload-purchase3.png)




## <a name="reports"></a>How to show business performance

Recording business activities is only one part. The more important is to show how uesers' business performance. 


![How to show business performance](/static/readme/reports1.png)
![How to show business performance](/static/readme/reports2.png)
![How to show business performance](/static/readme/reports3.png)



## <a name="datamodel"></a>Data Model

#### Part 1


![Data Model](/static/readme/datamodel1.png)


#### Part 2


![Data Model](/static/readme/datamodel2.png)


## <a name="author"></a>Author
Sisi Wang is a software engineer, and she was a data analyst five years ago.