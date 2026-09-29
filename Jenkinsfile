
pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat '''
                    @echo off
                    python --version
                    if errorlevel 1 exit /b 1

                    python -m venv venv
                    if errorlevel 1 exit /b 1

                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    if errorlevel 1 exit /b 1

                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m pytest
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m compileall .
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask CI/CD pipeline successful!'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs above.'
        }
    }
}