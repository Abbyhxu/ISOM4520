from arch import arch_model


def _add_garch_forecasting(df, interval, **params):
    """
    Add GARCH forecasting results to the dataframe.
    """

    ##TODO: ASSIGNMENT #4 - Add GARCH forecasting here

    sholud_add_garch = params['should_add_garch']

    if not sholud_add_garch:
        return df

    df = df.copy()
    
    ## TODO: Add GARCH forecasting
    #add GARCH forecasting  
    model = arch_model(df['Close'], vol='Garch', p=1, q=1)
    model_fit = model.fit(disp='off')

    # make forecast
    forecast = model_fit.forecast(horizon=1258)
    df[f'stat_GARCH_forecast_{interval}'] = forecast.variance.values[-1, :]
    df[f'stat_GARCH_forecast_{interval}'] = df[f'stat_GARCH_forecast_{interval}'].shift(1)
    df[f'stat_GARCH_forecast_{interval}'] = df[f'stat_GARCH_forecast_{interval}'].fillna(method='bfill')


    #print(model_fit.summary())

    df = df.copy()
    return df