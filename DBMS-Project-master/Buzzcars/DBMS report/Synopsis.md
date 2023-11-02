# Team Members
1. Rahul Googikoll [1AM19CS158]
2. Rahul Mishra [1AM19CS159]
3. Saurav Kumar [1AM19CS195]
4. Om Prakash Jha [1AM19CS133]


# Introduction
## 1.1 Project outline
This application is going to be used by:
1. Employees
2. Customer

This application is meant for users (Employees and Customers) who can access the information from database about car deals. Our objective is so that executives and administrators can easily automate their work with less effort. For example they can generate quotations for any enquiry for a car in no time. They can also have the customer’s feedback to the show room authority regarding show room services.

## 1.2 Project Goals
The System should be capable of performing the following:
- Store basic information regarding cars, employees, customers, accessories and services provided by the organization.
- Store salary information of employees (entered by the team leaders in each city) such as, working hours, salary per hour, salary before tax, tax percentage, total amount of tax paid , salary after tax, social security fee, on monthly basis
- Help employees automate the billing process by quickly fetching car/accessory details from the database.
- System should be able to generate invoices and maintain transaction details.
- Should be able to list the inventory of cars currently available in a dealership.
- Should help customers to access car details like model, make, engine no., price etc.
- Help the organization to maintain customer details like customer name, transaction/purchase details, car purchased, purchase medium, purchase date etc.
- Display details of various dealerships of the same franchise/organization like, profits, dealership name, number of cars in dealership, number of employees etc.


# System Specifications

## 2.1 Hardware requirements
	
### Minimum requirements :
- ***processor:***  `Intel Pentium 4/ AMD Athlon series`
- ***RAM:*** `512MB`
- ***Storage:*** `100MB`
	
### Recommended requirements:
- ***processor:***  `Intel 11th generation I-series/AMD Ryzen Threadripper series`
- ***RAM:*** `8GB`
- ***Storage:*** `500GB`
	
## 2.2 Software requirements
*OS:*`Windows,GNU/Linux Distributions, Mac OS, BSD, 64-bit`

### Tech stack used:
#### *Front end:* `HTML5, CSS, JS`
- **HTML5**:

	 HTML5 is a markup language used for structuring and presenting content on the World Wide Web. It is the fifth and last major HTML version that is a World Wide Web Consortium recommendation. The current specification is known as the HTML Living Standard.
	
- **CSS**:
	CSS3 is **the latest version of the CSS specification**. CSS3 adds several new styling features and improvements to enhance the web presentation capabilities. Note: Our CSS tutorial will help you to learn the fundamentals of the latest CSS3 language, from the basic to advanced topics step-by-step.
	
- **JS**:
	JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS. Over 97% of websites use JavaScript on the client side for web page behavior, often incorporating third-party libraries.

#### *Back end:* `Django, SQLite3`

- **Django**:
	Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

