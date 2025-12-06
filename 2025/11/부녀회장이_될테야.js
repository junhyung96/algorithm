const fs = require('fs')

const [T, ...cases] = fs.readFileSync(0).toString().trim().split('\n').map(Number)

let dp = Array.from({length: 15}, () => Array.from({length: 15}, () => 0))

for (let i=1; i<=14; i++){
    dp[0][i] = i
}
for (let i=1; i<=14; i++){
    for (let j=1; j<=14; j++){
        for (let k=1; k<=j; k++){
            dp[i][j] += dp[i-1][k]
        }
    }
}

result = ""
for (let i=0; i<T; i++){
    result += dp[cases[2*i]][cases[2*i+1]] + '\n'
}

console.log(result)