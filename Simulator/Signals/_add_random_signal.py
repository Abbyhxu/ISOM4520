import numpy as np

def add_random_signal(df_in, **params):

    '''
    This function adds a random signal to the dataframe.
    The signal is a random choice of 0, 1, or -1 with probabilities 0.4, 0.3,
    and 0.3 respectively. The trade opening price is the open price of the
    stock multiplied by 1 plus the signal multiplied by the slippage rate.

    Two new columns should be added to the dataframe:
    - signal: which gives the signal for the trade. 1 for long, -1 for short, 0 for no trade
    - trade_opening_price: which gives the price at which the trade is assumed to be opened

    Using the open price as the trade opening price is a good assumption because
    we are assuming that the trade is opened at the open price of the stock.

    Parameters
    ----------
    df_in : pd.DataFrame
        Input dataframe
    params : dict
        Dictionary of parameters
    
    Returns
    -------
    pd.DataFrame
        DataFrame with added signal and trade_opening_price columns
    '''

    df = df_in.copy()
    slippage_rate = params['slippage_rate']

    df['signal'] = np.random.choice([0, 1, -1], len(df), p=[0.4, 0.3, 0.3])
    df['trade_opening_price'] = df['Open'] * (1+ df['signal'] * slippage_rate)

    return df