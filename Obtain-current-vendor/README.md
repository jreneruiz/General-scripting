# Obtain-current-vendor
With this script it was possible obtain useful key information to decision making in the organization where this was implemented.
- [Obtain-current-vendor](#obtain-current-vendor)
- [Problem description](#problem-description)
- [Restrictions](#restrictions)
- [Solution](#solution)
- [Personal comments](#personal-comments)

# Problem description
As a supply chain analyst you work with a lot of data and information relations. One of the first challenge that I faced is get from all the raw materials the last vendor that provide the material.

The information can be requested from the MRP system that the organization utilize but only give you the raw material in purchase orders. Just to put you in context in purchase orders are like ~12k raw materials but in total we have like ~70k raw materials purchased.

Fortunately, there is a record of purchase requisition per week since 2008 to date (07/2018) the information is standarized in csv files, they contain the same number of colums and in each file the columns have the same name.

# Restrictions
- Get only information required not the whole scope of data
    - Material
    - Vendor code
    - Vendor name
- Process the information quickly, this are running weekly and each week are more files

# Solution
Python script that run weekly when a new file of purchase requisitions is detected, pandas is really convenient to read each csv file and concatenate the information in order to create a single file.

# Personal comments
This script made me a headache spesifically with the processing of dates.

The files have a column named PO Date, this column is used to determine when was put it the purchase order and who is the last vendor of the raw material.

They have dates with this format: 01/01/1900 (month/day/year), at the moment of trying to sort dates without formating they sort the dataset with dates 01 to 12 without caring the day or year. e.g. with a dataset like this:

Without po date sort:

mat      | mat desc  | po date    | vendor    | id
----     | ----      | ----       | ----      | ----
abc-mat  | desc A    | 01/20/2008 | SA vendor | 1
efg-mat  | desc B    | 12/31/2014 | CC vendor | 2
efg-mat  | desc B    | 08/01/2017 | PP vendor | 3
efg-mat  | desc B    | 11/01/2008 | SA vendor | 4

With po date sort (wrong way):

mat      | mat desc  | po date    | vendor    | id
----     | ----      | ----       | ----      | ----
abc-mat  | desc A    | 01/20/2008 | SA vendor | 1
efg-mat  | desc B    | 08/01/2017 | PP vendor | 3
efg-mat  | desc B    | 11/01/2008 | SA vendor | 4
efg-mat  | desc B    | 12/31/2014 | CC vendor | 2

After converting the whole column with the **to_datetime** function finally we can get the correct result:

With po date sort (correct way):

mat      | mat desc  | po date    | vendor    | id
----     | ----      | ----       | ----      | ----
abc-mat  | desc A    | 2008-01-20 | SA vendor | 1
efg-mat  | desc B    | 2008-11-01 | SA vendor | 4
efg-mat  | desc B    | 2014-12-31 | CC vendor | 2
efg-mat  | desc B    | 2017-08-01 | PP vendor | 3

Probably you're thinking that this is something of newbie's, but at least I didn't know after a few tries and a google search. Yep, this is what I learned with this.