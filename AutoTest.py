# AutoTest.py

from CreateTest.CreateTest import CreateTest
from PrepareTest.PrepareTest import PrepareTest


class AutoTest:
    def __init__(self):
        # print(r'Auto Test default constractor')
        self.create_test = CreateTest()
        self.prepare_test = PrepareTest()
        self.id = 0

    # def __init__(self, test_name, test_id):
    #     print(r'Auto Test constractor')
    #     self.create_test = CreateTest()
    #     print(self.create_test.print_test_print_parameters())

    def do_create_test(self, requested) -> (str, int):
        self.create_test.set_test_name(requested['Name'])
        self.create_test.set_test_prerequisite(requested['Prerequisite'])
        self.create_test.set_test_timeout(requested['RunTimeout'])
        self.create_test.set_test_summary(requested['Summary'])
        self.create_test.set_test_threshold(requested['ResultThreshold'])
        self.create_test.set_test_main_version(requested['MainVersion'])
        self.create_test.set_test_site(requested['Site'])
        self.create_test.set_test_environment(requested['Environment'])
        # self.create_test.set_test_environment(requested['StartPoint'])

        self.create_test.print_test_print_parameters()
        return self.create_test.do_main()

    def do_prepare_test(self, requested_id, requested_name) -> str:
        self.prepare_test.set_test_id(requested_id)
        self.prepare_test.set_test_name(requested_name)

        return self.prepare_test.do_main()

    def main(self):
        self.id = 1


# print("AutoTest name: " + __name__)

if __name__ == "AutoTest":
    pass  # print("do main()")
