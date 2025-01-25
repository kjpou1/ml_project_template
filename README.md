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

-