import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class CarsMenu{
    private ChromeDriver new_session;

    CarsMenu (ChromeDriver session) {
        new_session = session;
    }

    WebElement cars_button(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[4]/a");
        }
        catch (Exception ex) {
            System.out.println("Failed to get 'Cars' button. Error: " + ex);
        }
        return element;
    }
}
