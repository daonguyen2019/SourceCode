--------Data Cleaning & Manipulation
Coalesce(Expr1, Expr2, Expr3) --return first not null, order is important
NVL(Expr, replacement_str) --replace null value with a specific str

TRIM( [LEADING|TRAILING|BOTH] trim_character FROM trim_source)
LPAD(EXPRESSION, PADDED_LENGTH, PAD_CHARACTER) --pads the left side on an expression with a
							----specific set of characters until it reaches its padded length
RPAD(EXPRESSION, PADDED_LENGTH, PAD_CHARACTER)

GREATEST(EXPRESSION_1, EXPRESSION_2…EXPRESSION_N) --return greatest values
LEAST(EXPRESSION_1, EXPRESSION_2…EXPRESSION_N) --return least values

SELECT * FROM
( SELECT COL_1, COL_2.. COL_N FROM TABLE) 
PIVOT (AGG_FUNC(COL_N) FOR COL_N IN (LIST))

WINDOW_FUNCTION
	OVER(
	PARTITION BY ...
	ORDER BY ....
	WINDOW_FRAME
)
unbounded preceding : unbounded preceding and current row
N preceding : N preceding and current row
current row: current row
N following: current row and N following
unbounded following: current row and unbounded following

Range: 
	_actual numerical value range : 20 - 1= 19
	_range consider in the order clause
	
If Order by is specified, then the frame is RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
		--> Running total
If Order by is NOT specified, then the frame is ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING

 
LAG(expression, offset, [,default]) OVER(order_by_clause)
-->expression: this can be a field, it can also contain a built-in function but not another analytical function
-->offset: optional. This is the offset from the current row
-->default: default is the value to be returned if offset goes beyond the scope of the partition. It default to NULL
-->order by clause: LAG() must be used with an aorder by clause in the OVER clause in SQL
--> LAG return the value in previous rows
--> Example:
	lag(name) over (order by name)
	lag(name, 2) over (order by name)
	lag(name,2,'blank') over (order by name)

LEAD function is opposite with LAG
NTILE(number) OVER (order by clause)
--> example: 
		-->ntitle(3) over (order by population)
		-->ntitle(3) over (partition by region_id order by population)
NTH_VALUE(expression,n) OVER()
-->example:
		-->nth_value(name,2) over()
		-->nth_value(name,2) over(partition by region_id)
RANKING function
row_number() over (order by population) --> assign 1 and incremental for each row
rank() over (order by population) --> rank will skip the numbers if we have same numbers in ranking
dense_rank() over (order by population) --> rank will not skip the numbers if we have same numbers in ranking

DISTRIBUTION function
percent_rank() over (order_by_clause) --> (rank-1)/(total number of rows - 1)

cum_dist() over (order_by_clause) --> (num of rows <= current rows value/(total rows in partiton)

ORDER OF EXECUTION
	FROM
	JOIN
	WHERE
	GROUP BY
	HAVING 
	WINDOW
	SELECT
	ORDER BY
	LIMIT/FETCH/TOP





















