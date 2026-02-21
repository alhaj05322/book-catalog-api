# **Book Catalog API**

This is a repository containing a sample readme file.

---

## **Description**
This is a Flask API. It has the following properties:
    1. User
    2. Book
   A user can create an accout, login logout. After login users can add a book to database,
   edite existing book, get a list of all books, and delete books form database.

## **Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Installation and Set Up
Clone the repo from GitHub:
```
git clone https://github.com/alhaj05322/book-catalog-api.git
```

Navigate to the root folder:
```
cd book-catalog-api
```

Install the required packages:
```
pip install -r requirements.txt
```

Create the database
```
python create_db.py
```



## Launching the Program
Run ```flask run```. You may use [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) for Google Chrome to run the API.

## API Endpoints

| Resource URL | Methods | Description | Requires Login |
| -------- | ------------- | --------- |--------------- |
| `/api` | GET  | The index | FALSE |
| `/api/auth/register` | POST  | User registration | FALSE |
|  `/api/auth/login` | POST | User login | FALSE |
|  `/api/auth/logout` | POST | User logout | TRUE |
| `/api/books` | GET, POST | View all books, add a book | TRUE |
| `/api/books/<int:book_id>` | PUT, DELETE | edit, and delete a single book | TRUE |



## Sample API Requests

Registering and logging in to get a JWT token:
![User Registration](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/api_register.png)

![User Login](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/api_login.png)

Displaying a paginated list of teachers:
![List of Teachers](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/api_list_teachers.png)

Displaying a paginated list of subjects:
![List of Subjects](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/api_list_subjects.png)

Updating a student:
![Updating Student](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/api_update_student.png)

## Web App

The app has a web-based interface and can be accessed [here](https://flask-school-app.herokuapp.com/). A sample user has already been created with the following credentials:

```
username: testuser
password: testpassword
```

Login:
![User Login](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/app_login.png)

Dashboard:
![App Dashboard](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/app_dashboard.png)

Displaying all students:
![Students](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/app_students.png)

Displaying all teachers:
![Teachers](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/app_teachers.png)

Displaying all subjects:
![Subjects](https://github.com/mbithenzomo/flask-student-api/blob/master/screenshots/app_subjects.png)


## Testing
To test, run the following command: ```nose2```

## Built With...
* [Flask](http://flask.pocoo.org/)
## **Contact Information**

Provide your contact information or links to your social profiles for users to reach out with questions or feedback.

Example:
- Email: your.email@example.com
- Twitter: [@yourhandle](https://twitter.com/yourhandle)
- GitHub: [yourusername](https://github.com/yourusername)

---

This structure is flexible and can be adapted to suit the specific needs of your project. The goal is to make the README informative, easy to navigate, and helpful for anyone interacting with your project.
