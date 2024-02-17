
<img src='https://img.freepik.com/free-psd/3d-illustration-doctor-placing-vaccine-injection_1419-2774.jpg'>

# MediSync 🩺

MediSync is a project designed to manage hospitals. It offers a comprehensive platform for managing patient, doctor, and appointment records. The project is built using Django, HTML, CSS, and JavaScript. MediSync includes features such as patient record management, appointment creation, and a visually appealing user interface with a dark mode and customizable button colors.. 🏥📝⏰

## Installation and Usage

To run the MediSync project locally or using Docker, follow these steps:

1. **Clone the project repository** to your local machine using the following command:
   ```bash
   git clone https://github.com/samadpls/MediSync.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd MediSync
   ```

3. **Install the necessary dependencies** listed in the project's requirements file.
   ```bash
   pip install -r requirements.txt
   ```

4. **Perform database migrations** using the following command:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Django development server**:
   ```bash
   python manage.py runserver
   ```
---
   **OR**, if you want to use Docker:

5. **Run the project using Docker Compose:** (make sure you have Docker installed):
   ```bash
   docker-compose up
   ```

6. Access the project in your web browser using the provided URL.

## Components

The MediSync project is divided into three main components:

1. **MediSync:** The main project directory that contains project-level configurations and settings.

2. **App Website:** The Django app responsible for handling the website functionality, including patient and doctor management, appointment creation, and patient record management.

3. **Database App:** A Django app responsible for connecting to the database and handling data storage and retrieval using SQLite3.

## Features

MediSync offers the following features:

- Patient Management: Allows editing, updating, saving, and deleting patient information. ✍️👥
- Doctor Management: Allows editing, updating, saving, and deleting doctor information. ✍️👩‍⚕️👨‍⚕️
- Appointment Management: Provides the ability to create, view, and manage appointments through the system. 🗓️👥
- Patient Record Management: Enables viewing the patient's complete record, including appointment history and other relevant information. 📄👥
- REST APIs: Uses JavaScript to control REST APIs for interacting with the backend and retrieving data. 🚀🔌
- Dark Mode: Offers a visually appealing dark mode for the user interface. 🌙🖤
- Customizable Button Colors: Allows customization of button colors to suit personal preferences. 🎨🔘

## Technologies Used

The MediSync project utilizes the following technologies:

- Django: A high-level Python web framework used for rapid development and clean design.
- HTML: Markup language for creating the structure and content of web pages.
- CSS: Stylesheet language used for describing the presentation of a document written in HTML.
- JavaScript: A programming language used to add interactivity and dynamic functionality to web pages.
- SQLite3: A lightweight, file-based database system used for data storage.

## Contributing

Contributions to the MediSync project are welcome! If you find any issues or have suggestions for improvement, please submit a pull request or open an issue on the project repository.

## License

The MediSync project is licensed under the [MIT License](LICENSE).

Feel free to customize and modify the project according to your needs. This is just a template for your README file, and you can add or modify sections as required.



https://github.com/samadpls/MediSync/assets/94792103/5ca6b666-c223-4cfc-8675-1383c069427f


