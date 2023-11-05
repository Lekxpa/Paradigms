<!-- % Написать программу на языке Prolog для вычисления суммы 
% элементов списка. На вход подаётся целочисленный массив. 
% На выходе - сумма элементов массива. -->


sum_elements([], 0).
sum_elements([X|T], Sum_el) :- 
    sum_elements(T, Sum1), Sum_el is Sum1 + X.

?- sum_elements([1,2,3,4,5,6,7,8], Sum_el), write(Sum_el).