# Flask REST API - User Management

A simple Flask-based REST API to manage user data in memory, supporting **CRUD operations**:
- **GET**: Retrieve all users
- **POST**: Add a new user
- **PUT**: Update existing user
- **DELETE**: Remove a user

## 🚀 Features
- Simple in-memory user storage (Python dictionary)
- JSON-based request/response
- Works with Postman or cURL
- Beginner-friendly Flask code

---

## 📂 Project Structure

flask-api/
│
├── app.py # Main Flask application
└── requirements.txt # Dependencies

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/flask-rest-api.git
cd flask-rest-api
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Application
```bash
python app.py
The API will start at:
http://127.0.0.1:5000
```
---

## 📬 API Endpoints
#### 1. Add User
```bash
POST /users

{
    "id": "1",
    "name": "John Doe",
    "email": "john@example.com"
}
Response:

{ "message": "User added" }
```
#### 2. Get All Users
```bash
GET /users
Response:

{
    "1": {
        "id": "1",
        "name": "John Doe",
        "email": "john@example.com"
    }
}
```
#### 3. Update User
```bash
PUT /users/1

{
    "name": "John Smith",
    "email": "john.smith@example.com"
}
Response:

{ "message": "User updated" }
```
#### 4. Delete User
```bash
DELETE /users/1
Response:

{ "message": "User deleted" }
```
---

## 🧪 Testing
You can test using:
Postman
Copy URL in terminal

Example:
```bash
curl -X POST http://127.0.0.1:5000/users \
-H "Content-Type: application/json" \
-d '{"id":"1","name":"John Cena","email":"john@example.com"}'
```
