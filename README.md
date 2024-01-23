Part of [Assignment](https://github.com/IpshitaSingh/scraper-analyzer) for Software Development class (WiSe '23) - To demonstrate Build Management, CI/CD Pipeline, & Unit Testing

![CI/CD Pipeline](https://github.com/IpshitaSingh/CICD/workflows/CI/CD%20Pipeline/badge.svg)

# Build Management, CI/CD, Tests 

This is a simple application to demostrate integration of build management, CI/CD, and testing with a Flask app. This is done with setuptools (Python library) for build management, GitHub Actions for Continuous Integration/Continuous Deployment (CI/CD), and pytest (Python testing framework) for testing. An additional tool, Docker has been used for containerization and deployment. 

**Choice of Tools** - The primary reason for these choices is Python-centric nature of the tools. For build management, this ensures better compatibility with the Flask app as compared to Java-centric options like Ant, Maven, and Gradle. For CI/CD, the decision to use GitHub Actions over tools such as Travis CI was due to its direct and seamless integration with the GitHub platform.

**Functionality** - Renders the message "Hello World!" locally on a web browser.

## Table of Contents

- [Installation](#installation)
- [Output](#output)
- [Usage](#usage)
- [Build Management](#build-management)
- [CI/CD Pipeline](#cicd-pipeline)
- [Tests](#tests)
- [Docker](#docker)

## Installation

To install the app:

```
git clone https://github.com/IpshitaSingh/CICD.git
cd app
pip install -e .
```
## Usage

To run the app locally:
```
flask run
```
The app should now be functioning on the localhost website.

## Output
Zoomed-in version of the output:
<img src="https://raw.githubusercontent.com/IpshitaSingh/CICD/main/imgs/output.png">

## Build Management
The build management of this project is done using setuptools. This tool streamlines the process of packaging the application, managing dependencies, and preparing it for distribution. The setup.py file contains the metadata and configuration for the project.

### Building the App:
Run the following command to create a distributable package:
```
python setup.py sdist bdist_wheel
```
This command generates source distribution (sdist) and binary distribution (bdist_wheel) packages. These can be used for the local deployment.

## CICD Pipeline
The CI/CD pipeline is set up using GitHub Actions. On each push to the main branch, the pipeline performs the following steps:

1. **Code Versioning:** Git for version control.
2. **Continuous Integration:** GitHub Actions for automated workflows.
3. **Build Management:** setuptools for streamlined project builds.
4. **Testing:** pytest for unit testing.
5. **Containerization:** Docker to package the app as image (_defined below!_) for deployment.

<img src="https://raw.githubusercontent.com/IpshitaSingh/CICD/main/imgs/cicd_checks.png" width="740">
<img src="https://raw.githubusercontent.com/IpshitaSingh/CICD/main/imgs/cicd_build.png" width="740">
<img src="https://raw.githubusercontent.com/IpshitaSingh/CICD/main/imgs/cicd_test.png" width="740">

## Tests
Unit tests are implemented using pytest in [tests.py](https://github.com/IpshitaSingh/CICD/blob/main/tests.py). The **CI/CD pipeline** runs these tests to ensure the proper functioning of the app.
### First Test: Basic Functionality
This test checks the core functionality of the app. It confirms that the home page returns a 200 status code and contains the expected message.

### Second Test: Handling Non-Existent Pages
It ensures that the app handles invalid routes properly by verifying that it returns a 404 status code when a request is made to a non-existent page. 

### Third Test: Handling Other Routes
This test ensures that the app appropriately responds to requests made to different routes. It verifies that it is able to handle routes other than the root.

## Docker
The app is containerized using Docker. The Dockerfile specifies the necessary steps to build the Docker image. An *image* is a self-contained package that holds all the necessary components for running an app. The image is automatically built and pushed to DockerHub as part of the CI/CD pipeline and is ready for deployment.

Note: A Docker account is needed for this step (Username and an Access Token).

To run the app in a Docker container:

Step 1:
```
docker pull ipshitadockerhub/ipshitadockerhub-image
```
Step 2:
```
docker run ipshitadockerhub/ipshitadockerhub-image
```
The app can then be accessed via the localhost website.
