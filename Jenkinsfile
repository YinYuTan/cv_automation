pipeline{
    agent any

    stages{
        stage('Checkout'){
            steps{
                checkout scm
            }
        }
        stage('Checking Python Version') {
            steps {
                script {
                    // echo "Checking Python version..."
                    bat 'python --version'
                }
            }
        }
        stage('Installing Virtual Environment'){
            steps{
                script{
                    bat "python -m venv venv"   // Create venv
                }
            }
        }
        stage('Install Dependencies'){
            steps{
                script{
                    bat """
                        call venv\\Scripts\\activate
                        python -m pip install --upgrade pip
                        pip install -r ./requirements.txt
                        pip install pillow
                        pip install --upgrade robotframework-seleniumlibrary
                    """
                }
            }
        }
        stage('Check Installed Dependencies'){
            steps{
                script{
                    bat """
                        call venv\\Scripts\\activate
                        pip list
                    """
                }
            }
        }
        // stage('Download Model') {
        //     steps {
        //         bat '''
        //             if not exist models mkdir models
        //             if not exist models\\multiclass_img2_model_v11.h5 (
        //                 echo Model not found. Downloading...
        //                 curl -o models\\multiclass_img2_model_v11.h5 https://jenkins-models-test.s3.ap-southeast-1.amazonaws.com/multiclass_img2_model_v11.h5
        //             ) else (
        //                 echo Model already exists. Skipping download.
        //             )
        //         '''
        //     }
        // }
        stage('Print Working Directory') {
            steps {
                bat 'cd'
            }
        }
        // stage('Cleanup Pictures') {
        //     steps {
        //         bat 'del /Q Robot\\pictures\\*.jpg'
        //     }
        // }
        stage('Cleanup Videos') {
            steps {
                bat 'del /Q Robot_vid\\video\\*.mp4'
            }
        }
        stage('Run Robot'){
            steps{
                script{
                    bat """
                        call venv\\Scripts\\activate
                        robot --outputdir results Robot_vid/prediction.robot
                    """
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'results/**', allowEmptyArchive: true

            step([$class: 'RobotPublisher',
                outputPath: 'results',
                outputFileName: 'output.xml',
                reportFileName: 'report.html',
                logFileName: 'log.html'
            ])
        }
    }
}