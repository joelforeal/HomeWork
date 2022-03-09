## How to install libraries of requirements.txt
**$ pip install -r requirements.txt**

## Uninstall what you just install from requirements.txt
**$ pip uninstall -r requirements.txt -y**

## To run script , you should have: 
  - python v3.90+
  - install libraries of requirements.txt
  - Downlaod chrome webdriver(that match your chrome version) and place it under root folder of installed Python  

Then you can execute following command to run scripts under root folder of scripts :
** $ python -m pytest**

(Note: after execution , you can check screenshots under {script root}\screenshots\ )


## Test case design:
### 1.For UI case:
> To check user can open ZIL/USDT trading page , start from /markets page;  
    In markets page,  
    - check markets page loading completed .  
    - check expected "USDT" element present .  
    - Check script will locate "ZIL/USDT" item ,then to find "Trade" button of the same line.  
    - Check rending to trading page is working , and can see clear "ZIL/USDT" item appeared.  
    
Meanwhile, also take screenshots of current locations for references.


### 2.For API case:
> To find out the expected humidity data of  (N)day after tomorrow,  
    need to write simple script to send "GET" request through following url:  
    [https://pda.weather.gov.hk/locspc/data/fnd_uc.xml] to get 9 days data,  
    which information is obtained via ios phone by using ZAP to scan traffic.  
    
About testcase design:
   - Send out request , then use jsonpath to extract expected property value by JSON PATH expression.
   - After make sure the specific humidity data can be found (Max_rh&Min_rh), define a function to list the value according what day after Tomorrow, to show these % data. 
   - Assert status code should be (equal) "200"  
   - Assert "general_situation" content should not be None(null value)  



    
