# Data Registry Service for Employee (or any) data

**Note** - In this scenario I had used employee data as a resource, but this may be modified to use any kind of data

## Usage

All responses will have the form 

```json
{
	"data": "Mixed type holdig the content of the response",
	"message": "Description of response"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all Employees

**Definition**

`GET /employees`

**Response**

- `200 OK` on success

```json
[
	{
		"identifier": "employee_001",
		"title": "Test Engineer 1"
		"name": "Mark Livingston",
		"age": "25",
		"address": "1538 Jacksonville Rd, Rochelle Park, NJ"
	},
	{
		"identifier": "employee_019",
		"title": "Junior Software Developer"
		"name": "Anthony Rodriguez",
		"age": "26",
		"address": "57 Sidney St, Clifton, NJ"
	}
]
```

### Registering a new Employee

**Definition**

`POST /employees`

**Arguments**

- `"identifier":string` a globally unique identifier for this employee
- `"title":string` the position title of the employee
- `"name":string` the name of the employee
- `"age":integer` the employee's current age
- `"address":string` where the employee lives

If an employee with the given identifier already exists, the existing employee will be overwritten.

**Response**

- `201 Created` on success

```json
{
	"identifier": "employee_001",
	"title": "Test Engineer 1"
	"name": "Mark Livingston",
	"age": "25",
	"address": "1538 Jacksonville Rd, Rochelle Park, NJ"
}
```

## Lookup employee details

`GET /employees/<identifier>`

**Response**

- `404 Not Found` if the employee does not exist
- `200 OK` on success

```json
{
	"identifier": "employee_001",
	"title": "Test Engineer 1"
	"name": "Mark Livingston",
	"age": "25",
	"address": "1538 Jacksonville Rd, Rochelle Park, NJ"
}
```

## Delete an employee

**Definition**

`DELETE /employees/<identifier>`

**Response**

- `404 Not Found` if the employee does not exist
- `204 No Content` on success