- **SQLite3**:
	SQLite is a C-language library that implements a [small](https://www.sqlite.org/footprint.html), [fast](https://www.sqlite.org/fasterthanfs.html), [self-contained](https://www.sqlite.org/selfcontained.html), [high-reliability](https://www.sqlite.org/hirely.html), [full-featured](https://www.sqlite.org/fullsql.html), SQL database engine. SQLite is the [most used](https://www.sqlite.org/mostdeployed.html) database engine in the world. SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.
	
	
# Design

## 3.1 Development model:
![[Pasted image 20211211220530.png]]

- **Requirement Analysis**:
	All possible requirements of the system to be developed are captured in this phase and documented in a requirement specification document.
	
- **Design stage**:
	The requirement specifications from first phase are studied in this phase and the system design is prepared. This system design helps in specifying hardware and system requirements and helps in defining the overall system architecture.
	
- **Implementation**:
	With inputs from the system design, the system is first developed in small programs called units, which are integrated in the next phase. Each unit is developed and tested for its functionality, which is referred to as Unit Testing.

- **Integration and Testing**:
	All the units developed in the implementation phase are integrated into a system after testing of each unit. Post integration the entire system is tested for any faults and failures.

- **Deployment of System**:
	Once the functional and non-functional testing is done; the product is deployed in the customer environment or released into the market.
	
- **Maintenance**:
	There are some issues which come up in the client environment. To fix those issues, patches are released. Also to enhance the product some better versions are released. Maintenance is done to deliver these changes in the customer environment.
	
All these phases are cascaded to each other in which progress is seen as flowing steadily downwards (like a waterfall) through the phases. The next phase is started only after the defined set of goals are achieved for previous phase and it is signed off, so the name "Waterfall Model". In this model, phases do not overlap.
	
## 3.2 Database description:

### ER Diagram

![[car dealership ER diagram (1) 1 1 1.jpg]]

### Schema Diagram
![[schema 1.jpg]]

# Documentation

## 4. Backend

### 4.1 Models (Tables)

#### Dealer Model
Contains the Dealer table definition and attribute list, based and derived from the schema diagram

```py
# src/models.py
class Dealer(models.Model) => (attrs)
```

The Dealer Table hereby referred to as the "Dealer Object" further into this section of the documentation consists of the following attributes

- <u>dealer_id</u>

	```py
	(variable) dealer_id: IntegerField => (
	primary_key: bool, 
	unique: bool
	)
	``` 
	```py
	dealer_id = models.IntegerField(
	primary_key=True, 
	unique=True
	)
	```

	Refers to the identification number of the dealer , `primary_key=True` parameter is setting the attribute to a primary key. The  `unique=True` parameter is useful in 
	referencing this particular attribute via ***Foreign Keys***.

- <u>dealer_img</u>
  
	Attribute definition:
	```py
	(variable) dealer_img: ImageField => (
	blank: bool
	)
	```
	source code:
	```py
	dealer_img = models.ImageField(
	blank=False
	)
	```

	Refers to the dealer's image field the `ImageField` method stores uploaded image in the room `/media/` folder. `blank = False`



- <u>dealer_name</u>
  
	Attribute definition:
	```py
	(variable) dealer_name: CharField =>(
	max_length: int, 
	blank: bool, null: bool
	)
	```
	
	source code:
	```py
	dealer_name = models.CharField(
	max_length=100, 
	blank=False, 
	null=False
	)
	```
	Refers to the dealer's name field the `NameField` method stores the name  of the dealer class,`null=False`parameter setting to the null attribute.max_length is set to (100) and it's restricts the number of characters used by the user by (100).
	`Blank=False` 


- <u>dealer_username</u>
  
  Attribute definition:
  ```py
  (variable) dealer_username: ForeignKey => (
  (class) User, 
  (parameter) on_delete: (...) -> None, 
  (parameter) related_name: str | None
  )
  ```

  Source code:
  ```py
  dealer_username = models.ForeignKey(
  User, on_delete=models.CASCADE, 
  related_name='d_username'
  )
  ```
  
  refers to the username of the dealer, as apparent here this attribute is a foreign key that refers to `(class) User`, it has a parameter `(parameter) on_delete: (...) -> None` set to `models.CASCADE` which means on deletion of a record from this table it reflects by comitting deletion on the referenced table as well. The `(parameter) related_name: str | None` parameter sets up an alternate name or view to avoid arising naming conflicts.

- <u>last_login</u>
  
	Attribute definition:
	```py
	(variable) last_login: DateTimeField => (
	(parameter) auto_now: bool
	)
	```	

	Source code:
	```py
	last_login = models.DateTimeField(auto_now=True)
	```
	The `last_login` attribute refers to the last time the dealer had logged in. the `(parameter) auto_now: bool` is set to `True` , the `auto_now` parameter automatically sets the login time based on server timezone.




	
	
- <u>contact</u>
  
	Attribute definition:
	```py
	(variable) contact: IntegerField => (
	null: bool, 
	blank: bool
	)
	```

	Source code:
	```py
	contact = models.IntegerField(
	null=False, 
	blank=False
	) 
	```
	refers to the contact details of the dealer class.the `(parameter)null: bool` is set to `False`,`Blank=False` 

	


- <u>company_name</u>
  
	Attribute definition:
	```py
	 (variable) company_name: CharField => (
	 (parameter) max_length: int | None, 
	 (parameter) null: bool, 
	 (parameter) blank: bool
	 )
	```
	Source code:
	```py
	company_name = models.CharField(
	max_length=100, 
	null=False, 
	blank=False
	)
	```
	

	The `company_name` attribute refers to the name of the company that the dealer belongs to, since it is a `CharField` it consists of the `(parameter) max_length` that is set to `100`. This field cannot be left `null` or `blank`.

- <u>address</u>
  
	Attribute definition:
	```py
	 (variable) address: TextField => (
	 (parameter) max_length: int | None, 
	 (parameter) null: bool, 
	 (parameter) blank: bool
	 )
	```
	Source code:
	```py
	address = models.TextField(
	max_length=300, 
	blank=False, 
	null=False
	)
	```

	The `Address` attribute refers to the Dealer's address, `(parameter) max_length: int | None` is set to `300`, and `(parameter) blank: bool` and `(parameter) null: bool` are set to `False`.
	
	


- <u>created</u>
  
	Attribute definition:
	```py
	(variable) created: DateTimeField => (
	(parameter) auto_created: bool
	)
	```

	Source code:
	```py
	created = models.DateTimeField(
	auto_created=True
	)
	```

	The `created` attribute refers to the date the dealer's profile was created, `(parameter) auto_created: bool` is set to `True`, this is a method passed in as a parameter which sets the value to current date and time based on the server region and timezone.






- <u>status</u>
	Attribute definition:
	```py
	(variable) status: CharField =>(
	(parameter) max_length: int | None,
	(parameter) choices: _FieldChoices | None, 
	(parameter) default: Any
	)
	```
	here the choices are defined in a list of choice sets,
	```py
	(constant) STATUS_CHOICE: list
	```
	Source code:
	```py
	STATUS_CHOICE = [
	('Active', 'Active'),
	('Inactive', 'Inactive')
	]
	```
	```py
	status = models.CharField(
	max_length=20, 
	choices=STATUS_CHOICE, 
	default= 'Active'
	)
	```
	refers to the status in the dealer class.Since it is a `CharField` it consists of the `(parameter) max_length` that is set to `20`.
	by `default= Any` the `STATUS_CHOICE` is set to `Active`.


	
	
#### Vehicle Model

Contains the Vehicle table definition and attribute list, based and derived from the schema diagram

- <u>vehicle_id</u>

	Attribute definition:
	```py
	(variable) vehicle_id: IntegerField => (
	(parameter) primary_key: bool, 
	(parameter) unique: bool
	)
	```

	Source code:
	```py
	vehicle_id = models.IntegerField(
	primary_key=True, 
	unique=True
	)
	```

	The `vehicle_id` attribute refers to the numeric id of the vehicle entries present in the table, it is a `primary_key` and it is set to be `unique`.


- <u>dealer_id</u>
	Attribute definition:
	```py
	(variable) dealer_id: ForeignKey =>(
	(class) Dealer, 
	(parameter) on_delete: (...) -> None, 
	(parameter) to_field: str | None
	)
	```
	Source code:
	```py
	dealer_id = models.ForeignKey(
	Dealer, 
	to_field='dealer_id', 
	on_delete=models.CASCADE
	)
	```
	 refers to the id of the dealer, as apparent here this attribute is a foreign key that refers to `(class) dealer`, it has a parameter `(parameter) on_delete: (...) -> None` set to `models.CASCADE` which means on deletion of a record from this table it reflects by comitting deletion on the referenced table as well. the `to_field` is set to `dealer_id`

	

- <u>vehicle_img</u>

	Attribute definition:
	```py
	(variable) vehicle_img: ImageField => (
	blank: Any
	)
	```
	
	Source code:
	```py
	vehicle_img = models.ImageField(
	blank=False
	)
	```

	The `vehicle_img` attribute contains the vehicle images uploaded to the server stored at `/media/` folder in the `MEDIA_DIR` directory of the server, `blank` is set to `False` so an image is required for every record uploaded.



- <u>name</u>

	Attribute definition:
	```py
	(variable) name: CharField => (
	(parameter) max_length: int | None, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	name = models.CharField(
	max_length=100, 
	blank=False
	)
	```
	
	The `name` attribute refers to the vehicle name, it's `max_length` is set to `100` and `blank` is `False` so it cannot be left empty.
	

	

- <u>type</u>
	Attribute definition:
	```py
	(variable) type: CharField =>(
	(parameter) max_length: int | None, 
	(parameter) choices: _FieldChoices | None, 
	(parameter) blank: bool
	)
	```

	here the choices are defined in a list of choice sets,

	```py
	(constant) VEHICLE_TYPE: list
	```
	
	```py
	VEHICLE_TYPE = [
    ("Hatchback", "Hatchback"),
    ("Sedan", "Sedan"),
    ("MPV", "MPV"),
    ("SUV", "SUV"),
    ("Crossover", "Crossover"),
    ("Coupe", "Coupe"),
    ("Convertible", "Convertible")
	]
	```
	Source code:
	```py
	type = models.CharField(
	max_length=100, 
	choices=VEHICLE_TYPE, 
	blank=False
	)
	```
	The `type` attribute refers to the the vehicle type,it's `max_length` is set `100` and `balck=False` so it cannot be left empty.The `choices`
	parameter is set to `VEHICLE_TYPE`


- <u>description</u>

	Attribute definition:
	```py
	(variable) description: TextField => (
	(parameter) max_length: int | None, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	description = models.TextField(
	max_length=100, 
	blank=False
	)
	```

	The `description` attribute refers to vehicle description, it's `max_length` is `200` and `blank` is set to `False`.

- <u>cost</u>

	Attribute definition:
	```py
	(variable) cost: IntegerField => (
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	cost = models.IntegerField(
	blank=False
	)
	```

	The `cost` attribute refers to the vehicle cost, it cannot be blank since `blank` is set to `False`.

- <u>status</u>

	Attribute definition:
	```py
	(variable) status: CharField => (
	(parameter) max_length: int | None, 
	(parameter) choices: _FieldChoices | None, 
	(parameter) blank: bool
	)
	```

	here the choices are defined in a list of choice sets,

	```py
	(constant) VEH_STATUS: list
	```

	```py
	VEH_STATUS = [
    ("For Sale", "For Sale"),
    ("Sold", "Sold")
	]
	```

	Source code:
	```py
	status = models.CharField(
	max_length=20, 
	choices=VEH_STATUS, 
	blank=False, 
	default='For Sale'
	)
	```
	The `status` attribute refers to the vehicle sale status, the choice sets are defined in `VEH_STATUS` , and `default` choice is `For Sale`.
	


- <u>created</u>
	Attribute definition:
	```py
	(variable) created: DateTimeField => (
	(parameter) auto_now_add: bool
	)
	```

	Source code:
	```py
	created = models.DateTimeField(
	auto_now_add=True
	)
	```
	The `created` attributes refers to the date on which the vehicle was created.The `auto_now_add:bool` is set to `True`.  



#### Customer Model

Contains the Customer table definition and attribute list, based and derived from the schema diagram

- <u>customer_id</u>

	Attribute definition:
	```py
	(variable) customer_id: IntegerField => (
	(parameter) primary_key: bool, 
	(parameter) unique: bool
	)
	```

	Source code:
	```py
	customer_id = models.IntegerField(
	primary_key=True, 
	unique=True
	)
	```

	The `customer_id` attribute refers to numeric customer id, it is a `primary_key`, and it is `unique`.


- <u>first_name</u>

	Attribute definition:
	```py
	(variable) first_name: CharField => (
	(parameter) max_length: int | None, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	first_name = models.CharField(
	max_length=100, 
	blank=False
	)
	```
	
	The `first_name` attribute stores the customer first name.The`max_length` is set to `100`.it cannot be left `blank`

- <u>last_name</u>

	Attribute definition:
	```py
	(variable) last_name: CharField =>(
	(parameter) max_length: int | None,
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	last_name = models.CharField(
	max_length=100, 
	blank=False
	)
	```

	The `last_name` attribute refers customer's last name, it cannot be left `blank`.

- <u>gender</u>

	Attribute definition:
	```py
	(variable) gender: CharField =>(
	(parameter) max_length: int | None,
	(parameter) blank: bool,
	(parameter) choices: _FieldChoices | None
	)
	```
	
	here the choices are defined in a list of choice sets,
	```py
	(constant) GENDER: list
	```
	```py
	GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
	]
	```
	Source code:
	```py
	gender = models.CharField(
	max_length=100, 
	blank=False, 
	choices=GENDER
	)
	```

	The `gender` attribute refers to the customer's gender, the gender field has `choices` defined in a list of sets defined in `GENDER`.
	
- <u>email</u>

	Attribute definition:
	```py
	(variable) email: CharField => (
	(parameter) max_length: int | None, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	email = models.CharField(
	max_length=100, 
	blank=False
	)
	```
	The `email` attribute refers to the customer's email.it's `max_length` is set to `100`and it cannot be left `blank`. 

- <u>contact</u>

	Attribute definition:
	```py
	(variable) contact: IntegerField =>(
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	contact = models.IntegerField(
	blank=False
	)
	```

	The `contact` attribute refers to the contact information of the customer, it cannot be left `blank`.

- <u>city</u>

	Attribute definition:
	```py
	(variable) city: CharField => (
	(parameter) max_length: int | None, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	city = models.CharField(
	max_length=100, 
	blank=False
	)
	```
	The `city` attribute refers to the customer's city name in which he/she resides.it's`max_length` is set to `100` and it cannot be left. `blank`.

- <u>state</u>

	Attribute definition:
	```py
	(variable) state: CharField =>(
	(variable) state: CharField,
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	state = models.CharField(
	max_length=100, 
	blank=False
	)
	```

	The `state` attribute refers to the customer's state, it cannot be `blank`.

- <u>address</u>

	Attribute definition:
	```py
	(variable) address: TextField => (
	(parameter) max_length: int | None
	)
	```

	Source code:
	```py
	address = models.TextField(
	max_length=100, 
	blank=False
	)
	```

	The `address` attribute refers to the customer's address, it cannot be left `blank`.


#### Sale Model

Contains the Sale table definition and attribute list, based and derived from the schema diagram

- <u>customer_id</u>

	Attribute definition:
	```py
	(variable) customer_id: ForeignKey => (
	(class) Customer, 
	(parameter) to_field: str | None, 
	(parameter) on_delete: (...) -> None
	)
	```

	Source code:
	```py
	customer_id = models.ForeignKey(
	Customer, 
	to_field='customer_id', 
	on_delete=models.CASCADE
	)
	```

	The `customer_id` attribute refers to the numeric id of the referenced customer.  


- <u>sale_id</u>

	Attribute definition:
	```py
	(variable) sale_id: IntegerField =>(
	(parameter) primary_key: bool,
	(parameter) unique: bool
	)
	```

	Source code:
	```py
	sale_id = models.IntegerField(
	primary_key=True, 
	unique=True
	)
	```

	The `sale_id` attribute refers to the numeric id of a sale made.

- <u>vehicle_id</u>

	Attribute definition:
	```py
	(variable) vehicle_id: ForeignKey =>(
	(class) Vehicle, 
	(parameter) to_field: str | None, 
	(parameter) on_delete: (...) -> None
	)
	```

	Source code:
	```py
	vehicle_id = models.ForeignKey(
	Vehicle, 
	to_field='vehicle_id', 
	on_delete=models.CASCADE
	)
	```

	The `vehicle_id` attribute refers to the numeric id of the referenced vehicle object.

- <u>description</u>

	Attribute definition:
	```py
	(variable) description: TextField =>(
	(parameter) max_length: int | None, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	 description = models.TextField(
	 max_length=100, 
	 blank=False
	 )
	```

	The `description` attribute describes the sale made.

- <u>order_date</u>

	Attribute definition:
	```py
	(variable) order_date: DateTimeField =>(
	(variable) order_date: DateTimeField
	) 
	```

	Source code:
	```py
	order_date = models.DateTimeField(
	auto_created=True
	)
	```

	The `order_date` attribute refers to the date the sale was made.

- <u>cost</u>

	Attribute definition:
	```py
	(variable) cost: IntegerField => (
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	cost = models.IntegerField(
	blank=False
	)
	```

	The `cost` refers to the cost paid by the customer to the dealership.

- <u>deal_date</u>

	Attribute definition:
	```py
	(variable) deal_date: DateTimeField => (
	(parameter) auto_created: bool
	)
	```

	Source code:
	```py
	deal_date = models.DateTimeField(
	auto_created=True
	)
	```

	The `deal_date` attribute refers to the date the car deal was made.

- <u>status</u>

	Attribute definition:
	```py
	(variable) status: CharField => (
	(parameter) max_length: int | None, 
	(parameter) blank: bool, 
	(parameter) choices: _FieldChoices | None
	)
	```

	here the choice list is given in a list of sets,

	```py
	(constant) TAX_STATUS: list
	```
	```py
	SALE_STATUS = [
    ("Sold", "Sold"),
    ("On hold", "On hold"),
    ("Rejected", "Rejected")
	]
	```

	Source code:
	```py
	status = models.CharField(
	max_length=20, 
	blank=False, 
	choices=SALE_STATUS
	)
	```

	The `status` attribute refers to the deal status.

- <u>tax_id</u>

	Attribute definition:
	```py
	(variable) tax_id: IntegerField =>(
	(parameter) unique: bool, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	tax_id = models.IntegerField(
	unique=True, 
	blank=False
	)
	```
	The `tax` attributes refers to the id of the tax paid for the vehicle.the `unique` is set to `True` and it cannot be left blank. 


#### Tax Model

Contains the Tax table definition and attribute list, based and derived from the schema diagram

- <u>tax_id</u>

	Attribute definition:
	```py
	(variable) tax_id: ForeignKey => (
	(class) Sale, 
	(parameter) to_field: str | None, 
	(parameter) on_delete: (...) -> None
	)
	```

	Source code:
	```py
	tax_id = models.ForeignKey(
	Sale, 
	to_field='tax_id', 
	on_delete=models.CASCADE
	)
	```

	The `tax_id` attribute refers to the numeric id referenced in the Sale Model/Table.


- <u>tax</u>

	Attribute definition:
	```py
	(variable) tax: IntegerField =>(
	(variable) tax: IntegerField
	)
	```

	Source code:
	```py
	tax = models.IntegerField(
	blank=False
	)
	```
	The `tax` attribute refers to the amount of tax applied to the bill of sale.
	
- <u>description</u>

	Attribute definition:
	```py
	(variable) description: TextField=>(
	(parameter) max_length: int | None, 
	(parameter) blank: bool
	)
	```

	Source code:
	```py
	description = models.TextField(
	max_length=100, blank=False
	)
	```
	The `description` attribute refers to the description of the tax paid.
	
- <u>status</u>

	Attribute definition:
	```py
	(variable) status: CharField => (
	(parameter) max_length: int | None, 
	(parameter) blank: bool, 
	(parameter) choices: _FieldChoices | None
	)
	```

	here the choice list is given as,
	```py
	(constant) TAX_STATUS: list
	```
	```py
	TAX_STATUS = [ 
    ("Approved", "Approved"),
    ("Pending", "Pending"),
    ("Rejected", "Rejected")
	```
	
	Source code:
	```py
	status = models.CharField(
	max_length=20, 
	blank=False, 
	choices=TAX_STATUS
	)
	```
	The `status` attribute refers to the status of the tax payment, it refers to `TAX_STATUS` list for choice sets.


# Snapshots

## 5.1 Frontend w/backend admin panel
![[Screenshot (19).png]]
![[Screenshot (20).png]]
![[Screenshot (21).png]]
![[Screenshot (22).png]]
![[Screenshot (23).png]]
![[Screenshot (24).png]]
![[Screenshot (25).png]]
![[Screenshot (26).png]]

## Source code
![[Screenshot (27).png]]
![[Screenshot (28).png]]
![[Screenshot (29).png]]
![[Screenshot (30).png]]
![[Screenshot (31).png]]
![[Screenshot (32).png]]
![[Screenshot (33).png]]
![[Screenshot (34).png]]
![[Screenshot (35).png]]
![[Screenshot (36) 1.png]]
![[Screenshot (37).png]]
![[Screenshot (38).png]]
![[Screenshot (39).png]]
![[Screenshot (40).png]]
![[Screenshot (41).png]]
![[Screenshot (42).png]]
![[Screenshot (43).png]]
![[Screenshot (44).png]]
![[Screenshot (45).png]]
![[Screenshot (46).png]]
![[Screenshot (47).png]]
![[Screenshot (48).png]]
![[Screenshot (49).png]]
![[Screenshot (50).png]]
![[Screenshot (51).png]]
![[Screenshot (52).png]]
![[Screenshot (53).png]]
![[Screenshot (54).png]]
![[Screenshot (55).png]]































































	