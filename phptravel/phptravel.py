from selenium import webdriver
import getpass
import time


class Logger:
    def __init__(self):
        self.create_log_file()

    @staticmethod
    def create_log_file():
        try:
            with open(f'/Users/{getpass.getuser()}/Desktop/test_results.txt', 'w') as f:
                f.write('THE RESULTS OF THE TEST ARE: \n\n\n')
        except Exception as e:
            print(f"Results file couldn't be created. The test result won't be recoreded. Error: {e}")

    @staticmethod
    def log_data(text):
        with open(f'/Users/{getpass.getuser()}/Desktop/test_results.txt', 'a') as f:
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
    def __init__(self):
        self.page_title = "PHPTRAVELS"

        # elements represented by xpath (can also be created private and returned as @property)
        self.hotels_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[1]/a"
        self.flights_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[2]/a"
        self.tours_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[3]/a"
        self.cars_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[4]/a"
        self.visa_button = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/nav/ul/li[5]/a"

        self.hotels_destination_text = "DESTINATION"
        self.hotels_checkin_text = "CHECK IN"
        self.hotels_checkout_text = "CHECK OUT"
        self.hotels_adults_text = "ADULTS (12-75)"
        self.hotels_child_text = "CHILD (2-12)"

        self.hotels_destination_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[1]/div/label"
        self.hotels_checkin_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[1]/div/label"
        self.hotels_checkout_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[2]/div/div/div[2]/div/label"
        self.hotels_adults_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[1]/div/label"
        self.hotels_child_label = "/html/body/div[2]/div[1]/div[1]/div[3]/div/div/div/div/div/div/div[1]/div/div/form/div/div/div[3]/div/div/div/div/div/div/div[2]/div/label"


class Tests:
    def __init__(self):
        self.logger = Logger()
        self.session = PhpTravel()
        self.page_loaded = True
        self.page_objects = PageObjects()

    def test00(self):
        time_loaded = self.session.open_page()
        time.sleep(5)

        if self.page_objects.page_title in self.session.driver.title:
            self.logger.log_data(f"Page LOADED in {time_loaded} seconds \n\n")
        else:
            self.logger.log_data(f"Page FAILED to load. Exiting tests...\n")
            self.page_loaded = False

    def test01(self):
        self.logger.log_data("TEST 01 >> checking the following buttons: Flights, Tours, Cars, Visa, Hotels\n")

        buttons = {"Flights": self.page_objects.flights_button, "Tours": self.page_objects.tours_button, "Cars": self.page_objects.cars_button, "Visa": self.page_objects.visa_button,
                   "Hotels": self.page_objects.hotels_button}

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

    def test02(self):
        self.logger.log_data("TEST 02 >> checking menu: Hotels\n")

        expected_labels = {self.page_objects.hotels_destination_text: self.page_objects.hotels_destination_label,
                           self.page_objects.hotels_checkin_text: self.page_objects.hotels_checkin_label,
                           self.page_objects.hotels_checkout_text: self.page_objects.hotels_checkout_label,
                           self.page_objects.hotels_adults_text: self.page_objects.hotels_adults_label,
                           self.page_objects.hotels_child_text: self.page_objects.hotels_child_label}
        found_labels = []

        hotels = self.session.find_element_by_xpath(xpath=self.page_objects.hotels_button)
        if hotels:
            hotels.click()
            time.sleep(1)
            if hotels.is_enabled():
                for key in expected_labels.keys():
                    element = self.session.find_element_by_xpath(xpath=expected_labels[key])
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

    def test03(self):
        self.logger.log_data("TEST 03 >> checking menu: Flights\n")
        expected_labels01 = {"FROM": "col-md-6.col-6", "TO": "col-md-6.col-6", "DEPART": "class12.col-6.col-12"}
        expected_labels02 = {"ADULTS": "col-md-3.col-xs-12", "CHILD": "col-md-3.col-xs-12", "INFANT": "col-md-3.col-xs-12"}
        found_labels = []

        flights = self.session.find_element_by_link("Flights")
        if flights:
            flights.click()
            time.sleep(1)
            if flights.is_enabled():
                for value in expected_labels01.values():
                    labels = self.session.find_elements_by_class(cls=value)
                    for element in labels:
                        found_labels.append(element.find_element_by_class_name("form-group").find_element_by_tag_name("label").text)
                for label in expected_labels01.keys():
                    if label in found_labels:
                        self.logger.log_data(f"{label} is present in the Hotels menu  >>  PASS")
                    else:
                        self.logger.log_data(f"{label} is not present in the Hotels menu  >>  FAIL")
                found_labels.clear()
                for value in expected_labels02.values():
                    labels = self.session.find_elements_by_class(cls=value)
                    for element in labels:
                        if element.find_elements_by_class_name("col-4"):
                            for item in element.find_elements_by_class_name("col-4"):
                                if item.find_element_by_class_name("form-group.form-spin-group").find_element_by_tag_name("label"):
                                    found_labels.append(item.find_element_by_class_name("form-group.form-spin-group").find_element_by_tag_name("label").text)
                for label in expected_labels02.keys():
                    if label in found_labels:
                        self.logger.log_data(f"{label} is present in the Hotels menu  >>  PASS")
                    else:
                        self.logger.log_data(f"{label} is not present in the Hotels menu  >>  FAIL")
        self.logger.log_data("\n\n")

    def close_test(self):
        self.session.close_session()


def main():

    tests = Tests()
    tests.test00()

    if tests.page_loaded:
        tests.test01()
        tests.test02()
        #tests.test03()
        tests.close_test()


if __name__ == '__main__':
    main()
