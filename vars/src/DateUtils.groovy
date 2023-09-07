import java.util.Calendar
import java.text.DecimalFormat
class DateUtil {

    static getNowFormatted() {
        def year = new Date().format("yy")
        def calendar = Calendar.instance
        def week = calendar.get(Calendar.WEEK_OF_YEAR)
        def dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK)-1

        def df = new DecimalFormat("00")
        def formattedWeek = df.format(week)

        return "W${year}.${formattedWeek}.${dayOfWeek}"
    }
}

def xx=new DateUtil()
println(xx.getNowFormatted())