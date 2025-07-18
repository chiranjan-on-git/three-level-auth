# 3-Level Authentication System (Flask)

This project demonstrates a basic multi-stage authentication system built with Flask. Users must successfully navigate through three distinct authentication levels to gain access to a final "success" page.

## Project Overview

This Flask application simulates a layered security system where a user progresses through sequential authentication steps. It's designed as a simple demonstration of session management and multi-factor authentication concepts in a web environment.

## Features

*   **Level 1: Username and Password Login:** Standard initial authentication.
*   **Level 2: Security Question Challenge:** Adds an extra layer of verification.
*   **Level 3: Simulated Approval Step:** Represents a final gate, such as admin approval or a fixed confirmation.
*   **Session Management:** Uses Flask sessions to maintain user state across authentication levels.
*   **Basic Routing:** Clear separation of authentication stages using Flask routes.

## How It Works

The application defines a linear authentication flow:

1.  **Initial Login (`/`):** The user enters a hardcoded username and password. If successful, their username is stored in the session, and they are redirected to Level 2.
2.  **Security Question (`/level2`):** The user must answer a specific security question correctly. Success leads to Level 3.
3.  **Approval Step (`/level3`):** The user must provide a specific "approval" input. If correct, they are redirected to the final success page.
4.  **Success Page (`/success`):** Accessible only after completing all three levels.

If a user attempts to access a higher level without completing the previous one (i.e., without `session['user']` being set), they will be redirected back to the login page.

## Demo User Credentials

For demonstration purposes, the following user is pre-configured:

*   **Username:** `john`
*   **Password:** `1234`
*   **Security Question Answer:** `blue`
*   **Level 3 Approval Input:** `yes`

## Project Structure

For the application to run correctly, you will need the following files:

<img width="297" height="309" alt="image" src="https://github.com/user-attachments/assets/f4cfb7fe-96b1-48aa-b5a2-81a8532166db" width = 400 />

## Generated code
*   `app.py`: The main Flask application logic.
*   `requirements.txt`: Lists Python dependencies.
*   `templates/`: Directory containing the HTML templates for each authentication level and the success page. *(Note: The HTML files are not provided in this `app.py` snippet but are necessary for the application to function.)*

## Technologies Used

*   Python 3.x
*   Flask

## Setup and How to Run

1.  **Clone the repository** (or save `app.py` and create the `templates` directory manually).
2.  **Navigate to the project directory** in your terminal.
3.  **Install Flask:**
    ```bash
    pip install Flask
    ```
    *(Alternatively, create a `requirements.txt` file with `Flask` inside and run `pip install -r requirements.txt`)*
4.  **Create the HTML templates** in the `templates` directory:
    *   `login.html`
    *   `level2.html`
    *   `level3.html`
    *   `success.html`
    (Each HTML file should contain a form for user input corresponding to its authentication level.)
5.  **Run the application:**
    ```bash
    python app.py
    ```
6.  Open your web browser and go to `http://127.0.0.1:5000/` (or the port indicated in your console if different).

## Security Considerations (IMPORTANT)

**THIS PROJECT IS FOR DEMONSTRATION PURPOSES ONLY AND IS NOT SECURE FOR PRODUCTION USE.**

Key security vulnerabilities include:

*   **Hardcoded Credentials:** Usernames and passwords are hardcoded in `app.py` in plain text.
*   **Insecure Secret Key:** `app.secret_key = 'securekey'` is extremely insecure. In a real application, this should be a long, random, and securely stored key.
*   **Lack of Hashing:** Passwords are not hashed or salted.
*   **Simple Security Question:** The security question is fixed and easily bypassable.
*   **No Input Validation/Sanitization:** User inputs are not validated, making the application vulnerable to various attacks (e.g., XSS).
*   **No Rate Limiting:** No protection against brute-force attacks on login or security question attempts.
*   **No CSRF Protection:** Forms are vulnerable to Cross-Site Request Forgery.

