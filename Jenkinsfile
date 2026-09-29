
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Flask project from GitHub'
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '''
                    "C:\\Users\\moham\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version
                '''
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                    "C:\\Users\\moham\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m pip install --upgrade pip

                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m pytest -v
                '''
            }
        }

        stage('Build Flask Application') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m py_compile app.py
                '''
            }
        }

    }

    post {
        success {
            echo 'SUCCESS: Flask application built and tests completed!'
        }

        failure {
            echo 'FAILURE: Flask CI pipeline failed. Check the console output.'
        }

        always {
            echo 'Jenkins pipeline execution completed.'
        }
    }
}