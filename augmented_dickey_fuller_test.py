

from statsmodels.tsa.stattools import adfuller


#Augmented Dickey-Fuller test
def adf_test(series, signif=0.05, name='', verbose=False):
    t = adfuller(series, autolag='AIC')
    result = {'test_statistic':round(t[0], 4), 'pvalue':round(t[1], 4), 'n_lags':round(t[2], 4), 'n_obs':t[3]}
    p_value = result['pvalue'] 
    def aux(value, length= 6): 
        return str(value).ljust(length)

    #Summarize
    print(f'    Augmented Dickey-Fuller test for "{name}"', "\n   ", '-'*47)
    print(f' Null hypothesis: Data has unit root (non-stationary)')
    print(f' Significance level    = {signif}')
    print(f' Test statistic        = {result["test_statistic"]}')
    print(f' Number of lags chosen       = {result["n_lags"]}')

    for item,value in t[4].items():
        print(f' Critical value {aux(item)} = {round(value, 3)}')

    if p_value <= signif:
        print(f" => P-Value = {p_value}. Null hypothesis rejected (stationary series).")
    else:
        print(f" => P-Value = {p_value}. Could not reject the null hypothesis(non-stationary series).")     

