pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'python -m venv venv'
                sh '. venv/bin/activate && python -m pip install -r mock_site/requirements.txt'
                sh '. venv/bin/activate && pip list'
            }
        }
        stage('Test'){
            steps{
                dir('mock_site') {
                    sh '. ../venv/bin/activate && pytest --cov-config=.coveragerc --cov=.'
                }
            }
        }
    }
}