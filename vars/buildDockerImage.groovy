def call(package_path, docker_image_path) {
    node {
        // 复制 Dockerfile 到指定目录
        sh "cp docker/Dockerfile ${package_path}/"
        dir("${package_path}") {
            // 编译 Docker 镜像并保存为 tar 文件
            sh "docker build -t ${docker_image_path} -f Dockerfile ."
            sh "docker save -o ../${docker_image_path}.tar ${docker_image_path}"
            sh "docker rmi ${docker_image_path}"
        }
    }
}


//@Library('my-shared-library') _
//import my.shared.library.buildDockerImage
//
//pipeline {
//    agent any
//    parameters {
//        string(name: 'PACKAGE_PATH', defaultValue: '', description: 'Specify the package path')
//        string(name: 'DOCKER_IMAGE_PATH', defaultValue: '', description: 'Specify the Docker image path and tag')
//        // 其他参数...
//    }
//    stages {
//        stage('Build Docker Image') {
//            steps {
//                script {
//                    def package_path = params.PACKAGE_PATH
//                    def docker_image_path = params.DOCKER_IMAGE_PATH
//
//                    // 调用脚本中的函数来执行 Docker 相关操作
//                    buildDockerImage(package_path, docker_image_path)
//                }
//            }
//        }
//        // 其他阶段...
//    }