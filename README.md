# Inventory Management System API  

Welcome to the **Inventory Management System API**, a robust backend for managing products, stock levels, supplier relationships, reorders, and reporting. Built using **Django Rest Framework**, this API provides all the endpoints necessary for efficient inventory control.  

---

## Features  

- **Product Management**: Add, view, update, and delete products in your inventory.  
- **Stock Movement**: Track additions and removals of stock with detailed movement history.  
- **Supplier Management**: Manage supplier details and their relationships to products.  
- **Low Stock Alerts**: Automatically identify and flag low stock items for action.  
- **Reorder System**: Automate reordering when stock falls below thresholds.  
- **Reports and Analytics**: Gain insights into inventory trends, stock movements, and product performance.  

---

## API Endpoints  

Here is the list of available endpoints:  

| **Endpoint**                  | **Description**                              | **Method** |
|-------------------------------|----------------------------------------------|------------|
| `/api/v1/products/`           | List all products or add a new product.     | GET, POST  |
| `/api/v1/products/<int:pk>/`  | Retrieve, update, or delete a product.      | GET, PUT, DELETE |
| `/api/v1/stock-history/`      | View stock movement history.                | GET        |
| `/api/v1/suppliers/`          | List all suppliers or add a new supplier.   | GET, POST  |
| `/api/v1/suppliers/<int:pk>/` | Retrieve, update, or delete a supplier.     | GET, PUT, DELETE |
| `/api/v1/reorder/`            | View reorder requests or add new ones.      | GET, POST  |
| `/api/v1/product-sales/`      | View analytics for product sales.           | GET        |

---

## Installation  

Follow these steps to set up the project locally:  

### Prerequisites  

Ensure you have the following installed:  
- Python 3.8+
- Django 4.x
- Django Rest Framework  
- PostgreSQL or SQLite (for database)  

### Setup  

1. Clone this repository:  
   ```bash  
   git clone https://github.com/Jendoic/InventorySystem.git 
   cd InventorySystem 
   ```  

2. Create a virtual environment and install dependencies:  
   ```bash  
   python -m venv env  
   source env/bin/activate  
   pip install -r requirements.txt  
   ```  

3. Configure your `.env` file for the database and secret key settings.  

4. Apply migrations:  
   ```bash  
   python manage.py migrate  
   ```  

5. Create a superuser for accessing the admin panel:  
   ```bash  
   python manage.py createsuperuser  
   ```  

6. Start the development server:  
   ```bash  
   python manage.py runserver  
   ```  

---

## Usage  

### Authentication  

This API requires authentication for most endpoints. You can use token-based authentication. To obtain a token, log in and use the `/api-token-auth/` endpoint.  

### Low Stock Alerts  

The system automatically detects low stock and triggers reorder requests for flagged products.  

### Reporting and Analytics  

Use the `/api/v1/product-sales/` endpoint to view trends and analytics.  

---

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.  

---

## Contributing  

We welcome contributions! Feel free to submit issues or pull requests to improve the system.  

---

Enjoy using the **Inventory Management System API**!  

