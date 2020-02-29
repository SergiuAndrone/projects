from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time
import sys


class Logger:
    def __init__(self):
        self.log_location = f"/Users/{getpass.getuser()}/test_results.txt" if sys.platform == "darwin" else "C:/Users/Public/Documents/test_results.txt"
        self.create_log_file()

    def create_log_file(self):
        """
        Creates the test results file in the following location:

        Mac OS: "/Users/<user>/Desktop/test_results.txt"
        Windows: "C:/Users/Public/Documents/test_results.txt"

        Returns:
            None
        """
        try:
            with open(self.log_location, 'w') as f:
                f.write('*'*50 + '\n' + ' '*17 + 'TEST RESULTS\n' + '*'*50 + '\n\n')
        except Exception as e:
            print(f"Results file couldn't be created. The test result won't be recoreded. Error: {e}")

    def log_data(self, text=None):
        """
        Writes text in the test results file

        Args:
            text (str): the text to be written

        Returns:
             None
        """
        try:
            with open(self.log_location, 'a') as f:
                f.write(text + '\n')
        except Exception as e:
            print(f"Failed to write in file. Error: {e}")


class Helper:
    def __init__(self, session):
        self.__session = session
        self.__page = "https://www.phptravels.net/"

    def get_page(self):
        return self.__page

    def open_page(self):
        """
        Opens __page using the webdriver session received as argument

        Returns:
            The time took for the page to load
        """
        time_start = time.time()
        self.__session.get(self.__page)
        time_end = time.time()

        return time_end - time_start

    def find_element_by_id(self, element_id=None):
        """
        Find an element by id

        Returns:
             The Webpage element if found, None otherwise
        """
        element = None
        try:
            element = self.__session.find_element_by_id(id_=element_id)
        except:
            pass
        return element

    def find_element_by_class(self, cls=None):
        """
        Find an element by class

        Returns:
             The Webpage element if found, None otherwise
        """
        element = None
        try:
            element = self.__session.find_element_by_class_name(name=cls)
        except:
            pass
        return element

    def find_element_by_link(self, link_text):
        """
        Find an element by link

        Returns:
             The Webpage element if found, None otherwise
        """
        element = None
        try:
            element = self.__session.find_element_by_link_text(link_text=link_text)
        except:
            pass
        return element

    def find_element_by_xpath(self, xpath):
        """
        Find an element by xpath

        Returns:
             The Webpage element if found, None otherwise
        """
        element = None
        try:
            element = self.__session.find_element_by_xpath(xpath=xpath)
        except:
            pass
        return element

    def close_session(self):
        self.__session.close()


class MainPage:
    def __init__(self, session):
        self.__session = session
        self.helper = Helper(session=self.__session)
        self.page_title = "PHPTRAVELS"

        # main page specific elements
        self.__main_page = "//div[@id='mobileMenuMain']/nav//a[@title='home']"
        self.__accept_cookies = "//div[@id='cookyGotItBtnBox']//button[@role='button']"
        self.__filter_search = "/html//button[@id='searchform']"
        self.__dummy_button = "invalid_test_button"

    @property
    def main_page_reload(self):
        return self.helper.find_element_by_xpath(xpath=self.__main_page)

    @property
    def accept_cookies(self):
        return self.helper.find_element_by_xpath(xpath=self.__accept_cookies)

    @property
    def filter_search(self):
        return self.helper.find_element_by_xpath(xpath=self.__filter_search)

    @property
    def dummy_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__dummy_button)


class VisaMenu:
    def __init__(self, session):
        self.helper = Helper(session=session)

        self.__visa_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[5]/a"

    @property
    def visa_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__visa_button)


class CarsMenu:
    def __init__(self, session):
        self.helper = Helper(session=session)

        self.__cars_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[4]/a"

    @property
    def cars_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__cars_button)


class ToursMenu:
    def __init__(self, session):
        self.helper = Helper(session=session)

        self.__tours_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[3]/a"

    @property
    def tours_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__tours_button)


