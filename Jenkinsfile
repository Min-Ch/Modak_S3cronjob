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
}

