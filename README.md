# ml_project_template  
A scalable and modular template for machine learning projects, featuring CI/CD integration, configuration management, robust testing, Dockerization, and comprehensive documentation. Ideal for production-ready ML workflows.

---

## Table of Contents  
- [ml\_project\_template](#ml_project_template)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Datasets](#datasets)
  - [Model](#model)
  - [Results](#results)
  - [Installation](#installation)
  - [Usage](#usage)
    - [1. Running Data Ingestion](#1-running-data-ingestion)
      - [Available Options](#available-options)
    - [2. Running Model Training](#2-running-model-training)
      - [Available Options](#available-options-1)
    - [Example Runs](#example-runs)
    - [Notes](#notes)
  - [Configuration](#configuration)
  - [Project Structure](#project-structure)
  - [Technologies Used](#technologies-used)
  - [**Automated Test Suite Documentation**](#automated-test-suite-documentation)
  - [**Test Categories and Coverage**](#test-categories-and-coverage)
    - [**1. REST API Tests**](#1-rest-api-tests)
      - [**Test Cases:**](#test-cases)
    - [**2. Data Ingestion Tests**](#2-data-ingestion-tests)
      - [**Test Cases:**](#test-cases-1)
    - [**3. Data Transformation Tests**](#3-data-transformation-tests)
      - [**Test Cases:**](#test-cases-2)
    - [**4. Model Selection Tests**](#4-model-selection-tests)
      - [**Test Cases:**](#test-cases-3)
    - [**5. Command-Line Argument Tests**](#5-command-line-argument-tests)
      - [**Test Cases:**](#test-cases-4)
  - [**Execution Instructions**](#execution-instructions)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

---

## Description  
This project provides a reusable template to kickstart machine learning workflows. Designed for scalability, modularity, and production readiness, it features:  
- Clear pipeline-based architecture for training and prediction.  
- REST API and web applications for serving predictions.  
- Robust testing for ensuring reliability.  

---

## Features  
- Modular pipelines for data ingestion, transformation, model selection, and prediction.  
- REST API and Flask-based web UI for prediction services.  
- Logging and error handling with customizable configurations.  
- Comprehensive test suite with coverage reports.  

---

## Datasets  
- **Source**: [Provide dataset source here, e.g., Hugging Face Dataset Library]  
- **Preprocessing**: Includes normalization, handling missing values, and feature engineering.  
- **Licensing**: [Specify dataset licensing details here]  

---

## Model  
- **Algorithms**: Implements `Random Forest`, `Linear Regression`, `XGBoost`, `CatBoost`, and more.  
- **Hyperparameters**: Configurable via YAML/JSON files.  
- **Evaluation**: Selects the best model based on R² scores across various algorithms.  

---

## Results  
- **Performance Metrics**:  
  - Random Forest: R² = 0.845  
  - Linear Regression: R² = 0.885  
  - XGBoost: R² = 0.875  
- **Artifacts**:  
  - Best Model: Saved as `model.pkl` in the `artifacts/` directory.  
  - Preprocessor: Saved as `preprocessor.pkl`.  

---

## Installation  
1. Clone the repository:  
   ```bash
   git clone [repository-url]
   cd ml_project_template
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. (Optional) Set up a virtual environment:  
   ```bash
   python -m venv venv  
   source venv/bin/activate  # On Linux/Mac  
   venv\Scripts\activate     # On Windows  
   ```  

---

## Usage  
The project supports two primary workflows:  
1. Data Ingestion (Download & Prepare Datasets)  
2. Model Training (Train ML Models)  

These workflows can be executed via command-line arguments.

---

### 1. Running Data Ingestion  
To ingest data, use the following command:
```bash
python launch.py ingest --config config/ingestion_config.yaml --debug
```
#### Available Options
| Argument  | Description | Default |
|------------|------------|---------|
| `--config` | (Optional) Path to ingestion configuration file | None |
| `--debug` | (Optional) Enable debug mode | `False` |

---

### 2. Running Model Training  
To train a model, run:
```bash
python launch.py train --config config/model_config.yaml --debug
```
#### Available Options
| Argument  | Description | Default |
|------------|------------|---------|
| `--config` | (Optional) Path to training configuration file | `config/model_config.yaml` |
| `--debug` | (Optional) Enable debug mode | `False` |
| `--model-type` | (Optional) Specify one or more models to train (e.g., `"RandomForest DecisionTree"`) | Runs all models if not provided |
| `--best-of-all` | (Optional) If set, overrides `--model-type` and trains all models to find the best one | `False` |
| `--save-best` | (Optional) If set, saves the best-performing model after training | `False` |

---

### Example Runs  
- Run data ingestion with a custom config file:  
  ```bash
  python launch.py ingest --config my_custom_ingestion.yaml
  ```  
- Run model training in debug mode:  
  ```bash
  python launch.py train --debug
  ```  
- Train a specific model (e.g., CatBoost and Linear Regression):  
  ```bash
  python launch.py train --model-type "CatBoosting Regressor" "Linear Regression"
  ```  
- Train all models and pick the best one automatically:  
  ```bash
  python launch.py train --best-of-all
  ```  
- Train all models and save the best one:  
  ```bash
  python launch.py train --best-of-all --save-best
  ```  

---

### Notes
- If no `--config` is provided, default configurations will be used.
- If `--model-type` is not provided, all models will be trained.
- Using `--best-of-all` will override `--model-type` and automatically determine the best model.
- The `--save-best` flag ensures that the best model is stored after training.
- The script logs all activity for debugging and monitoring.

---

## Configuration  
- **Logging**: Configurable via environment variables (`LOG_LEVEL`, `LOG_JSON`).  
- **Hyperparameters**: Adjustable in `config/params.yaml`.  
- **Artifacts Directory**: Defined in `config/pipeline.yaml`.  

---

## Project Structure  
```plaintext  
ml_project_template/  
├── artifacts/              # Model and preprocessor artifacts  
├── config/                 # Configuration files  
├── src/                    # Core project source code  
│   ├── pipeline/           # Pipelines for training and prediction  
│   ├── services/           # Modular services for ingestion, transformation, etc.  
│   ├── utils/              # Utility functions for file handling and ML helpers  
├── tests/                  # Test cases  
├── requirements.txt        # Python dependencies  
└── README.md               # Project documentation  
```  

---

## Technologies Used  
- Python  
- Scikit-learn, XGBoost, CatBoost  
- FastAPI, Flask  
- Pytest  
- Docker (optional)  

---

## **Automated Test Suite Documentation**  

The project includes a comprehensive suite of tests to validate the functionality, robustness, and reliability of key components. Below is a categorized list of all tests with their purposes and expected outcomes, updated to reflect recent changes.  

---

## **Test Categories and Coverage**  

### **1. REST API Tests**  
**Located in**: `tests/test_rest_api.py`  

#### **Test Cases:**  
| **Test Name**                   | **Purpose**                                                                                           | **Expected Outcome**                                                                                          |
|----------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `test_predict_success`           | Tests the `/predict` endpoint with valid input data.                                                  | Returns a `200 OK` response with a valid prediction.                                                         |
| `test_predict_validation_error`  | Validates that the `/predict` endpoint handles missing or invalid input fields correctly.             | Returns a `400 Bad Request` response with detailed validation errors.                                         |
| `test_predict_missing_payload`   | Ensures the `/predict` endpoint handles empty or missing JSON payloads.                               | Returns a `422 Unprocessable Entity` response with an appropriate error message.                              |
| `test_root_endpoint`             | Verifies the root (`/`) endpoint functionality.                                                       | Returns a `200 OK` response with a health check message.                                                      |

---

### **2. Data Ingestion Tests**  
**Located in**: `tests/test_services/test_data_ingestion.py`  

#### **Test Cases:**  
| **Test Name**                       | **Purpose**                                                                                     | **Expected Outcome**                                                                                          |
|-------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `test_data_ingestion_with_missing_file` | Ensures the data ingestion process handles missing input files gracefully.                      | Raises a `CustomException` caused by a `FileNotFoundError`, with a message referencing the missing file.       |
| `test_data_ingestion_creates_files`  | Validates that data ingestion correctly creates train and test files from the input dataset.     | Generated train and test files exist in the specified paths and contain valid data.                           |

---

### **3. Data Transformation Tests**  
**Located in**: `tests/test_services/test_data_transformation.py`  

#### **Test Cases:**  
| **Test Name**                         | **Purpose**                                                                                     | **Expected Outcome**                                                                                          |
|---------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `test_data_transformation`            | Ensures the data transformation process works as expected with valid inputs.                    | Returns transformed train and test arrays with expected shapes and saves the preprocessor object.             |
| `test_data_transformation_missing_columns` | Validates that the transformation process handles missing required columns appropriately.       | Raises a `CustomException` indicating the missing columns.                                                    |

---

### **4. Model Selection Tests**  
**Located in**: `tests/test_services/test_model_selection.py`  

#### **Test Cases:**  
| **Test Name**                       | **Purpose**                                                                                     | **Expected Outcome**                                                                                          |
|-------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `test_initiate_model_trainer_success` | Validates the selection and evaluation of the best model from the given data.                   | Ensures a valid model report is returned, the best model is identified, and its score meets expectations.      |
| `test_no_model_meets_threshold`     | Ensures an exception is raised when no model meets the minimum performance threshold.            | Raises a `CustomException` with a message indicating no best model was found.                                 |
| `test_invalid_data_handling`        | Tests the behavior of model selection when invalid training and testing data are provided.       | Returns a model report with `None` scores for all but Linear Regression, which should score 1.0.              |

---

### **5. Command-Line Argument Tests**  
**Located in**: `tests/test_command_line.py`  

#### **Test Cases:**  
| **Test Name**                         | **Purpose**                                                                                     | **Expected Outcome**                                                                                          |
|---------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `test_parse_arguments_ingest_monkey`  | Tests argument parsing for the `ingest` command using `monkeypatch`.                            | Ensures `ingest` is recognized and `config` is properly set.                                                 |
| `test_parse_arguments_train_monkey`   | Tests argument parsing for the `train` command with `monkeypatch`.                             | Ensures `train` command is parsed and `--debug` is correctly set to `True`.                                  |
| `test_parse_arguments_ingest_mock`    | Tests `ingest` command parsing using `patch`.                                                 | Ensures correct argument assignment for `ingest`.                                                            |
| `test_parse_arguments_train_mock`     | Tests `train` command parsing using `patch`.                                                  | Ensures correct argument assignment for `train`.                                                             |
| `test_parse_arguments_ingest_no_config` | Ensures `ingest` works without a specified config file.                                        | Confirms default config behavior when none is provided.                                                      |
| `test_parse_arguments_train_no_debug` | Ensures `train` command behavior when `--debug` is not passed.                                | Confirms `debug` defaults to `False` and correct model config is used.                                       |
| `test_parse_arguments_ingest_with_debug` | Ensures `ingest` command accepts the `--debug` flag.                                         | Verifies `debug` is correctly set to `True`.                                                                |
| `test_parse_arguments_no_command`     | Tests behavior when no command is provided.                                                  | Ensures the application exits with an error.                                                                |

---

## **Execution Instructions**  

1. Ensure all dependencies are installed using:  
   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests using `pytest`:  
   ```bash
   PYTHONPATH=$(pwd) pytest -v
   ```

3. To run a specific test module, use:  
   ```bash
   PYTHONPATH=$(pwd) pytest -v tests/<test_module_name>.py
   ```

4. To generate a coverage report:  
   ```bash
   PYTHONPATH=$(pwd) pytest --cov=src --cov-report=html
   ```
   - View the HTML report in the generated `htmlcov` directory.

---

## Contributing  
1. Fork the repository.  
2. Create a new feature branch:  
   ```bash  
   git checkout -b feature/your-feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add your message"  
   ```  
4. Push to the branch:  
   ```bash  
   git push origin feature/your-feature-name  
   ```  
5. Submit a pull request.  

---

## License  
[Specify the license here, e.g., MIT License.]  

---

## Acknowledgements  
- Scikit-learn documentation for algorithm support.  
- Community contributors for feedback and improvements.  
```
