// Exercises XP

// Don’t forget to push on Github
// Exercise 1: Simple If/Else Statement
// Create 2 variables, x and y. Each of them has a different numeric value.
// Write an if/else statement that checks the biggest number.
// If x equals 5 and y equals 2, the program should display:

// x is the biggest number

// let x = 5
// let y = 2

// if (x > y){
//     console.log( x + "is Bigger than " + y)
// } else 
//     console.log( y + "won the amount of " +x);


// if (x===5 && y===2){
//     console.log(x +"is the biggest number");
// }








// Exercise 2: Chihuahua
// Create a variable newDog that is equal to the string “Chihuahua”.
// Check and display how many letters are in newDog.
// Display the newDog variable in uppercase and then in lowercase (no need to create new variables, just use 2 console.log).
// Check if the variable newDog equals to “Chihuahua”
// if it does, display ‘I love Chihuahua, it’s my favorite dog breed’
// else, console.log ‘I dont care, I prefer cats’
// 

// let newDog = "Chihuahua"

// let newDog1 = newDog.length

// console.log(newDog1)
// console.log(newDog.toLowerCase())
// console.log(newDog.toUpperCase())

// if (newDog === "Chihuahua"){
//     console.log("I love Chihuahua")
// }else
// console.log("I dont car, I prefer cats")



// Exercise 3: Even Or Not Even
// Ask a number to the user, and save it to a variable.
// Check if the variable is an even number
// If it is, display: “x is an even number’. Where x is the actual number of the user.
// If it isn’t, display “x is not an even number’. Where x is the actual number of the user
// 

// let num = prompt("Please give me a number here")

// if (num%2==0) {
//     console.log(num + "is an even number")
// } else 
// console.log(num +" isn't an even number - that's ODD lol")


// Exercise 4: Group Chat
// let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
// Using the array above, console.log the number of users in a group conversation based on the following rules:
// If there is no one, display “no one is online”.
// If there is 1 person, display “<name_user> is online”.
// If there are 2 people, display “<name_user1> and <name_user2> are online”.
// If there are n>2 people, display the first two names and add “and n-2 more are online”.
// For example, if there are 5 users, it should display:

// name_user1, name_user2 and 3 more are online


let users = ["lea123", "Princess45", "sheryl"]

let user = prompt("What's your name");

users.push(user);


if (users.length === 0) {
    console.log("there is no one online");
}
else if(users.length === 1) {
    console.log(users[0] + " is online");
}
else if(users.length === 2){
    console.log(users[0] + " and " + users[1] + " are logged in");
}
else if(users.length > 2) {
    console.log(users[0]+ ',' + users[1]+  " and" + (users.length -2)+ "more are online")
    }

