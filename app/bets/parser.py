from datetime import datetime
from selenium import webdriver
from flask import current_app
import csv


class Parimatch_parser:

    @staticmethod
    def get_matches(driver):
        items = driver.find_elements_by_tag_name('prematch-block')

        for item in items:
            pair = item.find_elements_by_class_name('prematch-box__team')
            # print('Players: {} vs {} :'.format(pair[0].text, pair[1].text))
            if not current_app.table_tennis.get(pair[0].text, ''):
                print('new set {}'.format(pair[0].text))
                current_app.table_tennis[pair[0].text] = {pair[1].text: {}}
            if not current_app.table_tennis.get(pair[1].text, ''):
                print('new set {}'.format(pair[1].text))
                current_app.table_tennis[pair[1].text] = {pair[0].text: {}}

            coefficents = item.find_elements_by_tag_name('main-markets-group')

            if len(coefficents):
                elements = coefficents[-1].find_elements_by_class_name('outcome__coeff')
                if len(elements) == 3:
                    # print("W1:{}, W2:{}".format(current_app.table_tennis[pair[0].text][pair[1].text], current_app.table_tennis[pair[1].text][pair[0].text]))

                    current_app.table_tennis[pair[0].text][pair[1].text] = {'W': elements[0].text, 'L': elements[-1].text}
                    current_app.table_tennis[pair[1].text][pair[0].text] = {'W': elements[-1].text, 'L': elements[0].text}

    @staticmethod
    def open_connection():
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.binary_location = current_app.config['CHROME_BROWSER_PATH']

        driver = webdriver.Chrome(current_app.config['CHROME_DRIVER_PATH'], chrome_options=options)
        return driver

    @staticmethod
    def close_connection(driver):
        try:
            driver.close()
            return True
        except Exception:
            print("Can't close driver connection")
            return False

    @staticmethod
    def parse(driver):


        # url = current_app.config['PARIMATCH_URL']
        start = datetime.now()

        Parimatch_parser.get_matches(driver)
        # print(current_app.table_tennis)
        # write_csv(i, data)
        end = datetime.now()
        total = end - start
        print("Total time spent:{}".format(str(total)))

        return current_app.table_tennis
