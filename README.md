# Product Catalog API

A RESTful API built using FastAPI and PostgreSQL to manage product data.  
This project implements CRUD operations

---

## Tech Stack

- Python 3
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic
- python-dotenv
- Uvicorn

---

##Features

- Create Product
- Get All Products
- Get Product by ID
- Update Product
- Delete Product

---

## 📂 Project Structure

product_catalog/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

---

##  Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/konduriPooja/Product-catalog-api.git
cd product_catalog

---

### 2️⃣ Create Virtual Environment

python -m venv .venv

Activate:

Windows:
.venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

DATABASE_URL=postgresql://username:password@localhost:5432/database_name

---

### 5️⃣ Run Application

uvicorn app.main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

---

## 🔐 Environment Variables

This project uses environment variables to securely manage database credentials.  
Sensitive information is not stored in the repository.

---

## 📖 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | /products/ | Create product |
| GET    | /products/ | Get all products |
| GET    | /products/{id} | Get product by ID |
| PUT    | /products/{id} | Update product |
| DELETE | /products/{id} | Delete product |

---

## ✅ Status

Project completed with CRUD functionality and PostgreSQL integration.
