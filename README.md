
# FastAPI To-Do List Application

This project is a simple **RESTful To-Do List API** built with **Python** and **FastAPI**, using a SQLite database.  It lets you create, read, update, and delete tasks (to-do items) via HTTP requests. The API supports JSON input and output, and includes user authentication with JWT tokens (see *“Authentication”* below). The full interactive API documentation is available at `/docs` (Swagger UI) and `/redoc` once the app is running.

## Tech Stack

* **Python 3.9+** – Programming language
* **FastAPI** – Web framework for building APIs
* **SQLite** – Lightweight file-based database
* **SQLAlchemy** (ORM) – Database access layer (if used in code)
* **Uvicorn** – ASGI server for running the app
* **Docker & Docker Compose** – Containerization and easy deployment

## Setup (Local)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dakshk19/todolistgit.git
   cd todolistgit
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv env
   source env/bin/activate    # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**
   (This project uses FastAPI and a database connector.)

   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database (if needed):**
   The project includes a SQLite file `task.db`. If you need to start fresh, delete `task.db` and run a migration or let the app recreate it. (Check the code for DB creation logic.)

5. **Run the FastAPI server:**

   ```bash
   uvicorn Todo_fastapi.main:app --reload
   ```

   The server will start on `localhost:8000` by default. You should see output like:

   ```
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   ```

   You can now access the API at this address.

6. **Verify interactive docs:**
   Open your browser to [localhost:8000/docs](http://127.0.0.1:8000/docs) for the Swagger UI, or [localhost:8000/redoc](http://127.0.0.1:8000/redoc) for ReDoc. FastAPI automatically provides these documentation pages.

## Setup (Docker)

A `Dockerfile` and `docker-compose.yml` are included for containerized deployment. You can run the app in Docker as follows:

* **Build the Docker image:**

  ```bash
  docker build -t todolist-app .
  ```

* **Run with Docker Compose:**

  ```bash
  docker-compose up
  ```

  This will start the FastAPI app in a container, exposing port `8000`. You can also use `docker run -p 8000:8000 todolist-app` if you prefer not to use Compose.

* **Access the app:**
  Once running in Docker, open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser to see the API docs. The API endpoints function the same as in local mode.

## API Endpoints

The To-Do API provides the following endpoints (assumes base URL `http://localhost:8000`):

* **`POST /users/`** – Create a new user account (provides username/password).

* **`POST /login/`** – Authenticate with username/password and receive a JWT token. Use this token for authorized endpoints (in an `Authorization: Bearer <token>` header).

* **`GET /todos/`** – *List all tasks.* Returns a JSON array of tasks.
  **Example:**

  ```bash
  curl -X GET "http://localhost:8000/todos/"
  ```

  **Response:**

  ```json
  [
    {"id": 1, "title": "Buy groceries", "description": "Milk, Eggs", "completed": false},
    {"id": 2, "title": "Walk dog",      "description": "",       "completed": true}
  ]
  ```

* **`GET /todos/{id}/`** – *Get a task by ID.* Replace `{id}` with the task’s ID.

  ```bash
  curl -X GET "http://localhost:8000/todos/1/"
  ```

  **Response (JSON):**

  ```json
  {"id": 1, "title": "Buy groceries", "description": "Milk, Eggs", "completed": false}
  ```

* **`POST /todos/`** – *Create a new task.* Send JSON with task details (e.g., `title`, `description`).

  ```bash
  curl -X POST "http://localhost:8000/todos/" \
    -H "Content-Type: application/json" \
    -d '{"title": "Read book", "description": "Finish chapter 4"}'
  ```

  **Response:** Newly created task object (JSON), e.g.:

  ```json
  {"id": 3, "title": "Read book", "description": "Finish chapter 4", "completed": false}
  ```

* **`PUT /todos/{id}/`** – *Update an existing task.* Provide the updated fields in JSON.

  ```bash
  curl -X PUT "http://localhost:8000/todos/3/" \
    -H "Content-Type: application/json" \
    -d '{"title": "Read book", "description": "Finish chapter 4", "completed": true}'
  ```

  **Response:** Updated task object.

* **`DELETE /todos/{id}/`** – *Delete a task by ID.*

  ```bash
  curl -X DELETE "http://localhost:8000/todos/3/"
  ```

  **Response:** `204 No Content` (if deleted successfully).

All endpoints that modify data (`POST`, `PUT`, `DELETE`) may require a valid JWT in the `Authorization` header after logging in, depending on the code’s security implementation.

## Usage Examples

1. **List all tasks:**

   ```bash
   curl http://localhost:8000/todos/
   ```
2. **Create a task:**

   ```bash
   curl -X POST http://localhost:8000/todos/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk and Eggs"}'
   ```
3. **Get a specific task (ID=1):**

   ```bash
   curl http://localhost:8000/todos/1/
   ```
4. **Update task 1 to mark it completed:**

   ```bash
   curl -X PUT http://localhost:8000/todos/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk and Eggs", "completed": true}'
   ```
5. **Delete task 1:**

   ```bash
   curl -X DELETE http://localhost:8000/todos/1/
   ```

*(Use `Authorization: Bearer <token>` header with your JWT for endpoints that require login.)*

## Additional Notes

* **API Documentation:** After running the server, interactive docs are available at `/docs` (Swagger UI) and `/redoc`. These pages list all endpoints, schemas, and allow you to test calls directly from the browser.
* **Database:** Data is stored in **SQLite** (`task.db`). For production, you might switch to PostgreSQL or MySQL. Ensure the database file is writable by the application.
* **Contributing:** Contributions are welcome! Feel free to open issues or pull requests to add features (user roles, due dates, etc.) or improve the code.
* **Contact:** For questions or feedback, reach out to the repository maintainer (@dakshk19)


	
