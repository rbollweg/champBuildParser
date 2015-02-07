__author__ = 'The Gibs'
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import sys
import re


class Match():
    def __init__(self):
        self.match_url = str()
        self.match_data = []
        self.server_played_on = str()

class ChampionBuild():
    def __init__(self, driver, participant_number):
        self.stepList = []
        self.champName = str()
        self.change_page(driver, participant_number)


    def change_page(self, driver, participant_number):
        #try:
            selector = ui.WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "participant-selector")))
            if (participant_number) <= 4:
                team_100 = selector.find_element_by_class_name('team-100')
                team_100_champs = team_100.find_elements_by_tag_name("img")
                next_champ = team_100_champs[participant_number]
                tabs_header = driver.find_element_by_class_name("tab-panel-header")
                hover = ActionChains(driver).move_to_element(tabs_header)
                hover.perform()
                next_champ.click()
            else:
                team_200 = selector.find_element_by_class_name('team-200')
                team_200_champs = team_200.find_elements_by_tag_name("img")
                next_champ = team_200_champs[participant_number - 5]
                tabs_header = driver.find_element_by_class_name("tab-panel-header")
                hover = ActionChains(driver).move_to_element(tabs_header)
                hover.perform()
                next_champ.click()
        #except:
        #    self.champName = "exception"


    def getBuild(self, driver):
            assert "No results found." not in driver.page_source

            selected = driver.find_element_by_css_selector('.champion-nameplate.selected')
            champion_image = selected.find_element_by_tag_name("img")
            champion_image_source = champion_image.get_attribute("src")
            result = re.search('(.*)/(.*).png', champion_image_source)
            champion_name = result.group(2)
            self.champName = champion_name

            buildSteps = driver.find_elements_by_class_name("build-step")

            for elementStep in buildSteps:
                step = Step()
                time = elementStep.text
                time.strip()
                if "\n" in time:
                    results = re.search('(\d*:\d*)', time)
                    time = results.group(1)
                step.time = time
                items = elementStep.find_elements_by_class_name("build-item")

                for item_container in items:
                    try:
                        item = Item()
                        if "build-item-item-sell" in item_container.get_attribute("class"):
                            item.is_sold = True
                        else:
                            item.is_sold = False
                        itemImg = item_container.find_element_by_tag_name("img")
                        image_source = itemImg.get_attribute("src")
                        result = re.search('(.*)/(.*).png', image_source)
                        item_number = result.group(2)
                        item.item_number = item_number
                        step.items.append(item)
                    except:
                        print("NoSuchEleLoL")
                self.stepList.append(step)

class Step():
    def __init__(self):
        self.time = str()
        self.items = []

class Item():
    def __init__(self):
        self.item_number = str()
        self.is_sold = bool

def spider(url):
    driver = webdriver.PhantomJS(service_log_path='C:/Users/The Gibs/PycharmProjects/extremeFlask/ghostdriver.log', executable_path="C:/bin/phantomjs/phantomjs.exe")
    driver.get(url)
    current_match = Match()
    current_match.match_url = url
    for i in range(0, 10):
        champBuild = ChampionBuild(driver, i)
        if champBuild.champName != "exception":
            champBuild.getBuild(driver)
            current_match.match_data.append(champBuild)
        else:
            driver.quit()
    driver.quit()
    return current_match