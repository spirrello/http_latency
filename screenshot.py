#!/usr/bin/env python

"""This script will measure load times for several sites."""


from selenium import webdriver
from depot.manager import DepotManager

depot = DepotManager.get()
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768) # set the window size that you need 
driver.get('http://192.168.122.101/cgi-bin/measure_sites.py')
driver.save_screenshot('http-latency.png')

