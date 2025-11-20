const fs = require('fs')

const input = fs.readFileSync(0).toString().split(" ").map(Number)

let asc = true
let desc = true

for (let i=1; i<=8; i++){
    if (asc && i == input[i-1]){
        asc = true
    } else {
        asc = false
    }
    if (desc && 9-i == input[i-1]){
        desc = true
    } else {
        desc = false
    }
}

result = "mixed"

if (asc) {
    result = "ascending"
} else if (desc){
    result = "descending"
}

console.log(result)