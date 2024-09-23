# Django E-commerce Application

A comprehensive and user-friendly e-commerce with a blog application built with Django where users can browse, add products to their cart, and complete their purchases and read through blog posts. Administrators can manage products, blog posts, categories, and user orders through the admin panel.

## Prerequisites
Before you begin, make sure you have the following installed:

- Python 3.11
- Django 5.1 or higher
- Virtualenv (optional but recommended)


## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mohammd-1819/blog.git


2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install the required dependencies:**
   ```bash
    pip install -r requirements.txt


4. **Apply the migrations:**
   ```bash
    python manage.py migrate


5. **Create a superuser for the admin panel (optional but recommended):**
   ```bash
    python manage.py createsuperuser
    default is: admin@gmail.com
    password : admin


6. **Run the development server:**
    ```bash
    python manage.py runserver


7. **Access the application:**
    Open your browser and go to http://127.0.0.1:8000/ for the main page


## Features
    User registration and login with password via emial verification
    Browse products by category and search functionality
    Add products to the shopping cart and manage the cart
    Admin panel for managing products,orders, users and blog posts 
    Product pagination and filtering options
    Comment system for each blog post and product (Only Authenticated User)
    Pagination for listing blog posts

## Usage
    Once the server is running, users can browse through the products, blog posts,add items to their cart and proceed to checkout. Administrators can add, edit, and delete products, as well as manage orders from the admin panel.

## Managing Products
    Only admin users can create a new product. Products can be categorized and have various attributes like price, description and stock status.

## Technologies Used
    Backend: Django
    Database: PostgreSQL
    Authentication: Customized Django built-in authentication system
    Frontend: HTML, CSS, JavaScript (with Bootstrap)

## Author
    https://github.com/mohammd-1819