import os

project_name = 'ecommerce_management_system'
apps = ['products', 'users', 'orders', 'cart', 'payments', 'blog']
static_dirs = ['css', 'js', 'images']
media_dirs = ['products', 'users']
templates_dirs = ['base.html', 'navbar.html']
app_templates = ['product_list.html', 'product_detail.html', 'order_summary.html', 'checkout.html']

# Function to create directories and files
def create_project_structure():
    # Create the project directory
    os.makedirs(project_name, exist_ok=True)

    # Create sub-directories
    for app in apps:
        app_path = os.path.join(project_name, app)
        os.makedirs(app_path, exist_ok=True)
        os.makedirs(os.path.join(app_path, 'templates'), exist_ok=True)
        os.makedirs(os.path.join(app_path, 'migrations'), exist_ok=True)
        os.makedirs(os.path.join(app_path, 'static'), exist_ok=True)
        
        # Create app files
        with open(os.path.join(app_path, 'models.py'), 'w') as f:
            f.write(f"# {app} models\n")
        with open(os.path.join(app_path, 'views.py'), 'w') as f:
            f.write(f"# {app} views\n")
        with open(os.path.join(app_path, 'urls.py'), 'w') as f:
            f.write(f"# {app} urls\n")

        # Create templates and static files
        for template in app_templates:
            with open(os.path.join(app_path, 'templates', template), 'w') as f:
                f.write(f"<h1>{template} for {app}</h1>\n")
        
        os.makedirs(os.path.join(app_path, 'static', 'css'), exist_ok=True)
        os.makedirs(os.path.join(app_path, 'static', 'js'), exist_ok=True)
        os.makedirs(os.path.join(app_path, 'static', 'images'), exist_ok=True)
    
    # Create the static, media, and templates folders for the entire project
    os.makedirs(os.path.join(project_name, 'static'), exist_ok=True)
    os.makedirs(os.path.join(project_name, 'media'), exist_ok=True)
    os.makedirs(os.path.join(project_name, 'templates'), exist_ok=True)

    # Add base.html and navbar.html in templates
    for template in templates_dirs:
        with open(os.path.join(project_name, 'templates', template), 'w') as f:
            f.write(f"<h1>{template}</h1>\n")

    # Create the requirements.txt file
    with open(os.path.join(project_name, 'requirements.txt'), 'w') as f:
        f.write("Django\n")

# Run the function to create project structure
create_project_structure()
