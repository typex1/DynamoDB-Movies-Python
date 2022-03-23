# DynamoDB-Movies-Python

This repo is giving you all the needed Python files mentioned in the official AWS DynamoDB tutorial https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.01.html to enable you to get up to speed quickly. - You do not need to copy them from the web pages.

Some adaptions and comments from my side:

* In the code, I have commented out the local DynamoDB endpoint url "http://localhost:8000" to be able to do all actions directly in your account's DynamoDB
* I have added a shortened import data version **"movies_small.json"** containing only 10 instead of 4859 items in "movies.json" not to be overwhelmed by data in the table.
* You can change the above import file name in MoviesLoadData.py


Table "Movies" structure:

Partition Key 'year' (datatype Number) | Sort Key 'title' (String)| Attribute 'info' (Map)
--|--|--
2013|Prisoners|{ "actors" : { "L" : [ { "S" : "Hugh Jackman" }, ...
2014|X-Men: Days of Future Past|{ "actors" : { "L" : [ { "S" : "Jennifer Lawrence" }, ...

Here the Python files and some comments:

* MoviesCreateTable.py - creates the table with primary key consisting of: partition key 'year' (type Number) and sort key 'title' (String)
* MoviesLoadData.py - this setup only loads only 3 items as mentioned above
* MoviesQuery01.py - simple query based on the partition key (year) only
* MoviesQuery02.py - query using partition key (year) and a range expression for the sort key (title)
* MoviesItemOps01.py - simple put_item operation adding a new item
* MoviesItemOps02.py - get_item based on year and title
* MoviesItemOps03.py - simple update_item - be aware that updating a partition key or a sort key can only be done by deletion and re-creation (see **transaction** example below)
* MoviesItemOps04.py - update_item - updating a counter (atomic operation, see tutorial)
* MoviesItemOps05.py - update_item, (here: remove the first entry from the actor list in a map) but only under a certain condition. Very useful!
* MoviesItemOps06.py - delete_item
* MoviesScan.py - scan the table (full table scan, as opposed to query which is always based on the primary key) - not advisable when handling large data
* MoviesTransactWriteItems.py - this is not part of the origninal tutorial - a transaction of doing a put AND a delete as a **transaction**. If one of them fails, all is rolled back. Neat example because the syntax is somewhat complex.
* MoviesDeleteTable.py - be aware that there is no "do you really want to delete" request :-)


Hint regarding the **cleanness** of the dataset:

* Be aware that not all items carry the same amount of attributes. E.g. only in 4624 out of 4859 movie items you will find the attribute "info"
