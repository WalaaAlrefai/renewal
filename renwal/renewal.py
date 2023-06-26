from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from arabic_reshaper import reshape
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False , slow_mo=50)

    page=browser.new_page()
    page.goto('https://eservices.cspd.gov.jo/index-rtl.html')
    page.fill('input[name="username"]','9912017766')
    page.fill('input[name="password"]','luluRe*91')
    page.click('input[type=submit]')
    # page.is_visible('div.filters col-md-12 col-xs-12 col-sm-12')
    # html = page.inner_html('div')
    html = page.inner_html('button[data-filter=".FamilyBooks"]')
    # print (reshape(html))
    # soup=BeautifulSoup(html,'html.parser')
    # print(soup.find_all('button'))
    page.click('button[data-filter=".FamilyBooks"]') # button دفاتر العائلة
    d=page.inner_html('div.service.sub-service.mix.FamilyBooks')
    soup=BeautifulSoup(d,'html.parser')
    result=soup.find('h4',string='ﺔﻠﺋﺎﻋ ﺮﺘﻓﺩ ﻒﻟﺎﺗ ﻝﺪﺑ')
    print(11111111111,result)
    n=soup.text.strip()
    print(12112212212,n)
    x=reshape(n)

    print(22222222222,x[::-1])
   
    # html2 = page.inner_html('h4')
    # print(c)
    if n == 'بدل تالف دفتر عائلة':
        page.click('div.service.sub-service.mix.FamilyBooks')
        b=page.inner_html('#CKEditorForMendix_widget_CKEditorViewerForMendix_0')
    # soup1=BeautifulSoup(b,'html.parser')
    # result1=soup1.find_all('div')
        print(33333333333,b[::-1])
        
        page.click('button.btn.mx-button.mx-name-actionButton9.fa.Next.mobilebtn.btn-default')
        c=page.inner_html('div.mx-name-layoutGrid6.mx-layoutgrid.mx-layoutgrid-fluid') 
        print(44444444444,c) ####
        f=page.inner_html('div.mx-name-textBox11.lostpassfirstname.mx-textbox.form-group.no-columns')
        # g=page.input_value('div.mx-name-textBox11.lostpassfirstname.mx-textbox.form-group.no-columns')
        print(55555555555,f)
        # print(55555555555,g)
        # page.fill('input#1000.Booklet.Step1FamilyBookletDamage.textBox20.336_kel_75.form-control','224891')
        # page.fill('select#1000.Booklet.Step1FamilyBookletDamage.dropDown5.341_kel_76.form-control',value='لا')
        input_selector = '#1000.Booklet.Step1FamilyBookletDamage.textBox20.336_btb_75'  # Replace with the appropriate selector for the input field
        input_element = page.wait_for_selector(input_selector)
        input_element.fill('224891')


        select_selector = '#1000.Booklet.Step1FamilyBookletDamage.dropDown5.341_kel_76.form-control'  # Replace with the appropriate selector for the select field
        select_element = page.select_option(select_selector, value='لا')




    else:
        print('error')
    # print(111111111,page.inner_html('div.mx-name-container2.footer-btn'))
    # page.click('button.btn.mx-button.mx-name-actionButton9.fa.Next.mobilebtn.btn-default') ####
    
    # c=page.inner_html('div.mx-name-layoutGrid6.mx-layoutgrid.mx-layoutgrid-fluid') ####
    # print(44444444444,c) ####
    # f=page.inner_html('div.mx-name-textBox11.lostpassfirstname.mx-textbox.form-group.no-columns')####
    # print(3333333333,f)
    
    # soup=BeautifulSoup(c,'html.parser')
    # result=soup.find_all('input')
    
    # print(333333,result)
    # soup1=BeautifulSoup(f,'html.parser')
    # result1=soup1.find('input')
    # print(44444,result1)
    
    # page.fill('input#1000.Booklet.Step1FamilyBookletDamage.textBox20.336_kel_75.form-control','224891')
    # page.fill('select#1000.Booklet.Step1FamilyBookletDamage.dropDown5.341_kel_76.form-control','لا')
    # page.click('button.btn.mx-button.mx-name-actionButton9.fa.Next.mobilebtn.btn-default')

# html_code = '''
# <button type="button" class="btn mx-button mx-name-actionButton9 fa Next mobilebtn btn-default" title="" data-button-id="1003.Booklet.FamilyBookletDamagePrerequisites.actionButton9" data-disabled="false" style="font-family: inherit; height: 35px; width: 150px;"> التالي</button>
# '''

# # Create a BeautifulSoup object
# soup = BeautifulSoup(html_code, 'html.parser')

# # Find the button element
# button = soup.find('button')

# # Extract the attributes and their values
# button_type = button.get('type')
# button_class = button.get('class')
# button_title = button.get('title')
# button_data_button_id = button.get('data-button-id')
# button_data_disabled = button.get('data-disabled')
# button_style = button.get('style')
# button_text = button.text

# # Print the extracted data
# print('Button Type:', button_type)
# print('Button Class:', button_class)
# print('Button Title:', button_title)
# print('Button Data-button-id:', button_data_button_id)
# print('Button Data-disabled:', button_data_disabled)
# print('Button Style:', button_style)
# print('Button Text:', button_text)


# button_selector = 'button.btn.mx-button.mx-name-actionButton9.fa.Next.mobilebtn.btn-default'
# button = page.wait_for_selector(button_selector)
# button.click()
# browser.close()


