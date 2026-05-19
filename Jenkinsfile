pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Setting up Python Virtual Environment on Windows...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Application Tests...'
                bat '''
                    call venv\\Scripts\\activate
                    pytest test_app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application (Running Flask App in Background)...'
                bat '''
                    call venv\\Scripts\\activate
                    start /B python app.py > flask.log 2>&1
                '''
                echo 'Application is live!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
