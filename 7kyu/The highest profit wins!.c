// Story
// Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

// Task
// Write a function that returns both the minimum and maximum number of the given list/array.

void min_max (const int arr[/* count */], int count, int *min, int *max)
{
    *min = *max = arr[0]; // fix me!

    for (int i = 0; i < count; i++){
        *min = *min > arr[i] ? arr[i] : *min;
        *max = *max < arr[i] ? arr[i] : *max;
    }
    arr = *min;
}