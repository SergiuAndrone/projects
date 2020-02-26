from selenium import webdriver
import getpass
import time
import sys


class Tests:
    def __init__(self):
        self.logger = Logger()
        self.session = PhpTravel()
        self.page_loaded = True
        self.page_objects = PageObjects()

    def return_home(self):
        main_page = self.session.find_element_by_xpath(xpath=self.page_objects.main_page)
        if main_page:
            main_page.click()

    def test00(self):
        time_loaded = self.session.open_page()
        time.sleep(5)

        if self.page_objects.page_title in self.session.driver.title:
            self.logger.log_data(f"Page LOADED in {time_loaded} seconds \n\n")
        else:
            self.logger.log_data(f"Page FAILED to load. Exiting tests...\n")
            self.page_loaded = False

    def test01(self):
        self.logger.log_data("TEST 01 >> Checking if the following buttons exists, are clickable and become active: Flights, Tours, Cars, Visa, Hotels\n")

        buttons = {"Flights": self.page_objects.flights_menu.flights_button, "Tours": self.page_objects.tours_menu.tours_button, "Cars": self.page_objects.cars_menu.cars_button,
                   "Visa": self.page_objects.visa_menu.visa_button, "Hotels": self.page_objects.hotels_menu.hotels_button}

        for key in buttons.keys():
            result = self.session.find_element_by_xpath(xpath=buttons[key])
            if result:
                result.click()
                time.sleep(1)
                if result.is_enabled():
                    self.logger.log_data(f"{result.text}  >>  PASS")
                else:
                    self.logger.log_data(f"{result.text}  >>  FAIL: button present but inactive")
            else:
                self.logger.log_data(f"{key}  >>  FAIL: button not present")
        self.logger.log_data("\n\n")
        self.return_home()

    def test02(self):
        self.logger.log_data("TEST 02 >> checking the labels in: Hotels\n")

        expected_labels = {self.page_objects.hotels_menu.destination_text: self.page_objects.hotels_menu.destination_label,
                           self.page_objects.hotels_menu.checkin_text: self.page_objects.hotels_menu.checkin_label,
                           self.page_objects.hotels_menu.checkout_text: self.page_objects.hotels_menu.checkout_label,
                           self.page_objects.hotels_menu.adults_text: self.page_objects.hotels_menu.adults_label,
                           self.page_objects.hotels_menu.child_text: self.page_objects.hotels_menu.child_label}
        found_labels = []

        hotels = self.session.find_element_by_xpath(xpath=self.page_objects.hotels_menu.hotels_button)
        if hotels:
            hotels.click()
            time.sleep(1)
            if hotels.is_enabled():
                for key in expected_labels.keys():
                    element = self.session.find_element_by_xpath(xpath=expected_labels[key])
                    if element:
                        found_labels.append(element.text)
                for label in expected_labels.keys():
                    if label in found_labels:
                        self.logger.log_data(f"{label} is present in the Hotels menu  >>  PASS")
                    else:
                        self.logger.log_data(f"{label} is not present in the Hotels menu  >>  FAIL")
            else:
                self.logger.log_data("'Hotels' menu is not active  >>  FAIL")
        else:
            self.logger.log_data("'Hotels' menu wasn't found  >>  FAIL")

        self.logger.log_data("\n\n")
        self.return_home()

    def test03(self):
        self.logger.log_data("TEST 03 >> checking the labels in: Flights\n")

        expected_labels = {self.page_objects.flights_menu.from_text: self.page_objects.flights_menu.from_label,
                           self.page_objects.flights_menu.to_text: self.page_objects.flights_menu.to_label,
                           self.page_objects.flights_menu.depart_text: self.page_objects.flights_menu.depart_label,
                           self.page_objects.flights_menu.adults_text: self.page_objects.flights_menu.adults_label,
                           self.page_objects.flights_menu.child_text: self.page_objects.flights_menu.child_label,
                           self.page_objects.flights_menu.infant_text: self.page_objects.flights_menu.infant_label}
        found_labels = []

        flights = self.session.find_element_by_xpath(xpath=self.page_objects.flights_menu.flights_button)
        if flights:
            flights.click()
            time.sleep(1)
            if flights.is_enabled():
                for key in expected_labels.keys():
                    element = self.session.find_element_by_xpath(xpath=expected_labels[key])
                    if element:
                        found_labels.append(element.text)
                for label in expected_labels.keys():
                    if label in found_labels:
                        self.logger.log_data(f"{label} is present in the Hotels menu  >>  PASS")
                    else:
                        self.logger.log_data(f"{label} is not present in the Hotels menu  >>  FAIL")
            else:
                self.logger.log_data("'Flights' menu is not active  >>  FAIL")
        else:
            self.logger.log_data("'Flights' menu wasn't found  >>  FAIL")

        self.logger.log_data("\n\n")
        self.return_home()

    def test04(self):
        field_not_selected = self.session.find_element_by_xpath(self.page_objects.hotels_menu.destination_field_inactive)
        if field_not_selected:
            field_not_selected.click()
        field_selected = self.session.find_element_by_xpath(self.page_objects.hotels_menu.destination_field_active)
        if field_selected:
            field_selected.send_keys("Berlin")
        
        search = self.session.find_element_by_xpath(xpath=self.page_objects.hotels_menu.search_button)
        if search:
            search.submit()
        time.sleep(5)
        self.return_home()

    def close_test(self):
        self.session.close_session()


