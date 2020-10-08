pipeline {
    agent any

    stages {
        stage('Create File With Name') {
            steps {
                script {
                 status = sh(script: 'NAME=${NAME} ./bash_scripts/fifthAssignment.sh', returnStatus: true)
                 echo "status is ${status}"
                }
            }
        }

          stage('Run Selenium tests') {
            steps {
                script {
                 echo "sourcing venv"
                 source devopscourse/bin/activate
                 echo "running all selenium tests from fourth assignment"
                 status = sh(script: 'python3 fourth_assignment.sh', returnStatus: true)
                 echo "status is ${status}"
                }
            }
        }
    }
}
