Question 1 filename.py

Ensure that the users.csv file is in the same folder as the code
To execute the code in terminal run python filename.py users.csv

Question 2 weather.py

Ensure that the file weather.dat is in the same folder as the code
To execute the code in terminal run python weather.py

Question 3 main.py

How to run the program
To execute the code in terminal run python main.py

The program shall run on port 7777, if this port is in use change the port number on the last line of main.py to a free port

Test by using postman

After calling python main.py
Open postman to test the different cases:

1. Creating and updating the capacity size:
Through the POST route "http://127.0.0.1:7777/num" where num is any postive integer that you can input a queue of capacity "num" will be created,
The same route can be used to update the capacity.
A JSON response showing the numbers in the queue and the capacity will be shown

2. Addition of an element
Through the POST "http://127.0.0.1:7777/add/num" route where num is integer you can put, num will be added to the queue.
If the queue size is equal to the capacity, then a "Queue is full" error will be shown in the terminal 
A JSON response showing the numbers in the queue and the capacity will be shown.


3. Deletion of an element
Through the DELETE "http://127.0.0.1:7777/delete" route , num will be deleted from the queue.
If the queue is empty , then a "Queue is empty" error will be shown in the terminal 
A JSON response showing the numbers in the queue.

4. Get the number of sorted Items
Through the GET "http://127.0.0.1:7777/numSorted" route , number of sorted items in the list will be shown.

5. Geting the Queue :
Through the GET route "http://127.0.0.1:7777" the Queue can be retrived,
A JSON response showing the numbers in the queue and the capacity will be shown
