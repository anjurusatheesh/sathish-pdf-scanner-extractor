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
                            docker-compose down
                            logout
                            EOF
                        '''
                    }
                }
            }
        }
    }
    post {
    always {
        retry(3) { // Retry up to 3 times
            emailext attachLog: true,
                subject: "'${currentBuild.result}'",
                body: "Project: ${env.JOB_NAME}<br/>" +
                      "Build Number: ${env.BUILD_NUMBER}<br/>" +
                      "URL: ${env.BUILD_URL}<br/>",
                to: 'anjurusatheesh56@gmail.com'
            }    
        }
    }
}    
