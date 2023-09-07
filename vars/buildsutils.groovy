
class buildsutils {

    def getBuild() {
        currentBuild
    }
}
// 在其他地方使用
def build = getBuild()
println( "Build Number: ${build.number}" )
