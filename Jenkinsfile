pipeline {
    agent any

    stages {
        stage('Checkout from Git') {
            steps {
                git branch: 'master', url: 'https://github.com/anjurusatheesh/sathish-pdf-scanner-extractor.git'
            }
        }

        stage('Deploy to Local Container') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Executing Shell Script On Server') {
            steps {
                script {
                    sshagent(['EC2']) {
                        sh '''
                           ssh -t -t ubuntu@13.127.65.217 -o StrictHostKeyChecking=no << EOF
                            cd /home/ubuntu/sathish-pdf-scanner-extractor
                            docker-compose up -d 
                            logout
                            EOF
                        '''
                    }
                }
            }
        }
    }
}
