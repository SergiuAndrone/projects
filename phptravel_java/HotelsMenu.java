import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class HotelsMenu{
    private ChromeDriver new_session;

    protected String destination_text = "DESTINATION";
    protected String checkin_text = "CHECK IN";
    protected String checkout_text = "CHECK OUT";
    protected String adults_text = "ADULTS (12-75)";
    protected String child_text = "CHILD (2-12)";

    HotelsMenu (ChromeDriver session) {
        new_session = session;
    }

    WebElement hotels_button(){
        WebElement element = null;
        try {
             element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[1]/a");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement destination_field_inactive(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='hotels']/div//form[@role='search']//div[@class='form-icon-left typeahead__container']/div/a[@href='javascript:void(0)']/span[@class='select2-chosen']");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement enter_text(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("//div[@id='select2-drop']//input[@type='text']");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement search_button(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='hotels']/div//form[@role='search']//button[@type='submit']");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement add_adults(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/span/button[1]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement remove_adults(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/span/button[2]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement add_child(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[1]");
        }
        catch (Exception ignored){}
        return element;
    }    WebElement remove_child(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[2]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement destination_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[1]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement checkin_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[1]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement checkout_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[2]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement adults_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement child_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
}
