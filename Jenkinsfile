def icons = [":unicorn_face:", ":beer:", ":bee:", ":man_dancing:", ":partly_sunny:", ":ghost:", ":dancer:", ":scream_cat:", ":star:", ":stars:"]
def randomIndex = (new Random()).nextInt(icons.size())

pipeline {
  agent {
    docker {
        image 'cm9542/jenkinscron:0.1.0'
        args '-u root:sudo'
        }
  }
  triggers {
    cron('0 1 * * 0,3')
  }
  environment {
    AWS_IAM_ACCESS_KEY_ID      = credentials('AWS_IAM_ACCESS_KEY_ID')
    AWS_IAM_SECRET_ACCESS_KEY  = credentials('AWS_IAM_SECRET_ACCESS_KEY')
    AWS_S3_STORAGE_BUCKET_NAME = credentials('AWS_S3_STORAGE_BUCKET_NAME')
    AWS_S3_BUCKET_URL          = credentials('AWS_S3_BUCKET_URL')
    DATABASES                  = credentials('DATABASES')
  }
  stages {
    stage('Start') {
      steps {
        slackSend color: '#00FF00', message: ":seonkins:\n<!channel>\n*<CRONJOB STARTED>*\n<${env.RUN_DISPLAY_URL}|${env.JOB_NAME}#${env.BUILD_NUMBER}> ${icons[randomIndex]}"
      }
    }
    stage('DELETE S3 images unused') {
      steps {
        sh 'echo "dwen is handsome"'
        sh """
        echo 'AWS_IAM_ACCESS_KEY_ID       = "${env.AWS_IAM_ACCESS_KEY_ID}"' >> my_settings.py
        echo 'AWS_IAM_SECRET_ACCESS_KEY   = "${env.AWS_IAM_SECRET_ACCESS_KEY}"' >> my_settings.py
        echo 'AWS_S3_STORAGE_BUCKET_NAME  = "${env.AWS_S3_STORAGE_BUCKET_NAME}"' >> my_settings.py
        echo 'AWS_S3_BUCKET_URL           = "${env.AWS_S3_BUCKET_URL}"' >> my_settings.py
        echo 'DATABASES                   = "${env.DATABASES}"' >> my_settings.py
        """
        sh 'sudo pip install -r requirements.txt --user'
        sh 'python3 commandline.py'
      }
    }
  }
  post {
    always {
      cleanWs()
    }
    success {
      slackSend color: '#00FF00', message: "<!channel>\n*<CRONJOB SUCCEED>*\n<${env.RUN_DISPLAY_URL}|${env.JOB_NAME}#${env.BUILD_NUMBER}> ${icons[randomIndex]}"
    }
    failure {
      slackSend color: '#FF0000', message: "<!channel>\n*<CRONJOB FAILED>*\n~<${env.RUN_DISPLAY_URL}|${env.JOB_NAME}#${env.BUILD_NUMBER}>~\nPlease check <${env.RUN_DISPLAY_URL}|Console log> ${icons[randomIndex]}"
    }
  }
}

