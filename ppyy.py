import pandas as pd
import numpy as np
import re 
import os

os.chdir("Please write your path")

#################################################################### Function 函数 #######################################################################
def tsrank(x):
    # A的末位值在过去n天的顺序排位
    tar = x[-1]
    return np.where(np.sort(x) == tar)[0][0]

def decaylinear(x):
    ## 对A序列计算移动加权平均，权重为i/sum(i)
    len_x = len(x)
    w_np = np.array([i for i in range(1, len_x+1)])
    return np.dot(x, w_np/w_np.sum())


def df_cmp(df1, df2, kind):
    ## dataframe比大小，含nan值的处理
    condition = (df1 <= df2)
    nan_part1 = np.isnan(df1)
    nan_part2 = np.isnan(df2)
    
    if kind.lower() == "max":
        diff_part_condition = ~(nan_part2 == ~(nan_part1 == nan_part2))
        df1[condition] = df2
        df1[diff_part_condition] = df2
        return df1
    else:
        diff_part_condition = ~(nan_part1 == ~(nan_part1 == nan_part2))
        df2[~condition] = df1
        df2[diff_part_condition] = df1
        return df2
    

def sma(x, df, n, m, memory):
    ## 递归
    if x == 1:
        memory[x] = df.iloc[0]  
    else:
        if x not in list(memory.keys()):
            memory[x] = (df.iloc[x-1]*m + sma(x-1, df.iloc[:x,:], 3, 1, memory)*(n-m))/n
    return memory[x]
  
    
############################################################ Factor 因子 #######################################################################
def alpha_90(volume, vwap):
    # (RANK(CORR(RANK(VWAP), RANK(VOLUME), 5)) * -1)
    return -volume.rank(axis=1, pct=True).rolling(5).corr(vwap.rank(axis=1, pct=True))

def alpha_91(close, low, volume):
    # ((RANK((CLOSE - MAX(CLOSE, 5)))*RANK(CORR((MEAN(VOLUME,40)), LOW, 5))) * -1)
    part1 = (close - close.rolling(5).max()).rank(axis=1, pct=True)
    part2 = (low.rolling(5).corr(volume.rolling(40).mean())).rank(axis=1, pct=True)
    return -part1*part2
    
def alpha_92(close, vwap, volume, w1, w2):
    # w1 = 3
    # w2 = 5
#     (MAX(RANK(DECAYLINEAR(DELTA(((CLOSE * 0.35) + (VWAP *0.65)), 2), 3)), 
#     TSRANK(DECAYLINEAR(ABS(CORR((MEAN(VOLUME,180)), CLOSE, 13)), 5), 15)) * -1)
    entity1 = close*0.35 + vwap*0.65
#     part1 = (entity1 - entity1.shift(2)).ewm(span=3, adjust=True).mean().rank(axis=1, pct=True)
    weight1 = np.array([i for i in range(1,w1+1)])
    part1 = (entity1 - entity1.shift(2)).rolling(w1).apply(decaylinear, raw=True)  # mean().rank(axis=1, pct=True)
    
    weight2 = np.array([i for i in range(1,w2+1)])
    entity2 = abs(close.rolling(13).corr(volume.rolling(180).mean()))
    part2 = entity2.rolling(w2).apply(decaylinear, raw=True).rolling(15).apply(tsrank, raw=True)
    
    alpha = df_cmp(part1, part2, kind="max")
    return alpha
    
def alpha_93(open_df, low):
    # SUM((OPEN>=DELAY(OPEN,1)?0:MAX((OPEN-LOW),(OPEN-DELAY(OPEN,1)))),20)
    
    alpha = open_df.copy()
    condition1 = (alpha > open_df.shift(1))
    alpha[condition1] = 0
    
    condition2 = ((open_df - low) > open_df-open_df.shift(1))
    result = df_cmp((open_df - low), open_df-open_df.shift(1), kind="max")
    alpha[~condition1] = result
    
    return alpha.rolling(20).sum()
    
def alpha_94(close, volume):
    # SUM((CLOSE>DELAY(CLOSE,1)?VOLUME:(CLOSE<DELAY(CLOSE,1)?-VOLUME:0)),30)
    condition1 = (close == close.shift(1))
    condition2 = (close < close.shift(1))
    volume[condition2] = -volume
    volume[condition1] = 0
    return volume.rolling(20).sum()

def alpha_95(amount):
#     STD(AMOUNT,20)
    return amount.rolling(20).std()

def alpha_96(close, low, high):
#     SMA(SMA((CLOSE-TSMIN(LOW,9))/(TSMAX(HIGH,9)-TSMIN(LOW,9))*100,3,1),3,1)
    entity1 = (close - low.rolling(9).min())/(high.rolling(9).min() - low.rolling(9).min())
    
    memory1 = {}
    sma(entity1.shape[0], entity1, 3, 1, memory1)
    entity2 = pd.DataFrame(memory1).T
    entity2.index = close.index
    
    memory2 = {}
    sma(entity2.shape[0], entity2, 3, 1, memory2)
    alpha = pd.DataFrame(memory2).T
    alpha.index = close.index
    return alpha


def alpha_97(volume):
    # STD(VOLUME,10)
    return volume.rolling(10).std()

def alpha_98(close):
    # ((((DELTA((SUM(CLOSE, 100) / 100), 100) / DELAY(CLOSE, 100)) < 0.05) || ((DELTA((SUM(CLOSE, 100) / 100), 100) / 
# DELAY(CLOSE, 100)) == 0.05)) ? (-1 * (CLOSE - TSMIN(CLOSE, 100))) : (-1 * DELTA(CLOSE, 3)))
    
    entity = close.rolling(100).mean()
    condition = ((entity - entity.shift(100))/entity.shift(100) <= 0.05)
    
    alpha = -(close - close.rolling(100).min())
    alpha[~condition] = -(close - close.shift(3))
    return alpha

def alpha_99(close, volume):
    # (-1 * RANK(COVIANCE(RANK(CLOSE), RANK(VOLUME), 5)))
    return -((close.rank(axis=1, pct=True).rolling(5).cov(volume.rank(axis=1, pct=True))).rank(axis=1, pct=True))

def alpha_100(volume):
    # STD(VOLUME,20)
    return volume.rolling(20).std()
