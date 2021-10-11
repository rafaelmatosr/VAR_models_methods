

from statsmodels.tsa.stattools import adfuller


#Augmented Dickey-Fuller test
def adf_test(series, signif=0.05, name='', verbose=False):
    t = adfuller(series, autolag='AIC')
    result = {'test_statistic':round(t[0], 4), 'pvalue':round(t[1], 4), 'n_lags':round(t[2], 4), 'n_obs':t[3]}
    p_value = result['pvalue'] 
    def adjust(val, length= 6): return str(val).ljust(length)

    # Print Summary
    print(f'    Augmented Dickey-Fuller test for "{name}"', "\n   ", '-'*47)
    print(f' Null Hypothesis: Data has unit root (non-Stationary)')
    print(f' Significance Level    = {signif}')
    print(f' Test Statistic        = {result["test_statistic"]}')
    print(f' No. Lags Chosen       = {result["n_lags"]}')

    for item,value in t[4].items():
        print(f' Critical value {adjust(item)} = {round(value, 3)}')

    if p_value <= signif:
        print(f" => P-Value = {p_value}. Null hypothesis rejected (stationary series).")
    else:
        print(f" => P-Value = {p_value}. Could not reject the null hypothesis(non-stationary series).")     

#Aplication to each column
for name, column in df_train.iteritems():
    adf_test(column, name=column.name)
    print('\n')
