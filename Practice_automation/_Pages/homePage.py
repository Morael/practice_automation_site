class Home:

    def __init__(self, driver):
        self.driver = driver

        self.shop_link_text = "Shop"
        self.arrivals_class_name = "woocommerce-LoopProduct-link"
        self.arrival_less_than_450 = "#text-22-sub_row_1-0-2-2-0 > div > ul > li > a.woocommerce-LoopProduct-link > img"
        self.sliders_class = "n2-ss-slide-fill"

    def click_shop(self):
        self.driver.find_element_by_link_text(self.shop_link_text).click()

    def find_count_arrivals(self):
        arrivals_count = len(self.driver.find_elements_by_class_name(self.arrivals_class_name))
        return arrivals_count

    def count_sliders(self):
        count_sliders = len(self.driver.find_elements_by_class_name(self.sliders_class))
        return count_sliders

    def find_click_arrivals_img(self):
        self.driver.find_element_by_class_name(self.arrivals_class_name).click()

    def click_arrival_price_300(self):
        self.driver.find_element_by_css_selector(self.arrival_less_than_450).click()




