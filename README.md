This is project was created using Django.

It has user authentication.
It has basic CRUD operations where the conditions(rules) can be added or deleted.
It has email notification sending utility (untested) that requires configuring settings.py to work.

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

I was not able to get the scheduler to work for the criteria(rules) given by the user.



#Assignment

Managing campaigns using Rule Based Engine

 

Tyroo needs to effectively manage Swiggy's budget for advertisement on Social platforms like Facebook and Snapchat. Industry experts at Tyroo has seen that when following conditions are met on the day, it is best to pause the campaign and then start again on the next day to reduce spilling of budget.

 

Whenever any one of the following condition is met, campaign is paused and user is notified.

 

        `eCPM` >= $5.00 AND `Impressions` >= 1000000

        `Spend` >= $1000.00 AND `eCPC` <=  $0.20

        `Clicks` >= 50000 AND `Installs` <= 100

        `eCPI` >= $2.00 AND `Installs` >= 100

 

Variables/Metrics:-

    Impressions - how many times an as had been viewed

    Clicks - how many times an ad has been clicked

    Installs - how many times people have installed Swiggy's app through Tyroo's ad on Snapchat/Facebook

    Spend - how many dollars have Swiggy spent on ads for today

    eCPM - Cost per mile impressions (Spend * 1000 / Impressions)

    eCPC - Cost per click (Spend / Clicks)

    eCPI - Cost per install (Spend / Installs)

 

Actions:-

    Notify

    Pause campaign

    Start campaign

 

We want you to create a rule based engine that enables campaign managers to setup these rules through a user interface and receive notification through email.

 

For frontend, create a single page web app with following features:-

1) Login screen with email and password

2) On successful login, user should be redirected to a page having an "Add Rule" button which allows user to create a new rule through a modal (like a contact form). The Create Rule modal must have following things:-

    a) Rule name

    b) Campaigns - to which campaign, should the rule be attached (multiselect field)

    c) Schedule - at what time should this rule be triggered

    d) Conditions - text box in which rules can be specfied as an IF..ELSE condition (`eCPM` >= $5.00 AND `Impressions` >= 1000000)

    e) Action - actions that needs to be taken

    f) Status - Activated/Deactivated

3) The same page should have a table of all the rules that has been created by the user. Each rule line in the table should specify Rule name, Campaigns, Rule Schedule, Rule Status (Activated/Deactivated) and an edit button. The edit button opens the same Create Rule modal but with data filled according to the specific rule.

 

For backend, following components are needed:-

1) Rule executor service

    a) The service should run every 15 minutes

    b) It should check for rules that must be executed according to schedule

    c) If the rule should be executed, make a lookup for data and execute the condition in the rule and trigger congiured action if needed.

2) Action executor service

    a) Implement Notify action only

 

You need to create a schema for storing user info, variables/metrics, rules and actions so that your engine is easily extensible if new metrics and actions are introduced. For executing rules, please use the following schema which stores metric data on per minute basis:-

 

    Campaign        Metric              Value           Datetime

    Swiggy             Impressions         5             2019-01-01 10:01:00

    Swiggy             Clicks                   0             2019-01-01 10:01:00

    Swiggy             Installs                 0             2019-01-01 10:01:00

    Swiggy             Spend             0.05             2019-01-01 10:01:00

    Swiggy             Impressions         7             2019-01-01 10:02:00

    Swiggy             Clicks                   2             2019-01-01 10:02:00

    Swiggy             Installs                 1             2019-01-01 10:02:00

    Swiggy             Spend             0.07            2019-01-01 10:02:00

    Netflix               Impressions       84          2019-01-01 10:02:00

    Netflix               Clicks                   6           2019-01-01 10:02:00

    Netflix               Installs                 2           2019-01-01 10:02:00

    Netflix               Spend             1.68        2019-01-01 10:02:00

 

The engine must take little to no time in executing a rule so please design a smart solution which minimzes lookup to the metrics data.

 

Assumptions:-

    1) Pre-configure for only one user Admin, with email as your personal email and random password

    2) A rule can be scheduled as - Every 15 minutes, Every hour, Every day at 12:00 AM

    3) The only action available is 'Notify'

    4) Use dummy names for campaigns. Assume 5 campaigns are there in the system.

    4) Value column represents daily metric value.

    5) Fill the metrics data with random values. Create data for atleast one hour for all campaigns. Data need not be present for every minute in the hour. 

 

 

You are free to use any open source language/framework/library/database for creating the engine. Please create a single git repository for the complete code base, upload on github and share with us along with all the requirements for executing your code.
