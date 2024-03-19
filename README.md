# Project Gutenberg Backend

Project Gutenberg Backend is a Django application that serves as the backend for the Project Gutenberg platform. It provides APIs for users to find books based on popularity and download them via links.

## Features

- Retrieve books based on popularity.
- Download books via links provided in the API response.
- Swagger documentation for easy API testing.

## Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework
- drf-yasg (Swagger integration)

## Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Install dependencies:


4. Apply database migrations:


5. Start the development server:


The application will be accessible at http://localhost:8000.

## API Documentation

The API documentation is available via Swagger UI. After starting the development server, navigate to http://localhost:8000/swagger/ to view the API documentation.

## Deployment

The application can be deployed to various hosting platforms such as Heroku, AWS, or PythonAnywhere. Refer to the hosting provider's documentation for specific deployment instructions.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

