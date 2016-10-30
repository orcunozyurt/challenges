/*Walrus Weights problem is a problem that can be solved with bounded knapsack
alghoritm.Aka.Knapsack0-1. In the typical problems,
items also have a profit value, unlike
walrusweights. Therefore, value of every item is equalized with the weight.

My attempt was to solve it dynamically.
Recursive programming will solve it too for less number of items. However when
the dataset gets larger, it will be extremely slow, or will exceed the maximum
recursion depth. Depends on the system. --> lots and lots of stack.(N)

"""
  knapsack function will try to solve a knapsack problem dynamically.
  given set of item properties(value,weight, limit, ItemCount) are iterated
  twice. one with limit = 1000. After getting
  result, second iteration with limit = result + (1000-result) * 2
  Second iteration is the key to decide between 998 and 1002
  """
*/

#include <algorithm>
#include <iostream>


int M[2000][2000];
int knapsack(int value[], int weight[], int C, int n)
{
  for(int i = 1; i <= C; i++){
    for(int j = 0; j <n; j++){
      if(j > 0){
        M[j][i] = M[j-1][i];
        if (weight[j] <= i)
          M[j][i] = std::max(M[j][i], M[j-1][i-weight[j]]+value[j]);
      }
      else{
        M[j][i] = 0;
        if(weight[j] <= i)
          M[j][i] = std::max(M[j][i], value[j]);
      }
    }
  }
  return M[n-1][C];
}

int main()
{
    int limit, N, first, second;
    std::cin >> N;
    limit=1000;
    int* value = new int[N+1];
    int* weight = new int[N+1];
    for ( int i = 0; i < N; i++) {
        std::cin>>weight[i];
        value[i] = weight[i];
    }

    first = knapsack(value,weight,limit,N);
    if (first == limit){
      std::cout<<first<<std::endl;
      return 0;
    }
    limit = first + (limit-first) * 2;
    second = knapsack(value,weight,limit,N);
    std::cout<<second<<std::endl;
    return 0;
}
