// Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

// Note: a and b are not ordered!

int get_sum(int a , int b) {
    return a > b ? sum(b,a):sum(a,b);
}

int sum(int min, int max){
    int sum = 0; 
    for (int i = min; i < max+1; i++) sum += i;
    return sum;
}