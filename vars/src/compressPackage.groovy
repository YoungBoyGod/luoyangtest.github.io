def call(package_path, current_dir) {
    node {
        dir(current_dir) {
            // 压缩指定目录为 tar.gz 文件
            sh "tar -zcvf ${package_path}.tar.gz ${package_path}"
        }
    }
}


//@Library('my-shared-library') _
//import my.shared.library.compressPackage
//
//pipeline {
//    agent any
//    parameters {
//        string(name: 'PACKAGE_PATH', defaultValue: '', description: 'Specify the package path')
//        string(name: 'CURRENT_DIR', defaultValue: '', description: 'Specify the current directory')
//        // 其他参数...
//    }
//    stages {
//        stage('Compress Package') {
//            steps {
//                script {
//                    def package_path = params.PACKAGE_PATH
//                    def current_dir = params.CURRENT_DIR
//
//                    // 调用脚本中的函数来执行压缩操作
//                    compressPackage(package_path, current_dir)
//                }
//            }
//        }
//        // 其他阶段...
//    }



pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // 匹配多个 Tar 文件并归档
                archiveArtifacts artifacts: '*.tar*', onlyIfSuccessful: true, allowEmptyArchive: true
            }
        }
    }
}
