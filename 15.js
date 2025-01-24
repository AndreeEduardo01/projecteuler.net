
/**
 * Return factorial of a number (num!) )
 * @param {integer} num The number to get Factorial
 */
function getFactorial(num) {
    var number = 1;
    for (var i = 2 ; i <= num ; i++)
        number = (number * i)
    return number;
}

/**
 * 
 * @param {integer} n Number of total observations
 * @param {integer} k Number of Selected Items
 * @returns 
 */
function getCombinations(n,k) {
    combinatory = getFactorial(n) / (getFactorial(k) * getFactorial(n-k));
    return combinatory;
}

answer = getCombinations(40,20)

console.log(answer)