class FlightsMenu:
    def __init__(self, session):
        self.helper = Helper(session=session)

        self.__flights_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[2]/a"
        self.__search_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[4]/button"
        self.__add_adults = "/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[1]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[1]"
        self.__remove_adults = "/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[1]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[2]"
        self.__add_child = "/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[2]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[1]"
        self.__remove_child = "/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[2]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[2]"
        self.__add_infant = "/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[3]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[1]"
        self.__remove_infant = "/html//div[@id='flights']/div/div[@class='form-search-main-01']/form[@role='search']/div[@class='form-inner']/div[3]/div[3]/div[@class='col-inner']/div/div[3]/div[@class='form-group form-spin-group']/div[@class='form-icon-left']/div/span[@class='input-group-btn-vertical']/button[2]"
        self.__class_selector = "/html//div[@id='flights']/div//form[@role='search']/div/div[1]/div[2]/div/div/a/div"

        # name of the labels in "Flights" submenu
        self.from_text = "FROM"
        self.to_text = "TO"
        self.depart_text = "DEPART"
        self.adults_text = "ADULTS"
        self.child_text = "CHILD"
        self.infant_text = "INFANT"
        self.round_trip_text = "ROUND TRIP"
        self.one_way_text = "ONE WAY"
        self.economy_text = "Economy"
        self.business_text = "Business"
        self.first_text = "First"

        # xpath of the labels in "Flights" submenu
        self.from_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]/div/div[1]/div/label"
        self.to_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[1]/div/div[2]/div/label"
        self.depart_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[2]/div/div/div[1]/div/label"
        self.adults_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[1]/div/label"
        self.child_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[2]/div/label"
        self.infant_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/form/div/div[3]/div[3]/div/div/div[3]/div/label"
        self.round_trip_label = "//div[@id='flights']//form[@role='search']/div/div[1]/div[1]/div[2]/label[@class='custom-control-label']"
        self.one_way_label = "/html//div[@id='flights']//form[@role='search']/div/div[1]/div[1]/div[1]/label[@class='custom-control-label']"
        self.economy_label = "/html//div[@id='flights']/div//form[@role='search']/div/div[1]/div[2]/div/div//span[.='Economy']"
        self.business_label = "/html//div[@id='flights']/div//form[@role='search']/div/div[1]/div[2]/div/div//span[.='Business']"
        self.first_label = "/html//div[@id='flights']/div//form[@role='search']/div/div[1]/div[2]/div/div//span[.='First']"

        # editable fields
        self.__from_inactive = "//div[@id='s2id_location_from']//span[@class='select2-chosen']"
        self.__to_inactive = "//div[@id='s2id_location_to']//span[@class='select2-chosen']"
        self.__enter_text = "//div[@id='select2-drop']//input[@type='text']"

    @property
    def flights_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__flights_button)

    @property
    def search_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__search_button)

    @property
    def from_inactive(self):
        return self.helper.find_element_by_xpath(xpath=self.__from_inactive)

    @property
    def to_inactive(self):
        return self.helper.find_element_by_xpath(xpath=self.__to_inactive)

    @property
    def enter_text(self):
        return self.helper.find_element_by_xpath(xpath=self.__enter_text)

    @property
    def add_adults_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__add_adults)

    @property
    def remove_adults_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__remove_adults)

    @property
    def add_child_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__add_child)

    @property
    def remove_child_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__remove_child)

    @property
    def add_infant_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__add_infant)

    @property
    def remove_infant_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__remove_infant)

    @property
    def round_trip_button(self):
        return self.helper.find_element_by_xpath(xpath=self.round_trip_label)

    @property
    def one_way_button(self):
        return self.helper.find_element_by_xpath(xpath=self.one_way_label)

    @property
    def class_selector(self):
        return self.helper.find_element_by_xpath(xpath=self.__class_selector)


