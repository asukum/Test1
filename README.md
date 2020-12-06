# Test1
Successfully automate login to Web browser using selenium, python and page object model.
This is the repository for automating a login page using Selenium and Python with Page Object Model framework

You can get a copy of all files used in this tutorial by cloning this repository!

```shell
git clone https://github.com/asukum/Test1.git 
```

# Folder Structure
1) CONFIG has the URL and Credential Details
2) PAGES has seperate files for each page that needs to be automated and each page has the collection of Webelements and its actions
3) TEST has the test cases files for each page
4) Utils has the Test Report and Logging

Command to run the Test
```shell
pytest Tests/test_LoginPage.py
```

Command to run the Test and generate Report
```shell
pytest Tests/test_LoginPage.py -v --html=./Reports/testrun.html
```
