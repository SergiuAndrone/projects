import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class VisaMenu{
    private ChromeDriver new_session;

    VisaMenu (ChromeDriver session) {
        new_session = session;
    }

    WebElement visa_button(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[5]/a");
        }
        catch (Exception ex) {
            System.out.println("Failed to get 'Visa' button. Error: " + ex);
        }
        return element;
    }
}

