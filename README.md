# Python Deployment Pre-Check

A Python-based deployment pre-check tool that validates environment configuration, required environment variables, API availability, and overall deployment readiness.

## Features

- Accepts the deployment environment through command-line arguments
- Loads environment-specific configuration from JSON
- Validates required configuration
- Checks required environment variables
- Performs API health checks
- Uses a 5-second request timeout
- Handles HTTP and network failures
- Returns meaningful exit codes for automation and CI/CD pipelines

## Technologies

- Python
- JSON
- Requests
- Environment variables
- Command-line arguments

## Project Structure

```text
python-deployment-precheck/
├── deployment_precheck.py
├── config.json
└── README.md