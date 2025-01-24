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

## Logging Functionality

This project features an enhanced logging system powered by `LoggerManager`, which provides structured and flexible logging to both files and the console. Key features include:

- **Plain Text and JSON Logs**: Toggle between plain text and JSON log formats for better integration with modern logging pipelines.
- **Dynamic Log Levels**: Customize log verbosity using environment variables or `.env` configuration.
- **Rotating File Logs**: Automatically rotates logs to avoid disk space issues.

### Configurable Environment Variables

You can control the logging behavior through the following environment variables, either set directly or configured in a `.env` file at the root of the project:

| Environment Variable | Default Value | Description |
|-----------------------|---------------|-------------|
| `LOG_LEVEL`          | `INFO`        | Sets the logging level. Possible values are `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. |
| `LOG_JSON`           | `false`       | Set to `true` to enable structured JSON logs. If `false`, logs will be in plain text format. |

### .env File Example

Create a `.env` file in the root of your project to configure logging and other environment variables:

```env
LOG_LEVEL=DEBUG
LOG_JSON=true
```

### Example Usage

1. **Configure Logging with `.env`**:
   - Add the above `.env` file to the project root.

2. **Run the Application**:
   ```bash
   python launch_host.py --config /path/to/config.yaml
   ```

3. **Log Output**:

   **Plain Text Logs**:
   ```plaintext
   [ 2025-01-24 13:00:00 ] INFO [launch_host:12] - Launching host with arguments: {'config': 'path/to/config', 'host': '0.0.0.0'}
   ```

   **JSON Logs**:
   ```json
   {
     "timestamp": "2025-01-24 13:00:00",
     "level": "INFO",
     "logger": "launch_host",
     "line": 12,
     "message": "Launching host with arguments: {'config': 'path/to/config', 'host': '0.0.0.0'}"
   }
   ```

---

## .env Configuration

The `.env` file allows centralized and secure management of environment variables. In addition to logging configuration, it can store sensitive information like API keys or database connection strings.

### Best Practices for `.env` Files
- **Do not commit the `.env` file to version control**. Add it to `.gitignore` to avoid exposing sensitive information.
- Use a template file like `.env.example` to document expected variables for collaborators.

---

This integration of `LoggerManager`, `.env` configuration, and clearly defined script roles ensures a robust, modular, and production-ready setup for machine learning workflows.


---

## Roles of Key Scripts

### `predict_app.py`
The `predict_app.py` script serves as the main entry point for the Flask web application. It:
- Handles user inputs via a web interface.
- Validates inputs using the `PredictionInputSchema` to ensure data quality.
- Sends inputs to the `PredictPipeline` for generating predictions.
- Displays the prediction results or error messages back to the user.

### `launch_host.py`
The `launch_host.py` script initializes and hosts backend services. It:
- Serves as the entry point for running asynchronous backend tasks.
- Facilitates hosting of machine learning pipelines or other infrastructure components.
- Includes configuration options for deployment and runtime behavior.



