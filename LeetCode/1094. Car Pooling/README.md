<h1><a href="https://leetcode.com/problems/car-pooling">1094. Car Pooling</a></h1>

There is a car with <code>capacity</code> empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer <code>capacity</code> and an array <code>trips</code> where <code>trips[i] = [numPassengersi, fromi, toi]</code> indicates that the <code>i<sup>th</sup><code> trip has <code>numPassengersi</code> passengers and the locations to pick them up and drop them off are <code>fromi</code> and <code>toi</code> respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return <code>true</code> <em>if it is possible to pick up and drop off all passengers for all the given trips, or <code>false</code> otherwise.</em>

## Example 1:

<strong>Input:</strong> trips = [[2,1,5],[3,3,7]], capacity = 4
<strong>Output:</strong> false
## Example 2:

<strong>Input:</strong> trips = [[2,1,5],[3,3,7]], capacity = 5
<strong>Output:</strong> true

## Constraints:

- <code>1 <= trips.length <= 1000</code>
- <code>trips[i].length == 3</code>
- <code>1 <= numPassengersi <= 100</code>
- <code>0 <= fromi < toi <= 1000</code>
- <code>1 <= capacity <= 105</code>
