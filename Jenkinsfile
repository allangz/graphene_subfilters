pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'cd mock_site'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test'){
            steps{
                sh 'pytest --cov-config=.coveragerc --cov=.'
            }
        }
    }
}