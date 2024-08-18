markdown
# Proxy Server with Authentication and Middleware

This project is a proxy server built using Python with a microservice architecture. The main focus of this project is on authentication, incorporating various types of authentication methods used in real-life services for validation. Separate log files are generated for each event.

## Project Structure

proxy_server/
│
├── src/ # Source code for the proxy server
│ ├── init.py # Initialize the src package
│ ├── main.py # Entry point of the proxy server
│ ├── config.py # Configuration settings
│ ├── authentication/ # Authentication-related modules
│ │ ├── init.py
│ │ ├── auth_methods.py # Different authentication methods
│ │ ├── token_manager.py# Token management (JWT, OAuth)
│ │ ├── user_manager.py # User management (e.g., user validation)
│ │
│ ├── middleware/ # Middleware components
│ │ ├── init.py
│ │ ├── logging_middleware.py # Middleware for logging events
│ │ ├── auth_middleware.py # Middleware for authentication
│ │
│ ├── utils/ # Utility functions and helpers
│ │ ├── init.py
│ │ ├── logger.py # Logging utility
│ │ ├── error_handler.py# Error handling utility
│ │
│ ├── services/ # Service layers for proxy server functionalities
│ │ ├── init.py
│ │ ├── request_handler.py # Handling incoming requests
│ │ ├── response_handler.py # Handling outgoing responses
│ │
│ └── tests/ # Test cases for the project
│ ├── init.py
│ ├── test_authentication.py # Tests for authentication
│ ├── test_middleware.py # Tests for middleware
│ ├── test_services.py # Tests for services
│
├── logs/ # Directory for log files
│ ├── authentication.log # Log file for authentication events
│ ├── errors.log # Log file for errors
│ ├── events.log # Log file for general events
│
├── requirements.txt # List of project dependencies
└── README.md # Project documentation and instructions

perl
Copy code

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/proxy_server.git
    cd proxy_server
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set the `SECRET_KEY` environment variable:**

    ```sh
    export SECRET_KEY='your_secret_key'  # On Windows: set SECRET_KEY=your_secret_key
    ```

## Running the Proxy Server

1. **Run the main script:**

    ```sh
    python src/main.py
    ```

2. **Verify the output:**

    Ensure that the middleware processes the request correctly, and the response is as expected.

## Testing

1. **Run the tests:**

    ```sh
    python -m unittest discover src/tests
    ```

2. **Check the logs:**

    - `logs/authentication.log`: Log file for authentication events.
    - `logs/errors.log`: Log file for errors.
    - `logs/events.log`: Log file for general events.

## Features

- JWT Authentication
- Middleware for logging and authentication
- Separate logging for different events
- Microservice architecture

## Usage

- Customize the authentication methods in `src/authentication/auth_methods.py`.
- Implement additional middleware in `src/middleware`.
- Expand the request and response handling in `src/services`.

## Contributing

Feel free to open issues and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.