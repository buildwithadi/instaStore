# InstaStore — B2B SaaS for Instagram Clothing Sellers 👗📦

InstaStore is a lightweight, easy-to-use web application that enables Instagram clothing store owners to create a simple product website where customers can browse products and place orders via WhatsApp. Perfect for small businesses and home-run stores that want to streamline their order management without the complexity of a full e-commerce platform.

---

## 🚀 Features

- 🧑‍🤝‍🧑 Multi Vendor Support (There will be multiple vendor for each Store)
- 🔐 Seller Dashboard to add & manage products
- 🛍️ Customer-facing product catalog page
- 🧾 Order system that redirects to WhatsApp with pre-filled order details
- 💬 No need for complex payment gateways or logins
- 📱 Mobile-friendly and minimalistic interface

---

## 🛠️ Tech Stack

- **Frontend**: HTML,Bootstrap CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite (default), easily switchable to PostgreSQL
- **Order Integration**: WhatsApp `wa.me` links with auto-filled order details
- **Hosting**: Render
- **Version Control**: Git + GitHub

---

### How to Run the project?

- `pip install -r requirements.txt`
- `python manage.py runserver`

## Web Structure

- <website_name>/ : This is the main store page
- <website_name>/storeadmin : This will lead to the Admin Page of the Store
