# TRIUMF 435 User Guide

## Introduction
This document is designed to help you understand and use the webpage created by TRIUMF-435 2022. This webpage was created to help users read and monitor process data from EPICS devices. 

## Login 
The login page gives a password protected webpage. Only allowing users who know the password to access the data behind it. The password is "Test"
\
<img src="/user-guide-images/home-page.jpg"/>

## Dashboard Selection
The dashboard selection page allows the user to select which dashboard they want to display. If the user does not have a dashboard yet, they are able to click on the create dashboard button to create a new one.
\
<img src="/user-guide-images/dashboard-select.jpg"/>

## Dashboard Creation
If the user want to create a new dashboard, they will be redirected to the dashboard creation page. This page will allow the user to choose a name they want for their dashboard, if the name is taken, then they will not be able to create the dashboard. All dashboard names must be unique for storing purposes. Once created, they will be redirected to their new blank dashboard.
\
<img src="/user-guide-images/dash-create.jpg"/>

## Editing Dashboard
If the user wants to add process variables to the dashboard, use the input on the bottom of the page to input the process variable address ( Example : CSB:FC5:SCALECUR ). Once added, the process variable will now be displayed in the viewing page. In addition, you are able to remove process varialbes on this page. Simply click on the remove button and confirm the action in the browser alert. Once confirmed, the process variable will be taken off the dashboard. To finally view real time data of the dashboard, click on the button Change Dashboard on the top right of the webpage
\
<img src="/user-guide-images/add-pv.jpg"/>

## Viewing Dashboard
When viewing the data, process variables will automatically update every 5 seconds. To change this, add an extra variable at the end of the URL that you want for the desired seconds before each update. ( Example: /dashbaord_name/seconds_per_refresh). This page will not allow process variables to be changed in this page. You must go back to edit the PVs displayed. 
\
<img src="/user-guide-images/view-pv.jpg"/>