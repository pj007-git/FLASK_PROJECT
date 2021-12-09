Setup Instruction:

Framework: I used Python/ Flask FrameWork for This Project 
Database : For database i use "ORM" based SQLAlchemy for Sqlite Database (link = sqlite:///<fileName>.db)
for Creating Database I use Terminals (ex. db.create_all())


i have created flask application named "app" and as well as my filename
secret-key use for authenticate the user and protecting cookies in session which is store in server
I use authentication with session and also use  lifetime of the session 

for Creating User Model (Table of the our project Database) 
we can show our users detail after run the query(User.query.all())

for the run the application : python <filename> (app.py)



Code Architecture:


I created app file in my project and i created my project in virtual env
In the templates folder i created all the html files index.html, login.html, home.html

main file is "app.py" which run the whole application
In app.py filees i need to import all the requirements like "flask" for framework,for Database "SQLAlchemy" and "datetime"
also the User Model of the Databse and all the API routes is in this files.





Usage Instruction of API:


Registraion : (/OA/Registration/) when this API is called  the Registration page will shown 
on the Desktop this api holdes the "POST" request which handels by the def Registration() function
if User is already registered then its show the error else user is created

Login: (/OA/Login/) when this api is called or user redirect to this api browser show login.html page 
this api holdes the POST request so, if User's Name or Password is invalid or can't match with the Database
then its show the error messege else User is authenticate and Session is avalible for the 5 minutes and 
redirect to the Home Page.

Home : (/OA/Home/) this api call the home.html page and show the user_name and  "UserDetails" button and 
Logout Button after user click the show user buttopn "GET" Method calls and User table will be shown
on the page with pagination in pagiination page is called by the request.args.get() method 
this method holdes the argument of default pagenumber

Pagination : users = User.query.Pagination() so users information now the object of the Pagination and 
we can perform users.items for the values and users.iter_pages() for showing data per_page

Logout : (/OA/Logout/) when user clicks the Logout button first user's session will be popped from the dictionary
now user cant login directly user has to relogin for show the user data
after Logout user is redirect to the Login page
