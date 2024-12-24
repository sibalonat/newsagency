 News Agency Project

In this presentation, we will go over the main features of this site for the course Web Programming with Python and JavaScript. This project serves as the final requirement for certification and demonstrates my capability to develop something independently. The project is a news agency, divided into two applications within the main news agency: one for creating and reading news, and the other for managing users to determine who among them is an editor.

## Distinctiveness and Complexity

### Distinctiveness
This project is distinct because it integrates multiple functionalities into a single cohesive application, unlike other projects in this course which are typically simpler CRUD applications.
It includes user role management, access control, and dynamic content generation, providing a fully custom user experience without relying on Django's admin interface.
Features such as article creation, editing, deletion, and commenting add to its uniqueness, as these are not present in other projects.

### Complexity
The project involves multi-role access control, middleware for route protection, and dynamic content management. The application includes:
- It includes three distinct user roles (Reader, Editor, Superadmin) with specific permissions, adding to the complexity.
- Middleware is used to enforce access control based on user roles, ensuring secure and appropriate access to different parts of the application.
- Dynamic content generation and filtering, along with a custom seeder command to populate the database with initial data, add layers of complexity.
- Pagination is implemented to handle large datasets efficiently.
- Custom template tags and forms are used for both the news and user management applications.
- The integration of Bootstrap 5 for responsive design and custom CSS for additional styling enhances the user interface.
- JavaScript is used for dynamic content and user interactions, making the application more interactive and user-friendly.


## File Descriptions

### `news/models.py`
Contains the models for the application, including `Article` and `Comment`.

### `news/views.py`
Contains the views for handling requests and rendering templates.

### `news/management/commands/seed_data.py`
Custom management command to seed the database with initial users and articles.

### `news/urls.py`
Defines the URL patterns for the news application.

### `news/forms.py`
Contains the forms for the news application.

### `news/templates/news/*.html`
Contains the HTML templates for the news application.

### `news/static/news/styles.css`
Custom CSS for styling the news application.

### `user_management/models.py`
Contains the user model with custom fields for roles.

### `user_management/views.py`
Contains the views for user management, including registration and role toggling.

### `user_management/urls.py`
Defines the URL patterns for the user management application.

### `user_management/forms.py`
Contains the forms for the user management application.

### `user_management/templatetags/form_tags.py`
Contains custom template tags for the user management application.

### `user_management/templates/user_management/*.html`
Contains the HTML templates for the user management application.

### `user_management/static/user_management/styles.css`
Custom CSS for styling the news application.

### `user_management/static/user_management/index.js`
JavaScript for handling dynamic content and user interactions.


## How to Run Your Application

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```
2. **Run Migrations**:
```bash
python manage.py migrate
```
3. **Seed the Database**:
```bash
python manage.py seed_data
```
3. **Start the Development Server**:
```bash
python manage.py runserver
```
3. **Access the Application**:
   Open your web browser and navigate to ```bash http://127.0.0.1:8000/ ``` 

### Additional Information

## Roles

There are three roles within the application, none of which utilize the admin dashboard provided by Django:
- **Reader**: Can read news, comment, and filter news, but cannot create, edit, or delete it.
- **Editor**: Can create news, edit their own posts, and delete their own posts.
- **Superadmin**: Has the authority to manage users, allowing me to assign or revoke the editor role by reverting a user back to reader status.

## Access Control

Access to different routes is regulated by middleware, which restricts access based on roles, ensuring that users without permission for specific routes are redirected to the login page.

## Styling

The `user_management` and `news` applications employ Bootstrap 5 for styling, along with some custom CSS. Each application has its own templates but shares a common design pattern.

## Seeder Command

An important aspect of setting everything up is the seeder command. This command facilitates the creation of some editors, readers, and a superadmin (staff). Before executing the seed_data command, we must first install a lorem package to generate default content by running:

```bash
pip install -r requirements.txt
```
or 
```bash
pip install lorem
```

To execute the seed command, you need to run:

```bash
python manage.py seed_data 
```

## Usage

Once that is completed, accessing the default route will take you to the index page for the news. You must first log in as an editor by navigating to the login page. After logging in, a create article option will appear in the navigation at the top. The article requires three properties to be filled in: title, content, and image_url. Some fields are optional, while others are mandatory. After creating an article, you will be redirected back to the index page where you can view the article you just created. You also have the option to delete or view the article.

If you open the article, you can edit it and make changes, as well as filter articles based on the author, which is clickable. Editors do not have the ability to add comments; only registered readers can comment. Readers can view articles without registering and can filter articles by author. An editor can only edit and delete their own articles. If you choose to delete an article, whether from the index or article_detail, a confirmation page will load, asking you to confirm the deletion of that article.

When the number of articles exceeds 10, pagination is triggered on the frontend.

## Superuser

For the superuser, you need to go to the login page and log in with the username super and the password password123. There, you will see all the users that have been created. You can delete a user or create a new one. If you view a user, you can use JavaScript to toggle the editor status on and off, and by clicking on the username, you can load and view all the articles they have created.