class HotelsMenu:
    def __init__(self, session):
        self.helper = Helper(session=session)

        self.__hotels_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[1]/a"
        self.__search_button = "/html//div[@id='hotels']/div//form[@role='search']//button[@type='submit']"
        self.__add_adults = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/span/button[1]"
        self.__remove_adults = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/div[2]/div/span/button[2]"
        self.__add_child = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[1]"
        self.__remove_child = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[2]/div/span/button[2]"

        # expected 'text' of the labels in "Hotels" menu
        self.destination_text = "DESTINATION"
        self.checkin_text = "CHECK IN"
        self.checkout_text = "CHECK OUT"
        self.adults_text = "ADULTS (12-75)"
        self.child_text = "CHILD (2-12)"

        # the labels in "Hotels" submenu
        self.destination_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[1]/div/label"
        self.checkin_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[1]/div/label"
        self.checkout_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[2]/div/label"
        self.adults_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/label"
        self.child_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/label"

        # editable fields
        self.__destination_field_inactive = "/html//div[@id='hotels']/div//form[@role='search']//div[@class='form-icon-left typeahead__container']/div/a[@href='javascript:void(0)']/span[@class='select2-chosen']"
        self.__enter_text = "//div[@id='select2-drop']//input[@type='text']"

    @property
    def hotels_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__hotels_button)

    @property
    def search_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__search_button)

    @property
    def add_adults_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__add_adults)

    @property
    def remove_adults_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__remove_adults)

    @property
    def add_child_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__add_child)

    @property
    def remove_child_button(self):
        return self.helper.find_element_by_xpath(xpath=self.__remove_child)

    @property
    def destination_field_inactive(self):
        return self.helper.find_element_by_xpath(xpath=self.__destination_field_inactive)

    @property
    def enter_text(self):
        return self.helper.find_element_by_xpath(xpath=self.__enter_text)


