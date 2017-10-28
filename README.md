# Contents
1. [Introduction: Political Fundraising](RAEDME.md#objective)
2. [Input Data](README.md#input-data)
3. [Analysis](README.md#analysis)
4. [Steps](README.md#features)
5. [Output Data](RAEDME.md#output-data)
6. [Summary](RAEDME.md#summary)



### Introduction
Federal election commission regularly publishes campaign contributions. Though identifying individual donors in terms of their $ contributions are important but we will not do it since federal law phohibits that. As a data analyst we would rather identify lucrrative time and area for soliciting future donations for similar candidate.  

### Goal
This project aims to analyze purchases within the social network of users and detect users like user's id 1, 2, etc showing anomalous behavior i.e.; some shopper (referenced by id) making consecutively huge number of purchases (for a unique "id" and "timestamp") comparing the average trend (parameter: No of purchases, total purchases, etc) be identified as flagged purchase and be reported as 

{"event_type":"purchase", "timestamp":"2017‐06‐13 11:33:02", "id": "2", "amount": "1601.83", mean": "29.10", "sd": "21.46"}
in the output file flagged_purchases.json (amount $1601.83 is the total amount of purchase ? or ...).

Of course the mean and sd will be counted using the number of consecutive (unique "timestamp") purchases by a shopped with a unique id say id 7.

### Example
If user A makes a large purchase, we should "flag" them to make sure taht user B and C are influenced by it. C is mutual friend of all A, B and C. D can be notified regarding the large purchase recommending they become friends with user A since D was degree 2 friend of A. If D is now friend of A, then A and D shares a mutual friend C. 

We want to identify real high purchases; purchases that are 3 stndard drviation above the average within their social network. 
Comment: identify social network ?

### Comment

1. Social network change their purchasing behavior over time, so we should'nt avearge over the full history of tarnsaction (id, timestamp be considered for averaging)


### Input Data
The first input dataset 'batch_log.json' entries are as follows:

{"D":"3", "T":"50"}

This data set is for parameter degree D : 3 i.e.; friend of a friend of a friend i.e.; 3rd degree reference. The parameter T
is the Tracked (Identified) purchases to be considered for this calculation. 

Few more lines of entry of 'batch_log.json' for a 3rd degree friend (analysis be considered for 50 flagged purchases for this data 
set) are as follows:

{"event_type": "purchase", "timestamp":"2017-06-13 11:33:01", "id": "1", "amount": "16.83"}

i.e.; $16.83 purchase was made at 11:33:01 on 2017-06-13. Important concern here "id": "1" i.e.; user id number be used for what ? 

Another entry such as 

{"event_type":"purchase", "timestamp":"2017-06-13 11:33:01", "id": "1", "amount": "59.28"}


{"event_type":"befriend", "timestamp":"2017-06-13 11:33:01", "id1": "1", "id2": "2"}

{"event_type":"befriend", "timestamp":"2017-06-13 11:33:01", "id1": "3", "id2": "1"}

i.e.; Followed by two consecutive purchases (purchase done at the same time) by customer 1, consecutively customer 1 and customer 2 became friend. Also customer 3 and customer 1 became friend. A consecutive 3rd purchase of $11.20 was made by customer 1.   

Another consecutive entry as follows:

{"event_type":"unfriend", "timestamp":"2017-06-13 11:33:01", "id1": "1", "id2": "3"}

Here customer 1 and customer 3 became unfriend. 

### Analysis

### Key Points:

Flagged purchases: 

### Steps

1. anomalousTimeStamps.py ranked the time stamps in terms of tarnsactions.
2. flaggedPurchase.py ranked the flagged purchases for each time staps and calculate their mean and sd.




