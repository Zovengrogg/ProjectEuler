:- use_module(library(odbc)).

connect(Connection) :-
    odbc_connect('ec2-3-227-60-139.compute-1.amazonaws.com', Connection,
                 [ user('captain'),
                   password('@eb8&86Tt0u$DP2'),
                   alias('dynamic_pricing_prod'),
                   open(once)
                 ]).

% Execute a SQL query
execute_query(Query, Rows) :-
    connect(Connection),
    odbc_query(Connection, Query, Rows).


% cp.ClientProductKey, 
% pf.SourceFeatureKey 
% FROM Dynamic_Pricing_Prod.sc.ClientProduct cp
% INNER JOIN Dynamic_Pricing_Prod.sc.ProductFeature pf
%     ON pf.ClientProductKey = cp.ClientProductKey
% WHERE cp.SourceCategoryKey = 6165
main :-
    execute_query(
        'SELECT TOP(10) * FROM sc.ClientProduct', Rows),
    writeln(Rows),
    halt.


