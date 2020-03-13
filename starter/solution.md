#Solutions
### Task 1
```model.py```
1. first initialize variable  id, diameter, name, is_potentially_hazardous_asteroid, orbits  NearEarthObject constructor (__init__) .
2. update orbits function update orbits of neo like append the data in orbits variable which is initialized by the constructor
3. In class OrbitPath initialize variable with value of neo data,  variable neo_name, miss_distance_kilometers, close_aproach_Date

###Task 2
```database.py```
1. First initialize variable like filename, NearEarthObjects, OrbitPaths in the constructor
2. In load data function to read the file using CSV lib of python.
3. Run for loop and get data line by line from CSV
4. create NearEarthObject and OrbitPath object while reading the data line by line

###Task 3
```search.py```
1. Initialize some variable in Query class constructor number, date, start_date, end_date, filters, return_objects
2. build_query function create date_serach namedtuple according to date search if exact date search then equal, DateSearch nametuple otherwise between date_serach namedtuple create
3. lastly create Selectors namedtuple and return this created Selector namedtuple
4. In filter, class add Options like diameter, distance, is_hazardous. and add operators like greater than, equal, greaterthenequal
5.in constructor initialize all variable which is a parameter of constructor
6.and create_filter_options method create defaultdict variable where I store NEO, and ORB data like if the diameter or is_hazardous is given in filter then append in NEO default dict if the distance is given then I append data in ORB where (ORB, NEO is key in defaultDict) and return default dict from this function
7. In the apply method, I filtered the data using filter options and return resulted data
8. In NEOSearcher class  I create two method equal_serach and between the search for search data by date and call function according to the user query and return resulted data

###Task 4
```writer.py```
1. There are two types of the show resulted data 1st is displayed on terminal 2nd one is write in CSV file
2. for first I simply run the for loop and convert each line convert to __dict__ and print.
3 for 2nd create otput.csv file and write the data line by line in CSV file
