import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class MainPage {
    private ChromeDriver new_session;
    MainPage(ChromeDriver session){
        new_session = session;
    }

    // main page specific elements
    static String page_title = "PHPTRAVELS | Travel Technology Partner";
    protected String filter_search_text = "SEARCH";
    static String invalid_dummy_button = "invalid_test_button";

    WebElement accept_cookies(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("//div[@id='cookyGotItBtnBox']//button[@role='button']");
        }
        catch (Exception ex) {
            System.out.println("Failed to get 'Got it' button. Error: " + ex);
        }
        return element;
    }
    WebElement home_button(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("//div[@id='mobileMenuMain']/nav//a[@title='home']");
        }
        catch (Exception ex) {
            System.out.println("Failed to get 'HOME' button. Error: " + ex);
        }
        return element;
    }
    WebElement invalid_dummy_button(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("//div[@id='mob/a[@title='invalid']");
        }
        catch (Exception ex) {
            System.out.println("Failed to get 'Invalid dummy' button. Error: " + ex);
        }
        return element;
    }
    WebElement filter_search(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//button[@id='searchform']");
        }
        catch (Exception ex) {
            System.out.println("Failed to get 'Filter search' button. Error: " + ex);
        }
        return element;
    }
}

