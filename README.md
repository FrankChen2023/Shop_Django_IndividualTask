## Shop_Django_IndividualTask

### Development logs:  
**11th April Complete Version:da4b3a9** : Start project, basic website setting, one adding data function.  
**12th April to 13th April Complete Version:1d64744** : Add basic product and search function.  
**13th April Complete Version:fc8cceb** : Complete login signup system, with customer and admin account creation.  
**15th April Complete Version:fcb9809** : Complete basket creation function.  
**15th April Complete Version:6cb8b77** : Add auto skip pages after login, logout and creating new basket.  
**16th April to 17th April Complete Version:132282e** : Function picking item into basket completes and added.    
**17th April Complete Version:755093a** : Basket details function added, and rebuild the structure of code work (more clear classification).  
**18th April Complete Version:44e7a76** : A url link represents success page with auto-jump function added after creating new basket.  
**18th April Complete Version:640e09c** : Add filter with type condition to item_add and product_search pages.  
**18th April Complete Version:0e7063b** : Basket status, edit and delete functions added.  
**19th April Complete Version:e24b42e** : Item edit function added.  
**19th April Complete Version:b99046f** : Payment function added, with total cost caiculated and posted automatically.   
**21st April Complete Version:9e1f3bb** : Admin functions added, including checking all tables in two different ways, modifying contents, deleting rows, adding new products and so on.  
**21st April Complete Version:5999cf3** : Sorting data by upward and backward functions added.  


### Application Introduction:  
## Amazing Shopping Website Application (created by Frank Chen) 
This application achieves seearching items for guests, purchasing items for customers, managed website for administrators.  
This application 41 pages (urls)
**System: Many users, while each user can create many baskets (which means orders. I could make another order after I have made one, just like Amazon shopping, I could add several things into my basket and make payment together, and after that I could buy something else and repeat the steps.), each basket could include many items. Therefore, customer, basket and item tables are linked: customer (1 to many) basket, while basket (1 to many) item.
Tables:  
User: username / password (in django_auth, login only)  
Customer: username / account balance / email (personal details)  
Product (things on sale): name / type / price / amount (amount decreases if someone buy this product)  
Basket: username / Consignee / basketname (user can name and rename their basket freely) / address / status (paid or unpaid)  
Basket_detail (items): Things in customers' baskets. Including nearly all attributes above.   


**(Please distinguish products and items: products means things on sale, while items means things in customers' baskets (orders).**  
#### General Functions:  
**1.Registration / Login / Logout system (views.general, 6 urls and functions including success jump page)**: Whenever users signup login or logout, a automatical jump page will perform to report that the operate of user works.  
**2.Index page (view.general, 1 url and function)**: A home page including the link to product_search page, works for guests (browse only).    


#### Customer Functions:  
**Create basket (fill your personal details, consignee and address) -> add items into the basket -> check the basket (edit, add more items, change amount of a certain item, or delete) -> make payment (then no edit or modification is allowed)** 
**1.Balance system (view.customer, 1 url and function)**: The system offer £10000 for every registration account, and the balance page allows users to check thier funding.  
**2.Basket system - add basket (views.basket_add, 2 urls and functions including success jump page)**: Allows users to create many baskets, which means many orders (in fact many items could be added in one order).  
**3.Basket system - delete basket (views.basket_delete, 2 urls and functions including success jump page)**: Allows users to delete their baskets which are unpaid. If the baskets have been paid, which means successful orders, they will not be able to deleted by users directly.
**4.Basket system - basket detail / edit / payment / item edit (views.basket, 4 urls and functions)**: Allows users to check their baskets. The items in it, and the payment status. Besides, if the users want, they could find edit basket details, edit items details, make payment, and even delete the basket in this page, and of course for unpaid baskets.
**5.Item system - item detail / add / edit / delete (views.item, 4 urls and functions)**: Allows users to check each item record, and add new items into the basket, or edit items' contents (especially amount), or remove it from the basket.  

#### Staff Functions:  
**Check member account / modify account details / check all baskets or search baskets under a certain account / check all orders (items) or search items under a certain account's basket / add new products / edit price, type or amount of products**  
**1.Admin_console (view.staff_admin_console, 1 url with function)**: The main page of staff account.  
**2.Two models to check lists:**  
    a. Model 1: Check customers first, and click customer to check baskets under it, and click basket to check items in it. (Check in order, but can not see all            contents together, which is used for convenience.)  
    b. Model 2: Check 4 lists directly, and see all contents together, while a search function offered for convenience.  
    c. Both in two models, staff is allowed to edit the lists, change content or delete rows.  
**3.Product add / edit**: Allows staff to change the details (amount, price or other details) of products on sale, and add new products for sale.  
