# MIB E-Commerce Backend

**MIB E-Commerce Backend** is a production-grade backend system built with Django for managing e-commerce operations. It features a robust architecture with support for JWT authentication, Redis caching, Celery for background tasks, and load testing using Locust.

---

## Features

- **Django REST Framework**: Efficient API development.
- **JWT Authentication**: Secure user authentication with Djoser.
- **Redis and Celery**: Background tasks and caching support.
- **Docker**: Containerized deployment for scalability.
- **MySQL**: Reliable relational database support.
- **Locust for Load Testing**: Evaluate system performance.
- **Pytest**: Comprehensive unit testing.
- **Debug Toolbar**: Debugging tools for local development.

---

## Project Structure

```plaintext
project_storefront/
├── core/                    # Core app with shared logic and utilities
├── likes/                   # Handles likes and user interactions
├── locustfiles/             # Load testing scripts
├── playground/              # Experimental features and development tests
├── store/                   # Main e-commerce app with product management
├── storefront/              # Root project settings and configuration
├── tags/                    # Tagging system for products
├── web/                     # Frontend integration (optional)
├── .gitignore               # Git ignore file
├── Pipfile                  # Python dependencies (used by pipenv)
├── Pipfile.lock             # Dependency lock file
├── README.md                # Project documentation
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker image setup
├── manage.py                # Django management script
├── pytest.ini               # Pytest configuration
├── seed.sql                 # Database seed data
└── wait-for-it.sh           # Docker script for waiting on services
```

2. **Set up the environment**:

   - Create and install dependencies in virtual environment:

     ```bash
     pipenv install
     ```

   - Activate the virtual environment:

     - On Windows:

       ```bash
       pipenv shell
       ```

     - On macOS/Linux:

       ```bash
       source venv/bin/activate
       ```

3. **Set up the database**:

   - Apply migrations:

     ```bash
     python manage.py migrate
     ```

   - (Optional) Load initial data:

     ```bash
     python manage.py seed_db
     ```

4. **Configure environment variables**:

   - Create a `.env` file in the project root and add the necessary environment variables. Refer to `.env.example` for required variables.

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

The API provides the following endpoints:

### Authentication

- **Register a new user**  
  `POST /auth/users/`

- **Obtain a JSON Web Token**  
  `POST /auth/jwt/create/`

- **Refresh an existing token**  
  `POST /auth/jwt/refresh/`

### Products

- **List all products**  
  `GET /store/products/`

- **Create a new product**  
  `POST /store/products/`

- **Retrieve a specific product**  
  `GET /store/products/{id}/`

- **Update a specific product**  
  `PUT /store/products/{id}/`

- **Delete a specific product**  
  `DELETE /store/products/{id}/`

### Orders

- **List all orders**  
  `GET /store/orders/`

- **Create a new order**  
  `POST /store/orders/`

- **Retrieve a specific order**  
  `GET /store/orders/{id}/`

- **Update a specific order**  
  `PUT /store/orders/{id}/`

- **Delete a specific order**  
  `DELETE /store/orders/{id}/`