class Tests:
    def __init__(self):
        self.__session = webdriver.Chrome()
        self.__session.set_page_load_timeout(time_to_wait=10)
        self.__session.fullscreen_window()
        # self.__session.implicitly_wait(5)
        self.page_loaded = True

        self.logger = Logger()
        self.helper = Helper(session=self.__session)
        self.main_page = MainPage(session=self.__session)
        self.hotels_menu = HotelsMenu(session=self.__session)
        self.flights_menu = FlightsMenu(session=self.__session)
        self.tours_menu = ToursMenu(session=self.__session)
        self.cars_menu = CarsMenu(session=self.__session)
        self.visa_menu = VisaMenu(session=self.__session)

    def test_00(self):
        """
        Loads the page and accepts the cookies

        Returns:
            None
        """
        time_loaded = self.helper.open_page()
        time.sleep(5)

        if self.main_page.page_title in self.__session.title:
            self.logger.log_data(f"Page LOADED in {time_loaded} seconds \n\n")

            # accepting cookies
            try:
                self.main_page.accept_cookies.click()
            except Exception as e:
                self.logger.log_data(f"Accept cookies ('Got it' button)  >>  FAIL  >>  Error: {e}")
        else:
            self.logger.log_data(f"Page FAILED to load. Exiting tests...\n")
            self.page_loaded = False

    def test_01(self):
        """
        Searches for the 5 buttons of the Search menu and clicks on them

        Returns:
            None
        """
        self.logger.log_data("TEST 01 >> Checking if the following buttons exists, are clickable and become active: \n")

        buttons = {"Flights": self.flights_menu.flights_button,
                   "Tours": self.tours_menu.tours_button,
                   "Cars": self.cars_menu.cars_button,
                   "Visa": self.visa_menu.visa_button,
                   "Hotels": self.hotels_menu.hotels_button,
                   "Invalid dummy button": self.main_page.dummy_button}

        for key in buttons.keys():
            try:
                buttons[key].click()
                self.logger.log_data(f"'{key}' button  >>  PASS")
            except Exception as e:
                self.logger.log_data(f"'{key}' button  >>  FAIL  >>  Error: {e}")
            time.sleep(1)

        self.end_test()

    def test_02(self):
        """
        Checks if all the elements specific to the 'Hotels' menu are present and have the correct name

        Returns:
            None
        """
        self.logger.log_data("TEST 02 >> checking the labels in: Hotels\n")

        expected_labels = {self.hotels_menu.destination_text: self.hotels_menu.destination_label,
                           self.hotels_menu.checkin_text: self.hotels_menu.checkin_label,
                           self.hotels_menu.checkout_text: self.hotels_menu.checkout_label,
                           self.hotels_menu.adults_text: self.hotels_menu.adults_label,
                           self.hotels_menu.child_text: self.hotels_menu.child_label}
        found_labels = []

        try:
            self.hotels_menu.hotels_button.click
        except Exception as e:
            self.logger.log_data(f"Exiting test... the Hotels menu didn't load >>  CRITICAL  >>  Error: {e}")
            return

        for key in expected_labels.keys():
            element = self.helper.find_element_by_xpath(xpath=expected_labels[key])
            if element:
                found_labels.append(element.text)
        for label in expected_labels.keys():
            if label in found_labels:
                self.logger.log_data(f"'{label}' is present  >>  PASS")
            else:
                self.logger.log_data(f"'{label}' is not present  >>  FAIL")

        self.end_test()

    def test_03(self):
        """
        Checks if all the elements specific to the 'Flights' menu are present and have the correct name

        Returns:
            None
        """
        self.logger.log_data("TEST 03 >> checking the labels in: Flights\n")

        expected_labels = {self.flights_menu.from_text: self.flights_menu.from_label,
                           self.flights_menu.to_text: self.flights_menu.to_label,
                           self.flights_menu.depart_text: self.flights_menu.depart_label,
                           self.flights_menu.adults_text: self.flights_menu.adults_label,
                           self.flights_menu.child_text: self.flights_menu.child_label,
                           self.flights_menu.infant_text: self.flights_menu.infant_label,
                           self.flights_menu.round_trip_text: self.flights_menu.round_trip_label,
                           self.flights_menu.one_way_text: self.flights_menu.one_way_label,
                           self.flights_menu.economy_text: self.flights_menu.economy_label}
        found_labels = []

        try:
            self.flights_menu.flights_button.click()
        except Exception as e:
            self.logger.log_data(f"Exiting test... the Flights menu didn't load >>  CRITICAL  >>  Error: {e}")
            return

        for key in expected_labels.keys():
            element = self.helper.find_element_by_xpath(xpath=expected_labels[key])
            if element:
                found_labels.append(element.text)
        for label in expected_labels.keys():
            if label in found_labels:
                self.logger.log_data(f"'{label}' is present  >>  PASS")
            else:
                self.logger.log_data(f"'{label}' is not present  >>  FAIL")

        self.end_test()

    def test_04(self):
        """
        Searches the interactive elements from the Hotels menu and performs actions on them (click, submit, fill ..., depending on the element type)

        Returns:
            None
        """
        self.logger.log_data("TEST 04 >> checking the interactive elements in: Hotels\n")

        # fill in the DESTINATION field
        is_valid = True
        try:
            self.hotels_menu.destination_field_inactive.click()
        except Exception as e:
            self.logger.log_data(f"Click on the DESTINATION field  >>  FAIL  >>  Error: {e}")
            is_valid = False

        if is_valid:
            try:
                self.hotels_menu.enter_text.send_keys("Berlin")
                time.sleep(2)
                self.hotels_menu.enter_text.send_keys(Keys.TAB)
                self.logger.log_data("Fill the DESTINATION field  >>  PASS")
                time.sleep(2)
            except Exception as e:
                self.logger.log_data(f"Fill the DESTINATION field  >>  FAIL  >>  Error: {e}")

        # check the ADD (+) and REMOVE (-) buttons
        elements = {"Add adult (+)": self.hotels_menu.add_adults_button,
                    "Remove adult (-)": self.hotels_menu.remove_adults_button,
                    "Add child (+)": self.hotels_menu.add_child_button,
                    "Remove child (-)": self.hotels_menu.remove_child_button}

        for key in elements.keys():
            try:
                elements[key].click()
                self.logger.log_data(f"'{key}' element  >>  PASS")
            except Exception as e:
                self.logger.log_data(f"'{key}' element  >>  FAIL  >>  Error: {e}")
            time.sleep(1)

        # submit the data using the SEARCH button
        try:
            self.hotels_menu.search_button.submit()
            self.logger.log_data("'SEARCH' button  >>  PASS")
        except Exception as e:
            self.logger.log_data(f"'SEARCH'' button  >>  FAIL  >>  Error: {e}")
            is_valid = False

        # validate that the results page has appeared by searching the FILTER SEARCH button
        if is_valid:
            filter_search = self.main_page.filter_search
            if filter_search:
                self.logger.log_data(f"'FILTER SEARCH' button  >>  PASS")
            else:
                self.logger.log_data(f"'FILTER SEARCH' button  >>  FAIL")

        self.end_test()

    def test_05(self):
        """
        Searches the interactive elements from the Flights menu and performs actions on them (click, submit, fill ..., depending on the element type)

        Returns:
            None
        """
        self.logger.log_data("TEST 05 >> checking the interactive elements in: Flights\n")

        is_valid = True
        # navigate to the Flights menu
        try:
            self.flights_menu.flights_button.click()
        except Exception as e:
            self.logger.log_data(f"Exiting test... the Flights menu didn't load >>  CRITICAL  >>  Error: {e}")
            return

        # fill in the FROM field
        try:
            self.flights_menu.from_inactive.click()
        except Exception as e:
            self.logger.log_data(f"Click on the FROM field  >>  FAIL  >>  Error: {e}")
            is_valid = False

        if is_valid:
            try:
                self.flights_menu.enter_text.send_keys("Bucharest")
                time.sleep(2)
                self.flights_menu.enter_text.send_keys(Keys.TAB)
                self.logger.log_data("Fill the FROM field  >>  PASS")
                time.sleep(2)
            except Exception as e:
                self.logger.log_data(f"Fill the FROM field  >>  FAIL  >>  Error: {e}")

        # fill in the TO field
        is_valid = True
        try:
            self.flights_menu.to_inactive.click()
        except Exception as e:
            self.logger.log_data(f"Click on the TO field  >>  FAIL  >>  Error: {e}")
            is_valid = False

        if is_valid:
            try:
                self.flights_menu.enter_text.send_keys("Athens")
                time.sleep(2)
                self.flights_menu.enter_text.send_keys(Keys.TAB)
                self.logger.log_data("Fill the TO field  >>  PASS")
                time.sleep(2)
            except Exception as e:
                self.logger.log_data(f"Fill the TO field  >>  FAIL  >>  Error: {e}")
                is_valid = False

        # check the other interactive elements
        elements = {"Add adult (+)": self.flights_menu.add_adults_button,
                    "Remove adult (-)": self.flights_menu.remove_adults_button,
                    "Add child (+)": self.flights_menu.add_child_button,
                    "Remove child (-)": self.flights_menu.remove_child_button,
                    "Add infant (+)": self.flights_menu.add_infant_button,
                    "Remove infant (-)": self.flights_menu.remove_infant_button,
                    "Round trip": self.flights_menu.round_trip_button,
                    "One way": self.flights_menu.one_way_button,
                    "Class selector": self.flights_menu.class_selector}

        for key in elements.keys():
            try:
                elements[key].click()
                time.sleep(1)
                if key == "Class selector":
                    elements[key].click()
                if key == "Select date":
                    self.logger.log_data(f"'{key.text}' element  >>  PASS")
                self.logger.log_data(f"'{key}' element  >>  PASS")
            except Exception as e:
                self.logger.log_data(f"'{key}' element  >>  FAIL  >>  Error: {e}")
            time.sleep(1)

        # submit the data using the SEARCH button
        try:
            self.flights_menu.search_button.submit()
            self.logger.log_data("'SEARCH' button  >>  PASS")
        except Exception as e:
            self.logger.log_data(f"'SEARCH'' button  >>  FAIL  >>  Error: {e}")
            is_valid = False

        # validate that the results page has appeared by searching the FILTER SEARCH button
        if is_valid:
            filter_search = self.main_page.filter_search
            if filter_search:
                self.logger.log_data(f"'FILTER SEARCH' button  >>  PASS")
            else:
                self.logger.log_data(f"'FILTER SEARCH' button  >>  FAIL")

        self.end_test()

    def return_home(self):
        try:
            self.main_page.main_page_reload.click()
        except Exception as e:
            self.logger.log_data(f"Failed to reload the main page  >>  CRITICAL  >>  Error: {e}")

    def end_test(self):
        self.logger.log_data("\n" + "*"*50 + "\n")
        self.return_home()
        time.sleep(3)

    def close_test(self):
        self.helper.close_session()


def main():

    tests = Tests()
    tests.test_00()

    if tests.page_loaded:
        tests.test_01()
        tests.test_02()
        tests.test_03()
        tests.test_04()
        tests.test_05()

    tests.close_test()


if __name__ == '__main__':
    main()
