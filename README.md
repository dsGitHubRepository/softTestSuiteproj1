# Contents
1. [Objective](RAEDME.md#objective)
2. [Input Data](README.md#input-data)
3. [Analysis of the Input Data](README.md#Data-analysis)
4. [Interesting Features](README.md#features)
5. [Output Data](RAEDME.md#output-data)
6. [Summary](RAEDME.md#summary)



### Input DATA
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

i.e.; Followed by two consecutive purchases (purchase done at the same time) by customer 1, customer 1 and customer 2 became friend. Also customer 3 and customer 1 became friend. A consecutive 3rd purchase of $11.20 was made by customer 1.    


