# ml_project_template
A scalable and modular template for machine learning projects, featuring CI/CD integration, configuration management, robust testing, Dockerization, and comprehensive documentation. Ideal for production-ready ML workflows.

---

## Notes on Requirements and Installation

The `setup.py` script dynamically parses the `requirements.txt` file for dependencies, but explicitly excludes the editable installation directive (`-e .`). This is because:

- Editable installations (`-e .`) are intended for local development and are not portable across environments.
- To work on the package in editable mode, run the following command manually:

  ```bash
  pip install -e .
  ```

---

## REST API Documentation

This project features a FastAPI-based REST API for prediction tasks. The API provides endpoints for submitting input data and receiving predictions.

### Base URL

```plaintext
http://<host>:<port>
```

Default host: `0.0.0.0`, port: `8000`

---

### Endpoints

#### **Root Endpoint**
- **URL**: `/`
- **Method**: `GET`
- **Description**: Verifies that the API is running.
- **Response**:
  ```json
  {
      "message": "FastAPI Prediction Service is running"
  }
  ```

#### **Prediction Endpoint**
- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Accepts input data, validates it, and returns a prediction or an error response.

**Request Schema**:
- **Payload**:
  ```json
  {
      "payload": {
          "data": {
              "gender": "male",
              "race_ethnicity": "group A",
              "parental_level_of_education": "high school",
              "lunch": "standard",
              "test_preparation_course": "none",
              "reading_score": 72.0,
              "writing_score": 74.0
          }
      }
  }
  ```

**Response**:

1. **Successful Response** (`200 OK`):
   ```json
   {
       "code": 0,
       "code_text": "ok",
       "message": "Processed successfully.",
       "data": {"math_score": 76.9151611328125}
   }
   ```

2. **Validation Error** (`400 Bad Request`):
   ```json
   {
       "code": -1,
       "code_text": "error",
       "message": "Validation error occurred.",
       "errors": [
           {"field": "reading_score", "error": "value is not a valid float"},
           {"field": "writing_score", "error": "field required"}
       ]
   }
   ```

3. **Internal Server Error** (`500 Internal Server Error`):
   ```json
   {
       "code": -1,
       "code_text": "error",
       "message": "An internal server error occurred.",
       "errors": null
   }
   ```

---

### Example Usage

#### Using `curl`
**Request**:
```bash
curl -X POST "http://0.0.0.0:8000/predict" \
-H "Content-Type: application/json" \
-d '{
    "payload": {
        "data": {
            "gender": "male",
            "race_ethnicity": "group A",
            "parental_level_of_education": "high school",
            "lunch": "standard",
            "test_preparation_course": "none",
            "reading_score": 72.0,
            "writing_score": 74.0
        }
    }
}'
```

**Response**:
```json
{
    "code": 0,
    "code_text": "ok",
    "message": "Processed successfully.",
    "data": {"math_score": 76.9151611328125}
}
```

---

## Logging Functionality

This project features an enhanced logging system powered by `LoggerManager`. Key features include:

- **Plain Text and JSON Logs**.
- **Dynamic Log Levels**.
- **Rotating File Logs**.

### Configurable Environment Variables

| Environment Variable | Default Value | Description |
|-----------------------|---------------|-------------|
| `LOG_LEVEL`          | `INFO`        | Sets the logging level. |
| `LOG_JSON`           | `false`       | Enable JSON logs with `true`. |

---

Here's the updated section of the README with documentation for the FastHTML interface:

---

## Roles of Key Scripts

### `predict_app.py`
A Flask-based web application for end-users to interact with the prediction service. It:
- Accepts user inputs via a web form.
- Validates inputs using the `PredictionInputSchema` to ensure data quality.
- Sends inputs to the `PredictPipeline` for generating predictions.
- Displays predictions or error messages back to the user in an interactive interface.

---

### `launch_host.py`
An entry point for running asynchronous backend tasks. It:
- Serves as a host for machine learning pipelines or other backend services.
- Uses the FastAPI framework to facilitate communication and management of internal components.
- Configurable via command-line arguments for deployment and runtime behavior.

---

### `predict_rest_api.py`
A FastAPI-based RESTful API for serving predictions programmatically. It:
- Exposes endpoints to accept structured prediction requests in JSON format.
- Validates inputs with `PredictionInputSchema` for data consistency and reliability.
- Returns structured responses, including predictions, validation errors, or internal error messages.
- Designed for integration with external applications or automation pipelines.