class Logger:
    def __init__(self):
        self.log_location = f"/Users/{getpass.getuser()}/Desktop/test_results.txt" if sys.platform == "darwin" else "C:\\"

        self.create_log_file()

    def create_log_file(self):
        try:
            with open(self.log_location, 'w') as f:
                f.write('THE RESULTS OF THE TEST ARE: \n\n\n')
        except Exception as e:
            print(f"Results file couldn't be created. The test result won't be recoreded. Error: {e}")

    def log_data(self, text):
        with open(self.log_location, 'a') as f:
            f.write(text + '\n')


class PhpTravel:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_page_load_timeout(30)
        self.__page = "https://www.phptravels.net/"

    def get_page(self):
        pass

    def open_page(self):
        time_start = time.time()
        self.driver.get(self.__page)
        time_end = time.time()

        return time_end - time_start

    def find_element_by_id(self, element_id=None):
        element = None
        try:
            element = self.driver.find_element_by_id(id_=element_id)
        except:
            pass
        return element

    def find_element_by_class(self, cls=None):
        element = None
        try:
            element = self.driver.find_element_by_class_name(name=cls)
        except:
            pass
        return element

    def find_element_by_link(self, link_text):
        element = None
        try:
            element = self.driver.find_element_by_link_text(link_text=link_text)
        except:
            pass
        return element

    def find_element_by_xpath(self, xpath):
        element = None
        try:
            element = self.driver.find_element_by_xpath(xpath=xpath)
        except:
            pass
        return element

    def close_session(self):
        self.driver.close()


class PageObjects:
    """

    All the page elements used in tests must be retrieved from here. Can be created private and returned as @property

    """
    def __init__(self):
        self.page_title = "PHPTRAVELS"

        # xpath for main page
        self.main_page = "/html//header[@id='header-waypoint-sticky']/div[@class='header-top']//a[@href='https://www.phptravels.net/']/img[@alt='PHPTRAVELS | Travel Technology Partner']"

        self.hotels_menu = HotelsMenu()
        self.flights_menu = FlightsMenu()
        self.tours_menu = ToursMenu()
        self.cars_menu = CarsMenu()
        self.visa_menu = VisaMenu()


class VisaMenu:
    def __init__(self):
        # buttons/labels represented by xpath
        self.visa_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[5]/a"
        self.visa_submit_button = ""


class CarsMenu:
    def __init__(self):
        # buttons/labels represented by xpath
        self.cars_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[4]/a"
        self.search_button = ""


class ToursMenu:
    def __init__(self):
        # buttons/labels represented by xpath
        self.tours_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[3]/a"
        self.search_button = ""


class FlightsMenu:
    def __init__(self):
        # buttons/labels represented by xpath
        self.flights_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[2]/a"
        self.search_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[4]/button"

        # name of the labels in "Flights" submenu
        self.from_text = "FROM"
        self.to_text = "TO"
        self.depart_text = "DEPART"
        self.adults_text = "ADULTS"
        self.child_text = "CHILD"
        self.infant_text = "INFANT"

        # xpath of the labels in "Flights" submenu
        self.from_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]/div/div[1]/div/label"
        self.to_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]/div/div[2]/div/label"
        self.depart_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[2]/div/div/div[1]/div/label"
        self.adults_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[1]/div/label"
        self.child_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[2]/div/label"
        self.infant_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[3]/div/label"


class HotelsMenu:
    def __init__(self):
        # buttons/labels represented by xpath
        self.hotels_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[1]/a"
        self.search_button = "/html//div[@id='hotels']/div//form[@role='search']//button[@type='submit']"

        # name of the labels in "Hotels" submenu
        self.destination_text = "DESTINATION"
        self.checkin_text = "CHECK IN"
        self.checkout_text = "CHECK OUT"
        self.adults_text = "ADULTS (12-75)"
        self.child_text = "CHILD (2-12)"

        # xpath of the labels in "Hotels" submenu
        self.destination_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[1]/div/label"
        self.checkin_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[1]/div/label"
        self.checkout_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[2]/div/label"
        self.adults_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/label"
        self.child_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/label"

        # xpath for editable fields
        self.destination_field_inactive = "/html//div[@id='hotels']/div//form[@role='search']//div[@class='form-icon-left typeahead__container']/div/a[@href='javascript:void(0)']/span[@class='select2-chosen']"
        self.destination_field_active = "//div[@id='select2-drop']//input[@type='text']"




def main():

    tests = Tests()
    tests.test00()

    if tests.page_loaded:
        tests.test01()
        time.sleep(3)
        tests.test02()
        time.sleep(3)
        tests.test03()
        time.sleep(3)
        tests.test04()
        time.sleep(3)

    tests.close_test()


if __name__ == '__main__':
    main()
