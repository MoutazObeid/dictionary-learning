
company_employees ={
    "Engineering" :{
        "alice" : {
            "age":30,
            "role": "Software Engineer"
        },
         "bob": {
            "age":28,
            "role": "DevOps Engineer"
        }
    },
    "HR" :{
    "Charlie":{
    "age":35,
    "role": "HR Manager"
                }

    }
}
print(company_employees)

company_employees["Engineering"]["David"] = {"age": 27, "role": "Data Scientist"}

print(company_employees)