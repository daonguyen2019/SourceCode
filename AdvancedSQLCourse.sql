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











