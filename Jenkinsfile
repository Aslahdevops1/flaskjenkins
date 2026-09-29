pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '''
                    echo Checking Python...
                    "C:\\Users\\shaheem\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" --version

                    echo Creating virtual environment...
                    "C:\\Users\\shaheem\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv

                    echo Upgrading pip...
                    venv\\Scripts\\python.exe -m pip install --upgrade pip

                    echo Installing requirements...
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    echo Running tests...
                    venv\\Scripts\\python.exe -m pytest
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                    echo Build stage started...
                    echo Flask application build completed successfully.
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs above.'
        }
    }
}