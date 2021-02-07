try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except ImportError:
    print("Install Selenium")


import time
from datetime import datetime
import os

class SpeedTest:
    def __init__(self, waitTime = 5):
        try:
            self.url = "https://www.bing.com/widget/t/speedtest"
            self.waitTime = waitTime

            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--headless")
            self.options.add_argument("--enable-javascript")

            self.driver = webdriver.Chrome(chrome_options=self.options)
            self.driver.implicitly_wait(time_to_wait=waitTime)
            self.driver.get(self.url)
        except Exception as ex:
            print("SpeedTest::__init__() Exception:", str(ex))

    def isOpen(self):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h4[@id='answerTitle']")
                )
            )
            if "internet speed test" in el.text.lower():
                return True
            else:
                return False
        except:
            return False

    def getIP(self):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//h4[@id='answerTitle']")
                )
            )
            if "internet speed test" in el.text.lower():
                arr = el.text.lower().strip().split("ip -")
                if len(arr) == 2:
                    return arr[1].strip()
            return False
        except:
            return False

    def StartTest(self):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='button']")
                )
            )
            if "start" in el.text.lower():
                el.click()
            else:
                print("already started...")
            return True
        except Exception as ex:
            print("SpeedTest::StartTest() Exception:", str(ex))
            return False

    def getPingValue(self):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='pingValue']")
                )
            )
            t = el.text.strip()
            if len(t)<1:
                return False
            return t
        except:
            return False

    def getTestSpeed(self):
        try:
            elSpeed = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='speed']")
                )
            )
            elUnit = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='unit']")
                )
            )

            tSpeed = elSpeed.text.strip()
            tUnit = elUnit.text.strip()

            if len(tSpeed)<1 or len(tUnit)<1:
                return False
            else:
                return "{} {}".format(tSpeed, tUnit)
        except:
            return False

    def getDownloadSpeed(self):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='downloadValue']")
                )
            )
            t = el.text.strip()
            if len(t)<1:
                return False
            else:
                return t
        except:
            return False

    def getUploadSpeed(self):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@id='uploadValue']")
                )
            )
            t = el.text.strip()
            if len(t)<1:
                return False
            else:
                return t
        except:
            return False

    def isTesting(self):
        try:
            el = WebDriverWait(self.driver, self.waitTime).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@id='button']")
                )
            )
            if "start" in el.text.lower():
                return False
            elif "stop" in el.text.lower():
                return True
            else:
                return True
        except Exception as ex:
            return False



    def __del__(self):
        try:
            self.driver.close()
            self.driver.quit()
        #except Exception as ex:
            #print("SpeedTest::__del__() Exception:", str(ex))
        except:
            pass


def main():
    s = SpeedTest()
    print("Website open:",s.isOpen())
    print("IP:", s.getIP())
    print("Test started:", s.StartTest())

    lastpstr=""
    while s.isTesting():
        pingvalue = s.getPingValue()
        speed = s.getTestSpeed()
        downspeed = s.getDownloadSpeed()
        upspeed = s.getUploadSpeed()

        pstr = ""
        if pingvalue is not False:
            pstr += "{}:{}".format(" Ping", pingvalue)

        if speed is not False:
            pstr += "{}: {}".format(" Realtime Speed", speed)

        if downspeed is not False:
            pstr += "{}: {}".format(" Download Speed", downspeed)

        if upspeed is not False:
            pstr += "{}: {}".format(" Upload Speed", upspeed)

        if not(lastpstr==pstr):
            if len(pstr)>1:
                print(datetime.now(), "- [IP:", s.getIP(),"]\n", pstr,"\n")
            lastpstr = pstr

        time.sleep(1)

        pingvalue = s.getPingValue()
        speed = s.getTestSpeed()
        downspeed = s.getDownloadSpeed()
        upspeed = s.getUploadSpeed()

    pstr = ""
    if pingvalue is not False:
        pstr += "{}:{}".format(" Ping", pingvalue)

    if speed is not False:
        pstr += "{}: {}".format(" Realtime Speed", speed)

    if downspeed is not False:
        pstr += "{}: {}".format(" Download Speed", downspeed)

    if upspeed is not False:
        pstr += "{}: {}".format(" Upload Speed", upspeed)

    if len(pstr)>1:
        print(datetime.now(), "- [IP:", s.getIP(),"]\n", pstr, "\n")
    else:
        print(datetime.now(), "Failed to SpeedTest")

    os.system("PAUSE")




if __name__ == "__main__":
    main()
