User Manual: Installation & Setup Instructions
1. Download and Extract Files
	-Save the provided .zip file to your preferred folder on your laptop.
	-Right-click the .zip file and select “Extract All” to extract it.
	-The extracted folder includes:
		=Python application source code
		=recycling_system.sql (MySQL database file)


2. Install XAMPP (if not already installed)
	-Go to https://www.apachefriends.org/index.html and download XAMPP for your operating system.
	-Install XAMPP using the default setup.
	-After installation, open the XAMPP Control Panel.
	-Click Start for both:
		=Apache
		=MySQL


3. Import the MySQL Database
	-Open your browser and go to: http://localhost/phpmyadmin/
	-Click Databases at the top.
	-Create a new database (e.g., name it recycling_system).
	-Click the new database name from the left sidebar.
	-Select Import from the top menu.
	-Click Choose File and upload the recycling_system.sql file from the extracted folder.
	-Click Go to import


4. Configure the Database Connection (if needed)
	-Open the extracted code folder.
	-Find and open database.py in a code editor (e.g., VS Code).
	-Ensure the database configuration matches:
		self.db_connection = mysql.connector.connect(
   		         host="localhost",
  		         user="root",
  		         password="",  
   		         database="recycling_system"
    		)
MAKE SURE YOUR DATABASE NAME IN PHPMYADMIN  IS SAME WITH THE CODE IN database.py
If your phpMyAdmin has a different username/password, update them here.


5. Run the Application
	-Open the code folder in VS Code or any Python IDE.
	-Run the main application file,LoginSignUp.py
	-Ensure you have the required Python packages installed:
		-mysql-connector-python
		-tkinter (comes with standard Python installation)
	-If needed, install packages using (typing in the terminal):
		-pip install mysql-connector-python
		-pip install requests
		-pip install Pillow
		-pip install bcrypt


6. Using the System
	-The application will open in a window.
	-You can now:
		-Sign Up / Log In as a User or Admin
			-Example User Account : 
				-Email : bernard@gmail.com password : Bernard1234@ 
				-Email : zhenho@gmail.com password : Zhenho1234@ 
			-Example Admin Account : 
				-Email : admin@admin.com password : Admin1234@
			-Example User Account : 
				-Email : rcadmin@rcadmin.com password : Rcadmin1234@ 
