| Function        | Arguments                        | Brute Force                    | Memoized                     | Tabulated                      |
|:---------------:|:--------------------------------:|:------------------------------:|:----------------------------:|:------------------------------:|
| fibonacci       | n(int)                           | Time: O(2^n)  Space: O(1)      | Time: O(n)  Space: O(n)      | Time: O(n)  Space: O(n)        |
| grid_traveller  | m(int)  n(int)                   | Time: O(2^(m+n))  Space: O(m+n)| Time: O(m*n)Space: O(m + n)  | Time: O(m*n)  Space: O(m*n)    | 
| can_sum         | m = target_sum  n = len(numbers) | Time: O(n^m)  Space: O(m)      | Time: O(m*n)  Space: O(m)    | Time: O(m*n)  Space: O(m)      |
| how_sum         | m = target_sum  n = len(numbers) | Time: O((n^m)*m)  Space: O(m)  | Time: O(n*m^2)  Space: O(m^2)| Time: O(m^2 * n)  Space: O(m^2)|
| best_sum        | m = target_sum  n = len(numbers) | Time: O((n^m)*m)  Space: O(m^2)| Time: O(n*m^2)  Space: O(m^2)| Time: O(m^2 * n)  Space: O(m^2)|
| can_construct   | m = target_sum  n = len(numbers) | Time: O((n^m)*m)  Space: O(m^2)| Time: O(n*m^2)  Space: O(m^2)| Time: O(m^2 * n)  Space: O(m)  |
| count_construct | m = target_sum  n = len(numbers) | Time: O((n^m)*m)  Space: O(m^2)| Time: O(n*m^2)  Space: O(m^2)| Time: O(m^2 * n)  Space: O(m)  |
| all_construct   | m = target_sum  n = len(numbers) | Time: O(n^m)  Space: O(m)      | Time: O(n^m)  Space: O(m)    | Time: O(n^m)  Space: O(n^m)    |

