# 專案概述

本專案旨在建構數值預測模型，並比較不同演算法在不同資料集上的預測績效。採用三種不同的演算法，包括KNN、SVR、RandomForest，以應對多樣性的資料型態和特性。

## 實驗設計

### 資料集

1. **Adult 資料集：**
   - 訓練資料集：使用 `adult.train.txt`
   - 測試資料集：使用 `adult.test.txt`
   - 目標預測值：`hours-per-week` 欄位值

2. **第二個實驗資料集：**
   - 從 UCI ML Repository 中挑選一個純數值型態的資料集
   - 在此選擇accelerometer資料集

### 演算法選擇

使用三種演算法建構數值預測模型：
- KNN
- SVR
- RandomForest

### 特徵工程

利用 scikit-learn 的 `feature_importance` 功能計算特徵重要性，對欄位進行篩選。比較特徵欄位刪減前後模型績效之差異。

## 績效評估指標

使用以下績效指標進行評估：
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

## 期望結果

透過本專案的實驗比較，預期能夠獲得以下結果：

1. **演算法比較：** 對於不同資料集，比較KNN、SVR、RandomForest等三種演算法的預測效能，以確定在特定情境下最適用的模型。

2. **特徵工程影響：** 透過特徵重要性的計算，評估模型在特徵欄位刪減前後的表現差異。期望了解哪些特徵對於預測結果最具影響力。

3. **績效評估：** 使用MAE、RMSE和MAPE等指標綜合評估模型的預測準確性，提供對模型績效全面的了解。


