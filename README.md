# Python_algorithm
Staircase_algorithm
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs or 3 stairs and so on  at a time. Count the number of ways, the person can reach the top.
ways(n) = ways(n-1) + ways(n-2) + ways(n-3).........................
in the above equation we chose according to required steps to take
for example : There are 5 stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs or 3 stairs and so on  at a time. Count the number of ways, the person can reach the top.
ways(5)=ways(5-1)+ways(5-2)+ways(5-3)   ;
ways(5-1)=ways(4-1)+ways(4-2).....
recursive it will solve with condition n-i >=0 (where i is the required steps taken at a time)
