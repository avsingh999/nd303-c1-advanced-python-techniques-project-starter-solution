# Explore Close Approaches of Near-Earth Objects

In this project, you'll use Python - and the skills we've developed throughout this course - to search for and explore close approaches of near-Earth objects (NEOs), using data from NASA/JPL's Center for Near Earth Object Studies.

## Run & Install
```
create envirment
activate envirment
pip3 install -r requirement.txt

python3 main.py query --start-date 2020-01-01 --end-date 2020-12-31 --hazardous --min-diameter 0.25 --max-distance 0.1 --limit 5 --outfile results.json
```

## Overview

- Occurs on a given date.
- Occurs on or after a given start date.
- Occurs on or before a given end date.
- Approaches Earth at a distance of at least (or at most) X astronomical units.
- Approaches Earth at a relative velocity of at least (or at most) Y kilometers per second.
- Has a diameter that is at least as large as (or at least as small as) Z kilometers.
- Is marked by NASA as potentially hazardous (or not).

## Project Scaffolding

Upon starting, the project contains several files and folders to help you get up and running:

```
.
├── README.md       # This file.
├── main.py
├── models.py       # Task 1.
├── read.py         # Task 2a.
├── database.py     # Task 2b and Task 3b.
├── filters.py      # Task 3a and Task 3c.
├── write.py        # Task 4.
├── helpers.py
├── data
│   ├── neos.csv
│   └── cad.json
└── tests
    ├── test-neos-2020.csv
    ├── test-cad-2020.json
    ├── test_*.py
    ├── ...
    └── test_*.py
```

### Task 1:

- A `NearEarthObject` class, to represent the data for a single near-Earth object.

1.  Check if info is null/empty.
2. Check if info has required data is present or not if not then store None otherwise store value
3. IsBlank(string) function to check string is Blank or not
4. addCAD(approach)  function to add new cad to neo object.
5. NearEarthObject has variable designation, name, hazardous, diameter, approaches (list).

- A `CloseApproach` class, to represent the data for a single close approach of an NEO.
1. Get rquired data from ** info and store into CloseApproach class variable.
2. setNeo function is to set NearEarthObject class object function for that Approach.


### Task 2: Extract data from structures files into Python objects.
`extract.py`

- store all NearEarthObject object in neos list.
- store all CloseApproach obeject in approaches list.
- neos_id is map to store neos list element index with  NearEarthObject object designation.

`load_neos(....) function `

1. Read the request csv using csv python library with DictReader function.
2. Exract the required data from every row in csv file.
3. create Object from that exracted data and append that object into neos list.
4. update neos_id with designation and index of neos list.

`load_approaches(....) function `
1. Open requested json file using json python lib. and read the data.
2. json file fields are store in fields variable.
3. fileds name and index store with variable key map.
4. extract the required data fields using key and create CloseApproach object.
5. check if desingation of that object is present or not in neos_id map.
6. get that designation neo object from neos list using neos_id.
7. set Neo object to CloseApproach object and vice versa.
8. append that new CloseApproach object to approaches list.

### Task 3: Query close approaches with user-specified criteria.


#### Task 3a: Creating filters.

`filters.py`

1. Implement Date Class and write override get method of AttributeFilter.
2. return date type object of that requested approach.
3. Create Distance, Velocity, Hazardous, Diameter class and override get method and return required data for each class filter.

`create_filter_function(..)`
1. Create class Object for requested filter using operator and value.
2. append that created object to filters_map list.


#### Task 3b: Query the database of close approaches using user-specified criteria.

`database.py`
`get_neo_by_designation(..)`
1. return neo object for requested designation.

`get_neo_by_name(..)`
1. return neo object for requested name.

`query(...)`
1. Implement Query function for execute filters.
2.  every approach filter with reqeusted fillter and count.
3. if  approach is reutrn by after all filter class then append to result. 

#### Task 3c: Limit the results to at most some maximum number.
1. convert iterator to list and return that list for request n elements.
2. check if n is less than from iterator length.



### Task 4: Report the results.

- `write_to_csv`: Write a stream of `CloseApproach` objects to a specific CSV file.
1. create file with requested name and open it.
2. all requested filedsname store in variable and write header for that csv file.
3. create a new variable with name "row" and append that required data with map from results.
4. write every row in csv file.


- `write_to_json`: Write a stream of `CloseApproach` objects to a specific JSON file.
1. create file with requested name and open it.
2. intitalize dump_data list .
3. create a new map variable with data and add required data and append to dump_data list.
4. dump all dump_data data in json file.


### Results


```
$ python3 -m unittest
```
<img src="all_test.PNG">

```
 python3 -m unittest tests.test_query tests.test_limit
```

<img src="t2.PNG">

```
python3 -m unittest --verbose tests.test_query
```
<img src="t4.PNG">

```
python3 -m unittest --verbose tests.test_extract tests.test_database
```
<img src="t5.PNG">
