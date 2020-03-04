import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class ToursMenu{
    private ChromeDriver new_session;

    ToursMenu (ChromeDriver session) {
        new_session = session;
    }

    WebElement tours_button(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[3]/a");
        }
        catch (Exception ex) {
            System.out.println("Failed to get 'Tours' button. Error: " + ex);
        }
        return element;
    }
}
