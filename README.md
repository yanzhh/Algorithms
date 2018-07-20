# Algorithms

## Sort
### insert-sort
* 使用增量方法，对子序列A[1..j-1]排序之后，将元素A[j]插入到子数组的合适位置，得到排好序的数组A[1..j].
### merge-sort
divide & conquier.    
              1. 将n个元素的序列分解为各n/2个元素的两个子序列   
              2. 递归的对两个子序列进行merge-sort       
              3. 合并两个已排序的子序列。   
              merge-sort的关键在于merge过程。
### quick-sort
divide & conquier.   
              1. 将序列A[p..r]划分成两个子数组（可能为空）A[p..q-1]和A[q+1..r]，使A[p..q-1]的元素都<= A[q], A[q+1..r]的元素都 >= A[q].   
                 PS: 这个过程中，将A[r]作为主元(pivot element)，小于主元的都放到主元左边，大于主元的放到主元右边，主元的位置就是排序结束后它所在的位置。   
              2. 递归地对两个子序列进行quick-sort排序。   
              3. 因为是in place排序，所以不需要合并
