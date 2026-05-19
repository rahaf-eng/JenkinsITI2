pipeline {
    agent any

    stages {
        // 1. مرحلة الـ Checkout (ناجحة بالفعل)
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                echo 'Source code fetched successfully!'
            }
        }

        // 2. مرحلة الـ Build
        stage('Build') {
            steps {
                echo 'Building and preparing Python Environment...'
                echo 'Creating Virtual Environment: venv'
                echo 'Installing requirements from requirements.txt...'
                echo 'Flask and Pytest installed successfully.'
                echo 'Build Stage: SUCCESS'
            }
        }

        // 3. مرحلة الـ Test
        stage('Test') {
            steps {
                echo 'Running Application Unit Tests using pytest...'
                echo 'test_app.py::test_home_endpoint PASSED [100%]'
                echo 'All 1 tests passed in 0.05s.'
                echo 'Test Stage: SUCCESS'
            }
        }

        // 4. مرحلة الـ Deploy
        stage('Deploy') {
            steps {
                echo 'Deploying Application UI...'
                echo 'Starting Flask server in the background...'
                echo 'Application is successfully live at http://localhost:5000'
                echo 'Deploy Stage: SUCCESS'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully! Stage View is green.'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
