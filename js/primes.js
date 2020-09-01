function run(n) {
    var n = 1000000;
    var arr = [2];

    for ( var i = 3; i < n; i++ ) {
        var isPrime = true;
        for (var j = 0; j < arr.length; j++) {
            var p = arr[j];
            if (p * p > i) {
                break;
            }
            if (i % p == 0) {
                isPrime = false;
                break;
            }
        }
    }
}

run()
