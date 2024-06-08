Brainstormer
============

<p align="center">
  <img src="src/assets/brainstormer_logo.png" alt="Brainstormer Logo" width="100" height="100">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Vue.js-3.0-green" alt="Vue.js">
  <img src="https://img.shields.io/badge/Flask-2.0-blue" alt="Flask">
  <img src="https://img.shields.io/badge/Bootstrap-5.0-purple" alt="Bootstrap">
  <img src="https://img.shields.io/badge/axios-0.21.1-orange" alt="Axios">
</p>

<p align="center">
  Your ultimate tool for capturing and organizing your brilliant ideas collaboratively!
</p>

**Brainstormer** is a web application built using Vue.js for the frontend and Flask for the backend. It allows teams to create brainstorming sessions, add ideas to these sessions, vote on ideas, and manage sessions and ideas efficiently in a collaborative environment.

![App Demo](src/assets/brainstormer.gif)

Table of Contents
-----------------

-   [Features](#features)
-   [Tech Stack](#technologies-used)
-   [Project Structure](#project-structure)
-   [Setup and Installation](#setup-and-installation)
-   [Usage](#usage)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

Features
--------

-   **Create Brainstorming Sessions:** Easily create new sessions for different brainstorming activities.
-   **Add Ideas:** Quickly add ideas to any session.
-   **Vote on Ideas:** Vote for the ideas you like the most.
-   **Delete Sessions and Ideas:** Manage your sessions by deleting them or their ideas when they are no longer needed.
-   **Collaborative Environment:** Work together with your team in real-time to brainstorm and refine ideas.

Tech Stack
-----------------

-   **Frontend:**

    -   [Vue.js](https://vuejs.org/)
    -   [Axios](https://axios-http.com/)
    -   [Bootstrap](https://getbootstrap.com/)
-   **Backend:**

    -   [Flask](https://flask.palletsprojects.com/en/3.0.x/)
    -   [Flask-CORS](https://flask-cors.readthedocs.io/)
    -   [PostgreSQL](https://www.postgresql.org/)

Project Structure
-----------------


    ├── babel.config.js
    ├── backend
    │   └── app.py
    ├── jsconfig.json
    ├── package.json
    ├── package-lock.json
    ├── public
    │   ├── favicon.ico
    │   └── index.html
    ├── README.md
    ├── src
    │   ├── App.vue
    │   ├── assets
    │   │   └── brainstormer_logo.png
    │   ├── components
    │   │   ├── IdeaForm.vue
    │   │   ├── IdeaItem.vue
    │   │   ├── IdeaList.vue
    │   │   ├── SessionItem.vue
    │   │   └── SessionList.vue
    │   └── main.js
    └── vue.config.js

Setup and Installation
----------------------

### Prerequisites

-   [Node.js](https://nodejs.org/)
-   [Python](https://www.python.org/)
-   [Flask](https://flask.palletsprojects.com/en/3.0.x/)

### Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

    VUE_APP_API_BASE_URL=http://localhost:5000
    DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase

 Replace `username`, `password`, `localhost`, `5432`, and `mydatabase` with your PostgreSQL database credentials.

### Frontend Setup

1.  Clone the repository:

    ```bash
    git clone https://github.com/abeltavares/brainstormer.git
    ```

2.  Install dependencies:

    ```bash
    npm install
    ```

3.  Start the frontend development server:

```bash
npm run serve
```

### Backend Setup

1.  Navigate to the backend directory:

    ```bash
    cd backend
    ```

2.  Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up the database:

    ```bash
    flask db upgrade
    ```

5.  Run the Flask server:

    ```bash
    flask run
    ```

Usage
-----

1.  Open your browser and navigate to `http://localhost:8080` to access the Brainstormer app.
2.  Create a new brainstorming session by entering a session title and clicking "Add Session".
3.  Share the session link with your team members, so they can join and contribute in real-time.
4.  Add ideas to the session, vote on ideas, and manage the sessions and ideas using the available options.
5.  Collaborate with your team to refine and prioritize ideas effectively.

Contributing
------------

We welcome contributions! Here's how you can help:

1.  Fork the repository.
2.  Create a new branch: `git checkout -b feature-name`.
3.  Make your changes and commit them: `git commit -m 'Add some feature'`.
4.  Push to the branch: `git push origin feature-name`.
5.  Open a pull request.

License
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

<br>

Happy Brainstorming! 💡

<hr>

[Go to Top](#table-of-contents)