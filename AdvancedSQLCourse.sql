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

 




















