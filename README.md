# Contents
1. [Introduction: Political Fundraising](RAEDME.md#objective)
2. [Challenge Summary](README.md#challenge-summary)
3. [Details of the challenge](README.md#input-data)


### Introduction
Federal election commission regularly publishes campaign contributions. Though identifying individual donors in terms of their $ contributions are important but we will not do it since federal law phohibits that. As a data analyst we would rather identify lucrrative time and area for soliciting future donations for similar candidates.  

### Challenge Summary
Fom campaign contributions input files such as  cn.txt, cm.txt, ccl.txt; etc were chosen. From each entry only relevant field such as committee ID, zip code, transaction date, transaction amount and other ID was chosen to distill two ouput files such as 

1. medianvals-by-zip.txt
2. medianvals-by-date.txt

medianvals-by-zip: Presents a running median, total dollar amount and total number of contributions by recipient and zip codes.

medianvals-by-date: Presents calculated median, total dolalr amount and total number of contributions by recipient and date.

### Details of the challenge
From available data sets construct "itcont.txt" where each entry would contain information regarding campaign contribution that was made on a particular "date" from a donar to a political campaign, committee or other similar entity. 

We are primarily interested with

1.  donor ID  ( OTHER-ID )
2. donor zip code  ( ZIP-CODE )
3. $ amount contributed ( TRANSACTION-AMT )
4. date of transaction ( TRANSACTION-DT )
5. recipient ID  ( CMTE-ID )

