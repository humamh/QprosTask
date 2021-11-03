from selenium import webdriver



driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://petclincqpros.herokuapp.com/")
element = driver.find_element_by_xpath("(//img[@class='img-responsive'])[1]")
if 'ng-hide' not in element.get_attribute('class'):
    print('The image has been verified on the screen\n')
else:
    print('The image hasnt been verified on the screen\n')

driver.find_element_by_xpath("(//span[normalize-space()='Veterinarians'])[1]").click()

list=driver.find_elements_by_xpath ("(//table[@id='vets'])[1]")

for i in list :

 print (i.text + "\n")

driver.find_element_by_xpath("(//span[normalize-space()='Find owners'])[1]").click()

driver.find_element_by_xpath("(//button[contains(text(),'Find')])[1]").click()

list=driver.find_elements_by_xpath ("(//table[@id='owners'])[1]")

for i in list :

 print (i.text + "\n")

driver.find_element_by_xpath("(//span[normalize-space()='Find owners'])[1]").click()

driver.find_element_by_xpath("(//a[normalize-space()='Add Owner'])[1]").click()

First_Name = "Homam"
Last_Name = "Sefer Alhalabi"
Address = "Tlaa alali"
City = "Amman"
Telephone = "0000000000"
Pet_Name = "Chiba"
Birth_Date = "2021-11-01"

element = driver.find_element_by_xpath("(//input[@id='firstName'])[1]")
element.send_keys(First_Name)

element = driver.find_element_by_xpath("(//input[@id='lastName'])[1]")
element.send_keys(Last_Name)

element = driver.find_element_by_xpath("(//input[@id='address'])[1]")
element.send_keys(Address)

element = driver.find_element_by_xpath("(//input[@id='city'])[1]")
element.send_keys(City)

element = driver.find_element_by_xpath("(//input[@id='telephone'])[1]")
element.send_keys(Telephone)

driver.find_element_by_xpath("(//button[normalize-space()='Add Owner'])[1]").click()

driver.find_element_by_xpath("(//a[contains(text(),'Add')])[1]").click()

element = driver.find_element_by_xpath("(//input[@id='name'])[1]")
element.send_keys(Pet_Name)

element = driver.find_element_by_xpath("(//input[@id='birthDate'])[1]")
element.send_keys(Birth_Date)

driver.find_element_by_xpath("(//select[@id='type'])[1]").click()
driver.find_element_by_xpath("(//option[@value='cat'])[1]").click()
driver.find_element_by_xpath("(//button[normalize-space()='Add Pet'])[1]").click()
