import unittest
from Task_1 import yandex_Search
from Task_2 import yandex_Image

# class yandex_search_Test(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path="./chromedriver")
#         self.driver.get("https://www.yandex.ru/")

#     def tearDown(self) -> None:
#         self.driver.close()
#         self.driver.quit()


class yandex_Test(unittest.TestCase):
    def test_01(self):
        yandex_Search("https://www.yandex.ru/", 'Тензор')

    def test_02(self):
        yandex_Image("https://www.yandex.ru/")


if __name__ == '__main__':
    unittest.main()
