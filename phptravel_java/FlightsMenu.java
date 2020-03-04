import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class FlightsMenu{
    private ChromeDriver new_session;

    protected String from_text = "FROM";
    protected String to_text = "TO";
    protected String depart_text = "DEPART";
    protected String adults_text = "ADULTS";
    protected String child_text = "CHILD";
    protected String infant_text = "INFANT";
    protected String round_trip_text = "ROUND TRIP";
    protected String one_way_text = "ONE WAY";
    protected String economy_text = "Economy";

    FlightsMenu (ChromeDriver session) {
        new_session = session;
    }

    WebElement flights_button(){
        WebElement element = null;
            try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[2]/a");
        }
            catch (Exception ignored){}
            return element;
    }
    WebElement from_inactive(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("//div[@id='s2id_location_from']//span[@class='select2-chosen']");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement to_inactive(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("//div[@id='s2id_location_to']//span[@class='select2-chosen']");
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
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[4]/button");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement add_adults(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[1]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[1]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement remove_adults(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[1]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[2]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement add_child(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[2]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[1]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement remove_child(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[2]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[2]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement add_infant(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[3]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[1]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement remove_infant(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[3]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[2]");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement class_selector(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div//form[@role='search']/div/div[1]/div[2]/div/div/a/div");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement from_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]/div/div[1]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement to_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]/div/div[2]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement depart_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[2]/div/div/div[1]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement adults_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[1]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement child_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[2]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement infant_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[3]/div/label");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement round_trip_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("//div[@id='flights']//form[@role='search']/div/div[1]/div[1]/div[2]/label[@class='custom-control-label']");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement one_way_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']//form[@role='search']/div/div[1]/div[1]/div[1]/label[@class='custom-control-label']");
        }
        catch (Exception ignored){}
        return element;
    }
    WebElement economy_label(){
        WebElement element = null;
        try {
            element = new_session.findElementByXPath("/html//div[@id='flights']/div//form[@role='search']/div/div[1]/div[2]/div/div//span[.='Economy']");
        }
        catch (Exception ignored){}
        return element;
    }
}
