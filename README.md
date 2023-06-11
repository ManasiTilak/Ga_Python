
# Project Title

Python Script to fetch the Top 5 Pages of your Website (from Google Analytics 4)

## Prerequisites : 

- Google developer profile : To get one, sign in to your google account and activate it by going to the google's [developer](developers.google.com) site.

- A google analytics property setup. This can be a blog or a website whose analytics you want to track. If you want to learn more about how to set up google analytics for your website, go to the official google analytics documentation [here](https://support.google.com/analytics/answer/9304153?hl=en).

-Google Analytics 4 API setup. In order for your python script to work you should have Google Analytics 4 API setup and working for your project. If you want to know how to set up the Google Analytics API for your project, go to [here](https://codingaunty.com/google-analytics4-api-setup/).


## How to Run
- Create a virtual environment `python -m venv venv`
- Activate it using :
`source venv/bin/activate` 
- Install the requirements from the requirements.txt file
`pip install -r requirements.txt`
- Make a folder called `data`, in that folder make a file called `posts.json`. This is where you should get your data after running the script.
- Get your secret key and save it as `service_account.json` in the root of your project directory. You can get the secret key for your project from [here](https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries). If you want to learn how to step by step, read [this](https://codingaunty.com/google-analytics4-api-setup/)
- Get your property id following the instructions given in the link above. Make a `.env` file in your root directory. In the `.env` file, add : 
```
PROPERTY = 123456789 
```
Replace 123456789 with your property id. 

This should successfully setup your project. 
For more details, check [here](https://codingaunty.com/python-script-for-google-analytics-4-top-5-pages/).

Happy Coding!


