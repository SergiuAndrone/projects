import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

public class Tests {
    ChromeDriver driver = new ChromeDriver();
    Logger logger = new Logger();

    MainPage mainPage = new MainPage(driver);
    HotelsMenu hotels = new HotelsMenu(driver);
    FlightsMenu flights = new FlightsMenu(driver);
    ToursMenu tours = new ToursMenu(driver);
    CarsMenu cars = new CarsMenu(driver);
    VisaMenu visa = new VisaMenu(driver);

    boolean is_valid = false;

    public static void main(String[] args) {
        Tests new_test = new Tests();

        new_test.test_00();
        if (new_test.is_valid) {
            new_test.test_01();
            new_test.test_02();
            new_test.test_03();
            new_test.test_04();
            new_test.test_05();
        }
        new_test.close_session();
    }

    private void test_00() {
        logger.create_result_file();
        driver.get("https://www.phptravels.net/");
        driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        driver.manage().window().fullscreen();
        sleeptime(5000);

        // open the main page, check its title and accept cookies
        if (driver.getTitle().equals(MainPage.page_title)) {
            this.is_valid = true;
            try {
                mainPage.accept_cookies().click();
                logger.log_data("Cookies accepted  >>  PASS");
                sleeptime(2000);
            } catch (Exception ex) {
                logger.log_data("Accept cookies  >>  FAIL  >>  Error: " + ex);
            }
            end_test();
        }
    }

    private void test_01() {
        this.logger.log_data("TEST 01 >> Checking if the following buttons exists, are clickable and become active: \n");

        ArrayList<WebElement> buttons = new ArrayList<>(Arrays.asList(flights.flights_button(), tours.tours_button(),
                cars.cars_button(), visa.visa_button(), hotels.hotels_button(), mainPage.invalid_dummy_button()));
        ArrayList<String> buttons_name = new ArrayList<>(Arrays.asList("Flights", "Tours", "Cars", "Visa", "Hotels", "Invalid dummy button"));

        for (int i = 0; i < buttons.size(); i++) {
            try {
                buttons.get(i).click();
                logger.log_data(buttons_name.get(i) + " button  >>  PASS");
                sleeptime(2000);
            } catch (Exception ex) {
                logger.log_data(buttons_name.get(i) + " button  >>  FAIL  >>  Error: " + ex);
            }
        }
        end_test();
    }

    private void test_02() {
        this.logger.log_data("TEST 02 >> checking the labels in: Hotels\n");

        ArrayList<WebElement> elements_labels = new ArrayList<>(Arrays.asList(hotels.destination_label(),
                hotels.checkin_label(), hotels.checkout_label(), hotels.adults_label(), hotels.child_label()));
        ArrayList<String> elements_text = new ArrayList<>(Arrays.asList(hotels.destination_text, hotels.checkin_text,
                hotels.checkout_text, hotels.adults_text, hotels.child_text));

        for (int i = 0; i < elements_labels.size(); i++) {
            try {
                String label = elements_labels.get(i).getText();
                if (label.equals(elements_text.get(i))) {
                    this.logger.log_data(elements_text.get(i) + "  >>  PASS");
                } else {
                    this.logger.log_data(elements_text.get(i) + "  >>  FAIL  >>  Incorrect label: " + label);
                }
            } catch (Exception ex) {
                this.logger.log_data(elements_text.get(i) + "  >>  FAIL  >>  Error: " + ex);
            }
        }
        end_test();
    }

    private void test_03(){
        this.logger.log_data("TEST 03 >> checking the labels in: Flights\n");

        // navigate to the Flights menu
        try {
            flights.flights_button().click();
            sleeptime(2000);
        } catch (Exception ex) {
            logger.log_data("Exiting test... the Flights menu didn't load >>  CRITICAL  >>  Error: " + ex);
            return;
        }

        // check the labels and their names
        ArrayList<WebElement> elements_labels = new ArrayList<>(Arrays.asList(flights.from_label(), flights.to_label(),
                flights.depart_label(), flights.adults_label(), flights.child_label(), flights.infant_label(),
                flights.round_trip_label(), flights.one_way_label(), flights.economy_label()));
        ArrayList<String> elements_text = new ArrayList<>(Arrays.asList(flights.from_text, flights.to_text,
                flights.depart_text, flights.adults_text, flights.child_text, flights.infant_text,
                flights.round_trip_text, flights.one_way_text, flights.economy_text));

        for (int i=0; i<elements_labels.size(); i++){
            try {
                String label = elements_labels.get(i).getText();
                if (label.equals(elements_text.get(i))){
                    this.logger.log_data(elements_text.get(i) + "  >>  PASS");
                }
                else {
                    this.logger.log_data(elements_text.get(i) + "  >>  FAIL  >>  Incorrect label: " + label);
                }
            }
            catch (Exception ex){
                this.logger.log_data(elements_text.get(i) + "  >>  FAIL  >>  Error: " + ex);
            }
        }
        end_test();
    }

