let d = (x,y) => 4900*y-1700*x

let binarySearch = function (n, start, end) {
    if (start > end) return false;

    let mid=Math.floor((start + end)/2);
    console.log(`4900*${mid}-1700*${n}=${d(n,mid)}`)
    if (d(n,mid)===24500) return true;
    if(d(n,mid)>24500)
        return binarySearch(n, start, mid-1);
    else
        return binarySearch(n, mid+1, end);
}
  

for(let i = 5000; i<= 10_000; i++){
    console.log(`-------------------${i}-------------------`)
    if(binarySearch(i, 0,i))
        break;
}
