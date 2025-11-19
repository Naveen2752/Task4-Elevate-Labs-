# 🧩 User Management REST API Using Flask

# Task4-Elevate-Labs-
Task 3 Web Scraper for News Headlines Application


A simple and clean REST API built using **Flask** that performs full CRUD (Create, Read, Update, Delete) operations on user data.  
This project is perfect for learning the fundamentals of API development and is suitable for internship submissions or GitHub portfolios.

---

## 🚀 Features

- Create new users (`POST`)
- Fetch all users (`GET`)
- Fetch a single user by ID (`GET`)
- Update existing users (`PUT`)
- Delete a user (`DELETE`)
- In-memory data storage (no database required)
- Fully JSON-based API responses
- Easy testing with Postman or Curl

---

## 📁 Project Structure

```

📁 flask_user_api
│── app.py
│── requirements.txt
│── README.md

```

---

## 🛠️ Technologies Used

- **Python 3**
- **Flask** (for API development)
- **Postman / Curl** (for endpoint testing)

Install dependencies:
```bash
pip install flask
````

---

## 📌 API Endpoints Overview

| Method | Endpoint      | Description       |
| ------ | ------------- | ----------------- |
| GET    | `/users`      | Get all users     |
| GET    | `/users/<id>` | Get user by ID    |
| POST   | `/users`      | Create a new user |
| PUT    | `/users/<id>` | Update user by ID |
| DELETE | `/users/<id>` | Delete user by ID |

---

## 🧠 How It Works

* The API stores all users in an **in-memory Python dictionary** named `users`.
* Each user record contains:

  ```json
  {
    "id": 1,
    "name": "Naveen",
    "email": "naveen@example.com"
  }
  ```
* New users receive auto-incrementing IDs.
* The API responds with clean JSON and proper HTTP status codes.

---

## 🚀 Running the Project

### 1. Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install Flask:

```bash
pip install flask
```

### 3. Run the server:

```bash
python app.py
```

You will see:

```
 * Running on http://127.0.0.1:5000/
 * Press CTRL+C to quit
```

---

# 🧪 Testing the API (Postman or Curl)

### ✔ GET all users

```
GET http://127.0.0.1:5000/users
```

### ✔ POST create user

```
POST http://127.0.0.1:5000/users
```

Body → JSON:

```json
{
  "name": "Naveen",
  "email": "naveen@example.com"
}
```

### ✔ GET a single user

```
GET http://127.0.0.1:5000/users/1
```

### ✔ PUT update user

```
PUT http://127.0.0.1:5000/users/1
```

Body → JSON:

```json
{
  "email": "updated@mail.com"
}
```

### ✔ DELETE user

```
DELETE http://127.0.0.1:5000/users/1
```

---

## 🧩 Example JSON Responses

### ➤ Successful POST

```json
{
  "email": "naveen@example.com",
  "id": 1,
  "name": "Naveen"
}
```

### ➤ User Not Found

```json
{
  "error": "User not found"
}
```

---

## 📸 (Optional) Add Screenshots

You can include screenshots in your repo:

```
![Postman Screenshot](images/postman.png)
![Terminal Screenshot](images/terminal.png)
```

---

## 🎯 Learning Outcomes

By completing this project, you will understand:

* How REST APIs work
* How to build backend logic using Flask
* How to structure JSON responses
* How HTTP methods (GET, POST, PUT, DELETE) operate
* How to test APIs using Postman

This is a strong introductory backend project to showcase in your internship portfolio.

---

## 🤝 Contributing

Feel free to fork this project, make improvements, and submit pull requests.

---
