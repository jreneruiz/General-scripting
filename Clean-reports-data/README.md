# Clean-reports-data

Another python script that I made to facilitate the daily work.

- [Clean-reports-data](#clean-reports-data)
- [Problem description](#problem-description)
- [Restrictions](#restrictions)
- [Solution](#solution)
- [Personal comments](#personal-comments)

# Problem description

The MRP system that is managed in the organization where I worked allows you to download complex reports of the current situation in the organization, which are of great importance for decision making in real time, the problem lies in the processing of this information is very time consuming, as a reference a single report could pass 900k records plus for every 100 records you have 50 blank records and information of the parameters that were used to run the report, see below to see a reference of what I speak.

```
	Data statistics		Number of

	Records passed		"97,989,646"

Report with dummy data

User:		user-001
Date:		00/00/0000
Time:		 00:00:01


	material		description	id	… (n)

	907-mat-a		desc-a  	1	... (n)
	368-mat-b		desc-b  	2	... (n)

Report with dummy data

User:		user-001
Date:		00/00/0000
Time:		 00:00:01


	material		description	id	… (n)

	498-mat-c		desc-c  	3	... (n)
	682-mat-n		desc-n  	n	... (n)
```

# Restrictions

- Keep a single header
- Remove all junk information (blanks records and report parameters)

# Solution

Of the two reports that can be considered "heavy" in processing, with the first I noticed that each usable row began with a number [0-9]. The other report started with a tabulator space and the word "material". Then with two functions written in python for each report the line that is considered good is detected and written in the report, the rest is simply ignored.

# Personal comments
First time cleaning large amounts of information in a simple and fast way (I think)
