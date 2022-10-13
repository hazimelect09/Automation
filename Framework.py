from TestingConnection import setup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
class framework:
 def __init__(self,ChromePATH):
  s = setup(ChromePATH)
  self.driver = s.driver
 def chooseReligion(self,religion):
  WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'religion')))
  self.driver.find_element_by_id('religion').click()   # click on religion dropdown list
  if religion == 'Muslim':
        self.driver.find_element_by_id('religion1').click()  # choose muslim from the drop-down list
  else:
        self.driver.find_element_by_id('religion0').click()   # choose non-muslim from the drop-down list
 def chooseWorktype(self,worktype):
    self.driver.find_element_by_id('workType').click()   # click on workType dropdown list
    if worktype == 'Full Time':
        self.driver.find_element_by_id('workType0').click()  # choose Full-time from the list
    else:
        self.driver.find_element_by_id('workType1').click()   # choose part-time from dropdown list
 def chooseWorkDomain(self,workdomain):
    self.driver.find_element_by_id('abroadInd').click()  # click on work-domain dropdown list
    if workdomain == 'Abroad':
        self.driver.find_element_by_id('abroadInd0').click()  # choose Abroad from work-domain dropdown list
    else:
        self.driver.find_element_by_id('abroadInd1').click()  # choose Inland from work-domain dropdown list
 def writeIBan(self,IBAN):
    self.driver.find_element_by_id('iban').send_keys(IBAN) #send IBAN number to the controller
 def writeBank(self,Bank):
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/div[7]/div/div[2]/input').send_keys(Bank)
 def chooseContractPeriod(self,ContractPeriod):
    time.sleep(1)
    self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    #driver.execute_script("arguments[0].click();", element)
    element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "contractT")))
    element=self.driver.find_element(By.ID,'contractT')
    self.driver.execute_script("arguments[0].click();", element)

    #element.click()
    time.sleep(1)
    #self.driver.find_element_by_id('contractT').click() #click on contract period
    #if ContractPeriod == 'Fixed Contract':
    #    self.driver.find_element_by_id('contractT0').click()  # choose fixed contract from contract period dropdownlist
   # else:
    self.driver.find_element_by_id('contractT0').click()  # choose work related contract from contract period dropdownlist
 def writeDate(self,Dat):
    print(Dat)
    #self.driver.find_element_by_xpath('//input[contains(@placeholder,"DD/MM/YYYY")]').send_keys(Dat)
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/contract-form/div/div[2]/div[2]/input').send_keys(Dat)
 def writeEndDate(self,Dat):
     self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/contract-form/div/div[2]/div[3]/input').send_keys(Dat)
 def writeEndPeriod(self,End):
     self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/contract-form/div/div[2]/div[3]/div[2]/div[1]/input').send_keys(End)
     self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/contract-form/div/div[2]/div[3]/div[2]/div[2]/input').send_keys('0')
 #Enter Contract Start Date
 def writeWorkingHours(self,workhours):
     self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/contract-form/div/div[3]/div[3]/input').send_keys(workhours)
 def chooseWorkingHours(self,ContractPeriod):
     element = self.driver.find_element_by_id("workingStandard")
     self.driver.execute_script("arguments[0].click();", element)  # Click on working hours dropdown-list
     if ContractPeriod == 'daily':
        self.driver.find_element_by_id('workingStandard').click()  # Click on working hours dropdown-list
     else:
         element = self.driver.find_element_by_id("workingStandard1")
         self.driver.execute_script("arguments[0].click();", element)
 def writeWeeklyworkingDays(self,Days):
    self.driver.find_element_by_xpath('//input[contains(@formcontrolname,"weeklyWorkingDays")]').send_keys(Days)  # Enter Weekly working days
 def writeAnualleave(self,days):
    self.driver.find_element_by_xpath('//input[contains(@formcontrolname,"annualLeave")]').send_keys(days)  # Enter Number of annual leave
 def Next(self):
    self.driver.find_element_by_xpath('//button[contains(.,"Next")]').click() #click on Next
 def Previus(self):
    self.driver.find_element_by_xpath('//button[contains(.,"Previous")]').click() #click on Next
 def EnterjobTitle(self,Arabic,English):
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/div[4]/pms-employment-form/div/div[3]/div[2]/input').send_keys(Arabic)
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/div[4]/pms-employment-form/div/div[3]/div[3]/input').send_keys(English)
 #click on Salary radio button
 def chooseSalarycard(self):
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/div[6]/div[2]/label/span').click()
#Click on Select Country
 def chooseCountry(self,Country):
    self.driver.find_element_by_xpath('//span[contains(.,"Select country")]').click()
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/div[4]/pms-employment-form/div/div[4]/div[3]/div/angular2-multiselect/div/div[2]/div[3]/div[1]/input').send_keys(Country)
 def chooseCity(self,City):
    # click on Select city
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/div[4]/pms-employment-form/div/div[4]/div[3]/div/angular2-multiselect/div/div[1]/div').click()
    # Type on the search
    self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/div[4]/pms-employment-form/div/div[4]/div[3]/div/angular2-multiselect/div/div[2]/div[3]/div[1]/input').send_keys(City)
    str = '//li[contains(.,"'+ City +'")]'
    self.driver.find_element_by_xpath(str).click()
 def agree(self):
     self.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
     self.driver.find_element_by_class_name('check--label-box').click()
 def submit(self):
     print('Inside the submission')
     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     self.driver.find_element_by_xpath('//button[contains(.,"Submit")]').click()
 def Issuccessfull(self):
    return self.driver.find_element_by_id('alert-message').is_displayed()
 def navigate(self):
     self.driver.find_element_by_id('auditReportDownloadReportButton').click()  # employer button
     self.driver.find_element_by_xpath('//button[contains(.,"Authenticate")]').click()

 def Searchemp(self,Iqama):
     WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'filter-text')))
     input =self.driver.find_element_by_id('filter-text')
     textlen = len(input.get_attribute('value'))
     if  textlen>0:
          input.clear()
     self.driver.find_element_by_id('filter-text').send_keys(Iqama)
     #element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Search")]')))
     #element.click()
     wait = WebDriverWait(self.driver, 15)
     element = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Search")]')))
     element.click()
     #WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[contains(.,"Search")]')))
     #self.driver.find_element_by_xpath('//button[contains(.,"Search")]').click()
 def checkstate(self):
     check= self.driver.find_element_by_xpath('//button[contains(.,"Authenticate")]').is_displayed()
     if check == True:
         result =1
         return  result
     check = self.driver.find_element_by_id('noData')
     if check==True:
         result =2
         return result
 def authenticate(self):
     self.driver.find_element_by_xpath('//button[contains(.,"Authenticate")]').click()
 def checknodata(self):
     return len(self.driver.find_elements_by_id('noData'))
 def checkabsher(self):
     return len(self.driver.find_elements_by_id('modal-title'))
 def handleabsher(self):
      self.driver.find_element_by_id('okBtn').click()
 def checkauthenticated(self):
     return len(self.driver.find_elements_by_xpath('//button[contains(.,"Reauthenticate")] '))
 def writeProbation(self,Probation):
     element = self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/contract-form/div/div[3]/div[1]/input')
     element.clear()
     element.send_keys(Probation)
 def checkadditional(self):
     elements = self.driver.find_elements_by_id('workingStandard')
     if len(elements) > 0:
         self.driver.find_element_by_xpath('//button[contains(.,"Next")]').click()  # click on Next
     WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[contains(.,"Submit")]')))
     count =len(self.driver.find_elements_by_class_name('check--label-box'))
     return count
 def agreeAdditionalterm(self):
     elements =  self.driver.find_elements_by_class_name('check--label-box')
     for i in elements:
         i.click()
     time.sleep(1)
 def close(self):
     self.driver.close()
 def waitLoading(self):
     count = len(self.driver.find_elements_by_xpath('/html/body/pms-root/router-outlet/pms-busy-loader/div/div'))
     while count > 0:
         count = len(self.driver.find_elements_by_xpath('/html/body/pms-root/router-outlet/pms-busy-loader/div/div'))
         time.sleep(1)
 def checkSearch(self):
     elem= len(self.driver.find_elements_by_id('filter-text'))
     return elem
 def Nextv2(self):
     element = len(self.driver.find_elements(By.ID, 'contractT'))
     if element > 0:
      self.driver.find_element_by_xpath('//button[contains(.,"Next")]').click()
 def writeNoticeperiod(self,Notice):
     element = self.driver.find_element_by_xpath('//*[@id="homeContainer"]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/pms-contract-authentication/pms-contract-authentication-form/div/form/contract-form/div/div[4]/div[2]/input')
     element.clear()
     element.send_keys(Notice)