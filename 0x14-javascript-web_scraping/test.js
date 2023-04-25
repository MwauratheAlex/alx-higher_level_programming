#!/usr/bin/node

let jsonString = '{"name": "John", "age": 30, "city": "Nairobi"}'
let obj = JSON.parse(jsonString)

obj.name = "Mwaura"
obj.country = "Kenya"
obj.hobies = ["Cooking", "Eating", "Swimming"]
obj.hobies.push("Nitty Picking")
obj.hobies.splice(1, 1)

console.log(obj)
console.log(obj.name)
console.log(obj['age'])

let updatedJson = JSON.stringify(obj)
console.log(updatedJson)
