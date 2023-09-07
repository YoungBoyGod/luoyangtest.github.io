class CommonUtil {

    static def createDirectory(directoryPath) {
        if (!new File(directoryPath).exists()) {
            new File(directoryPath).mkdirs()
        }
    }

    static def deleteDirectory(directoryPath) {
        def file = new File(directoryPath)
        if (file.exists()) {
            def cmd = "rm -rf ${directoryPath}"
            def proc = cmd.execute()
            proc.waitFor()
        }
    }

}