---

### `predict_fasthtml_app.py`
A FastHTML-based web application designed as a lightweight frontend interface to interact with the REST API. It:
- Provides an elegant and responsive HTML interface for input submission.
- Communicates with the FastAPI `predict_rest_api` to send user inputs and display results.
- Handles validation errors returned by the REST API and presents them in a user-friendly format.

#### Key Features:
- **User-Friendly Interface**: 
  - A responsive form to input prediction data, styled with clean HTML and CSS for ease of use.
- **Integration with REST API**:
  - Sends POST requests to the FastAPI service's `/predict` endpoint.
  - Processes responses and displays results or error messages dynamically.

Here’s an updated and clear **"Running the `predict_rest_api.py`"** section for your README:

---

### Running the `predict_rest_api.py`

The `predict_rest_api.py` provides a RESTful API interface for programmatically interacting with the prediction service. It is designed to handle JSON-based requests and respond with structured outputs, making it ideal for integration with external applications or automation pipelines.

#### Prerequisites:
1. Install all dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

#### Starting the REST API Server:
1. Run the `predict_rest_api.py` server using **Uvicorn**:
   ```bash
   uvicorn predict_rest_api:app --host 0.0.0.0 --port 8008 --reload
   ```
   - The `--reload` flag enables automatic reloading of the server whenever code changes, useful for development.
   - The server will be accessible at:
     ```plaintext
     http://127.0.0.1:8008
     ```

#### Interacting with the API:
1. Open a REST client (e.g., **Postman**, **curl**, or a custom client application).
2. Use the `/predict` endpoint to submit prediction requests.

   **Example Request**:
   ```bash
   curl -X POST "http://127.0.0.1:8008/predict" \
   -H "Content-Type: application/json" \
   -d '{
       "payload": {
           "data": {
               "gender": "male",
               "race_ethnicity": "group A",
               "parental_level_of_education": "high school",
               "lunch": "standard",
               "test_preparation_course": "none",
               "reading_score": 72.0,
               "writing_score": 74.0
           }
       }
   }'
   ```

   **Response**:
   - On success:
     ```json
     {
         "code": 0,
         "code_text": "ok",
         "message": "Processed successfully.",
         "data": {"math_score": 76.9151611328125}
     }
     ```
   - On validation error:
     ```json
     {
         "code": -1,
         "code_text": "error",
         "message": "Validation error occurred.",
         "errors": [
             {"field": "reading_score", "error": "value is not a valid float"},
             {"field": "writing_score", "error": "field required"}
         ]
     }
     ```
   - On internal server error:
     ```json
     {
         "code": -1,
         "code_text": "error",
         "message": "An internal server error occurred.",
         "errors": null
     }
     ```

3. Verify the REST API is running by visiting:
   ```plaintext
   http://127.0.0.1:8008/
   ```
   - The root endpoint returns a simple health check message:
     ```json
     {
         "message": "FastAPI Prediction Service is running"
     }
     ```

#### Key Notes:
- The REST API validates all input data before processing and returns helpful error messages in case of validation issues.
- The server is designed for production and can be scaled using tools like **Docker** or **Kubernetes**.


---

### Running the `predict_fasthtml_app.py`

The `predict_fasthtml_app.py` provides a web interface for users to interact with the prediction service via the REST API.

#### Prerequisites:
1. Ensure that all dependencies are installed by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI REST API using the following command:
   ```bash
   uvicorn predict_rest_api:app --host 0.0.0.0 --port 8008 --reload
   ```
   This ensures the REST API is available to handle requests from the FastHTML app.

#### Starting the FastHTML Application:
1. Run the FastHTML app:
   ```bash
   python predict_fasthtml_app.py
   ```
2. Access the FastHTML interface in your browser:
   ```plaintext
   http://127.0.0.1:8009
   ```

#### Interaction:
1. Fill out the form fields (e.g., `Gender`, `Race/Ethnicity`, `Reading Score`, etc.) in the web interface.
2. Click the **Submit** button to send the data to the REST API for prediction.
3. **Response Handling**:
   - **On success**: Displays the predicted `Math Score` in a result section.
   - **On validation error**: Shows error messages returned by the REST API (e.g., missing or invalid inputs).
   - **On server error**: Displays a generic error message, such as "An error occurred."

This simple two-step process makes it easy to run the FastHTML app and interact with the machine learning service.


