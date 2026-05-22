pipeline {
    agent any

    environment {
        APP_NAME    = 'calculator'
        VERSION     = "1.0.${BUILD_NUMBER}"
        DIST_DIR    = 'dist'
        VENV_DIR    = '.venv'
    }

    stages {
        stage('Build') {
            steps {
                echo "Building ${APP_NAME} v${VERSION}"
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install pytest pytest-cov
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests with coverage'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python3 -m pytest test_calculator.py -v \
                        --cov=calculator \
                        --cov-report=xml:coverage.xml \
                        --cov-report=term-missing \
                        --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                    recordCoverage(
                        tools: [[parser: 'COBERTURA', pattern: 'coverage.xml']]
                    )
                }
            }
        }

        stage('Package') {
            steps {
                echo "Packaging ${APP_NAME} v${VERSION}"
                sh '''
                    mkdir -p ${DIST_DIR}
                    tar -czf ${DIST_DIR}/${APP_NAME}-${VERSION}.tar.gz \
                        calculator.py \
                        --transform "s|^|${APP_NAME}-${VERSION}/|"
                '''
                archiveArtifacts artifacts: "${DIST_DIR}/${APP_NAME}-${VERSION}.tar.gz",
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded — artifact: ${DIST_DIR}/${APP_NAME}-${VERSION}.tar.gz"
        }
        failure {
            echo 'Pipeline failed. Check the logs above for details.'
        }
        cleanup {
            sh 'rm -rf ${VENV_DIR}'
        }
    }
}