    private void test_04(){
        this.logger.log_data("TEST 04 >> checking the interactive elements in: Hotels\n");

        // navigate to the Hotels menu
        try {
            hotels.hotels_button().click();
            sleeptime(2000);
        } catch (Exception ex) {
            logger.log_data("Exiting test... the Hotels menu didn't load >>  CRITICAL  >>  Error: " + ex);
            return;
        }

        // select the Destination field
        boolean is_valid = false;
        try {
            hotels.destination_field_inactive().click();
            is_valid = true;
        }
        catch (Exception ex){
            this.logger.log_data("Click on the DESTINATION field  >>  FAIL  >>  Error: " + ex);
        }

        // if the Destination field has been selected, try to fill it
        if (is_valid){
            try {
            hotels.enter_text().sendKeys("Berlin");
            sleeptime(2000);
            hotels.enter_text().sendKeys(Keys.TAB);
            sleeptime(2000);
            this.logger.log_data("Fill the DESTINATION field  >>  PASS");
            }
            catch (Exception ex){
                this.logger.log_data("Fill the DESTINATION field  >>  FAIL  >>  Error: " + ex);
            }
        }

        // click on the other interactive elements in the menu
        ArrayList<WebElement> elements = new ArrayList<>(Arrays.asList(hotels.add_adults(), hotels.remove_adults(), hotels.add_child(),
                                                                       hotels.remove_child(), hotels.search_button()));
        ArrayList<String> elements_names = new ArrayList<>(Arrays.asList("Add adult (+)", "Remove adult (-)", "Add child (+)",
                                                                         "Remove child (-)", "Search button"));
        for (int i=0; i<elements.size(); i++ ){
            try {
                elements.get(i).click();
                this.logger.log_data(elements_names.get(i) + " element  >>  PASS");
            }
            catch (Exception ex){
                this.logger.log_data(elements_names.get(i) + " element  >>  FAIL  >>  Error: " + ex);
            }
            sleeptime(2000);
        }

        // validate that the search has been performed by searching for the "SEARCH" button (part of "SEARCH RESULT" from the result screen)
        if (mainPage.filter_search().getText().contains(mainPage.filter_search_text)) {
            this.logger.log_data("'FILTER SEARCH' button  >>  PASS");
        }
        else {
            this.logger.log_data("'FILTER SEARCH' button  >>  FAIL");
        }
        end_test();
    }

    private void test_05(){
        this.logger.log_data("TEST 05 >> checking the interactive elements in: Flights\n");

        // navigate to the Flights menu
        try {
            flights.flights_button().click();
            sleeptime(2000);
        } catch (Exception ex) {
            logger.log_data("Exiting test... the Flights menu didn't load >>  CRITICAL  >>  Error: " + ex);
            return;
        }

        // select the FROM field
        boolean is_valid = false;
        try {
            flights.from_inactive().click();
            is_valid = true;
        }
        catch (Exception ex){
            this.logger.log_data("Click on the FROM field  >>  FAIL  >>  Error: " + ex);
        }
        if (is_valid){
            try {
                flights.enter_text().sendKeys("Bucharest");
                sleeptime(2000);
                flights.enter_text().sendKeys(Keys.TAB);
                sleeptime(2000);
                this.logger.log_data("Fill the FROM field  >>  PASS");
            }
            catch (Exception ex){
                this.logger.log_data("Fill the FROM field  >>  FAIL  >>  Error: " + ex);
            }
        }

        // select the TO field
        is_valid = false;
        try {
            flights.to_inactive().click();
            is_valid = true;
        }
        catch (Exception ex){
            this.logger.log_data("Click on the TO field  >>  FAIL  >>  Error: " + ex);
        }
        if (is_valid){
            try {
                flights.enter_text().sendKeys("Athens");
                sleeptime(2000);
                flights.enter_text().sendKeys(Keys.TAB);
                sleeptime(2000);
                this.logger.log_data("Fill the TO field  >>  PASS");
            }
            catch (Exception ex){
                this.logger.log_data("Fill the TO field  >>  FAIL  >>  Error: " + ex);
            }
        }

        // interact with the rest of the elements
        ArrayList<WebElement> elements = new ArrayList<>(Arrays.asList(flights.add_adults(), flights.remove_adults(), flights.add_child(), flights.remove_child(),
                flights.add_infant(), flights.remove_infant(), flights.round_trip_label(), flights.one_way_label(), flights.class_selector(), flights.search_button()));
        ArrayList<String> elements_names = new ArrayList<>(Arrays.asList("Add adult (+)", "Remove adult (-)", "Add child (+)", "Remove child (-)", "Add infant (+)",
                "Remove infant (-)", "Round trip", "One way", "Class selector", "Search button"));

        for (int i=0; i<elements.size(); i++){
            try {
                elements.get(i).click();
                sleeptime(2000);
                this.logger.log_data(elements_names.get(i) + " button  >>  PASS");
                if (elements_names.get(i).equals("Class selector")){
                    elements.get(i).click();
                    sleeptime(2000);
                }
            }
            catch (Exception ex){
                this.logger.log_data(elements_names.get(i) + " button  >>  FAIL  >>  Error: " + ex);
            }
        }

        // validate that the search has been performed by searching for the "SEARCH" button (part of "SEARCH RESULT" from the result screen)
        if (mainPage.filter_search().getText().contains(mainPage.filter_search_text)){
            this.logger.log_data("'FILTER SEARCH' button  >>  PASS");
        }
        else {
            this.logger.log_data("'FILTER SEARCH' button  >>  FAIL");
        }
        end_test();
    }

    private static void sleeptime ( int amount){
        try {
            Thread.sleep(amount);
        } catch (Exception e) {
            System.out.println("exception:" + e);}
    }

    private void end_test(){
        try {
            mainPage.home_button().click();
            this.logger.log_data("Returning to Main Page ('HOME' button)  >>  PASS");
        }
        catch (Exception ex){
            this.logger.log_data("Returning to Main Page ('HOME' button)  >>  FAIL  >>  Error: " + ex);
        }
        sleeptime(1000);
        this.logger.log_data("\n" + "*".repeat(50) + "\n");
    }

    private void close_session () {
        driver.close();
        this.logger.close_result_file();
    }
}

