# Small Business Assistant
Multi-tenant web application, which helps small business owners to record their business activities and analyze business performance. Multiple users use the same instance of this application and only see their own data. This app contains three main parts: maintaining product catalog, transactions batch upload, and analysis reports.
![Homepage-User's Dashboard](/static/SBA-home.png)



## Table of Contents
* [Technologies Used](#technologiesused)
* [How to maintain product catalog](#catalog)
* [How to batch upload transactions](#upload)
* [How to analyze business performance](#use)


## <a name="technologiesused"></a>Technologies Used

* Flask
* Python
* Postgres
* SQLAlchemy
* Javascript(JQuery, Ajax)
* Chart.js
* HTML
* Bootstrap

(dependencies are listed in requirements.txt)

## <a name="catalog"></a>How to maintain product catalog

User can add one product by filling in the form. A product is a type of item users sale, and each product has different attribute. In additon, users can add and remove as many user-defined attributes as they want. The reason why it’s possible is that all attributes are not stored as columns in the product table but as rows in separate child table.

![Users maintain product](/static/SBA-home.png)


## <a name="upload"></a>How to batch upload transactions

The walking directions will also slide down at this time. 



## <a name="author"></a>Author
Sisi Wang is a software engineer, and she was a data analyst five years ago.