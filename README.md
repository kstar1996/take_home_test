# Take home assignment

## 1. Tech Stack Used
* Python 3.7
* Flask 2.1.2 > Web framework
* UnitTest > For unit testing

## 2. Running instructions

You will need to install flask. You can run the server by using the following command:

```shell
$ python3 main.py
```

This starts a REST server listening on port `9090`. Everything is stored in memory and there
is no persistence, meaning restarting the server will clear everything.

## 3. REST API

We store the data as a dictionary and use the reference number as a key. The value is a nested dictionary where the name, birthday, phone number, and address are keys. It would be best to use a DB, but since it is a simple example, a dictionary was used.

### 3-1. GET /participant

You can get all participants by using the query string `?ref_num=all` and get a particular participant by using the query string `?ref_num={ref_num}`.
Returns the participant(s) in JSON.

Example:

```shell
$ curl -X GET localhost:9090/participant?ref_num=all
```

```shell
$ curl -X GET localhost:9090/participant?ref_num={ref_num}
```

### 3-2. POST /participant/add/<ref_num>

Creates a new participant and returns JSON for the created participant.

Example:

```shell
$ curl -X POST localhost:9090/participant/add/<ref_num> -d '{"name": "Claire", "date_of_birth": "960521", "phone_number": "+447975777666", "address": "UK"}' -H "Content-Type: application/json" 
```

### 3-3. POST /participant/update/<ref_num>

Updates a participant's details and returns the JSON of the updated participant.

Example:

```shell
$ curl -X POST localhost:9090/participant/update/<ref_num> -d '{"name": "Claire", "date_of_birth": "960521", "phone_number": "+821085749987", "address": "Seoul"}' -H "Content-Type: application/json" 
```

### 3-4. DELETE /participant/delete/<ref_num>

Deletes the participant, returning an empty JSON object.

Example:

```shell
$ curl -X DELETE localhost:9090/participant/delete/<ref_num>
```


