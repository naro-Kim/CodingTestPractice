function solution(price, money, count) {
    const sum = count * (price + price*count) / 2
    return (money - sum) < 0 ? (money-sum)*-1 : 0
}