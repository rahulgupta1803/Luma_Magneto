import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='edge':
        driver=webdriver.Edge()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver=webdriver.Chrome(options=options)

    driver.get('https://magento.softwaretestingboard.com/')
    driver.maximize_window()
    yield driver
    driver.quit()
    return driver

def pytest_metadata(metadata):
    metadata['tester'] = 'Rahul Gupta'
    metadata['class'] = 'Credence'
    metadata['batch'] = 'ct15'
    metadata.pop('Packages', None)

@pytest.fixture(params=[
    ('rahuls@iesta.com','Rahul1234..'),
    ('rahuls@iesta.com','Rahul1234...'),
    ('Rahuls@hiesta.com','rahul12345'),
    ('Rahul@pista.com','Rahul@12345'),
    ('Rahul@husta.com','Rahul@#$%')
])
def getuserdata(request):
    return request.param



