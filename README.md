# Gallery

  Gallery is a website dedicated to sharing photography.


## Author

**CHRISTINE MULINDI**

## Features


As a user of the application you will be able to:

1. View different photos that interest you.
2. Click on a single photo to expand it and also view the details of the photo. The photo details will appear      on a modal within the same route as the main page.
3. Search for different categories of photos. (ie. Travel, Food)
4. View photos based on the location they were taken or category.


### Installing

* Clone this repo: git clone https://github.com/ChristineMulindi/Gallery.git
* The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
* Open your terminal and navigate to gallery then create a virtual environment.For detailed guide refer  [here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
* To run the app, you'll have to run the following commands in your terminal
       pip install -r requirements.txt
* On your terminal,Create database gallery using the command below.
       CREATE DATABASE gallery;
* Migrate the database using the command below
       python3.6 manage.py migrate
* Then serve the app, so that the app will be available on localhost:8000, to do this run the command below
       python manage.py runserver
* Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Running the tests

Use the command given below to run automated tests.
        python manage.py test gallery



## Built With

* Django
* HTML - For building Mark Up pages/User Interface
* CSS - For Styling User Interface


## License

This project is licensed under the MIT License.Copyright 2019( ChristineMulindi)
