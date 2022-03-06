# Install this project

```bash
# if you have ssh key
git clone git@github.com:shaggy-axel/alex.git && cd alex/
# else
git clone https://github.com/shaggy-axel/alex.git && cd alex/

# install virtualenvironment
python3.9 -m venv .venv
. .venv/bin/activate

# migrate and run server
python src/manage.py migrate
python src/manage.py runserver
```

# Create project yourself
```bash
python3.9 -m venv .venv
. .venv/bin/activate
django-admin startproject project_name
mv project_name/ src/
```

# Create application and connect to project
1. create folder `apps/` in `src/` folder
2. create `your_app_name/` folder in `apps/` folder
3. create needed files `.py` and connect this app in `settings.py`:
```python
INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    ...
    'django.contrib.staticfiles',

    # your apps
    'apps.your_app_name',
]
```

# Migration's commands
```bash
python src/manage.py makemigrations  # Create migration files
python src/manage.py migrate         # Run migration files
```

# MODELS

```python
Role:
 - title
 - description

Employee:
 - first_name
 - last_name
 - sex
 - telephone
 - role [Role] ForeignKey

Order
 - employee [Employee] ForeignKey
 - products [Product]  ManyToMany
 - date

Product:
 - title
 - description
 - photo
 - quantity
 - price
 - currency
```

# How to use database shell, and python shell connected to your project
```bash
python src/manage.py shell  # run python-shell
python src/manage.py dbshell  # run db-shell using connected database engine (sqlite3)
```

```python
# python-shell
# from apps.app_name.models import YourModel
from apps.products.models import Product

# simple request to db using model
products = Product.objects.all()  # queryset of all products.
product = Product.objects.get(title="Put title here")  # you get object of product with title "Put title here"
product = Product.objects.create(
    title="Iphone", description="...",
    price=1000, currency="USD",
    quantity=2000,
)  # create an object with values in args
product, created = Product.objects.get_or_create(
    title="Iphone", description="...",
    price=1000, currency="USD",
    quantity=2000,
)  # return an object product, if already exist -> created=False, else -> created=True

# all products where title starts with "Ip"
products = Product.objects.filter(title__startswith="Ip")

# all products where price > 100 and currency = "USD"
products = Product.objects.filter(price__gt=100, currency="USD")
```

```sql
/* db-shell sqlite3 */
/* to exit */
.exit
/* get help message */
.help
/* use sql syntax and send request to db */
```