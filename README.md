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

#### General Functions:  
**1.Registration / Login / Logout system (views.general, 6 urls and functions including success jump page)**: Whenever users signup login or logout, a automatical jump page will perform to report that the operate of user works.  
**2.Index page (view.general, 1 url and function)**: A home page including the link to product_search page, works for guests (browse only).    


#### Customer Functions: 
**1.Balance system (view.customer, 1 url and function)**: The system offer £10000 for every registration account, and the balance page allows users to check thier funding.  
**2.Basket system - add basket (views.basket_add, 2 urls and function including success jump page)**: One user could create many baskets, which means many orders (in fact many items could be added in one order).  
**3.

