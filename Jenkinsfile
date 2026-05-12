pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Vishwajeetsinghh01/To-Do.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t to-do-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 to-do-app || true'
            }
        }
    }
}