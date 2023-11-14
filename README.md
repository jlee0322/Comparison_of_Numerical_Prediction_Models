# 數值預測模型比較

## 專案概述

本project的目標是建構數值預測模型，並比較至少三種不同演算法的預測績效。將使用 scikit-learn中的三種演算法，包括 KNN、SVR、RandomForest，來建構預測模型。而資料集來自 UCI ML Repository。

## 專案任務

1. **演算法建模：**
   - 使用三種演算法建構數值預測模型。
   - 可考慮 KNN、SVR、RandomForest演算法。

2. **資料集選擇及處理：**
   - 第一個實驗使用 Adult 資料集，其中 adult.train.txt 當作訓練資料集，adult.test.txt 當作測試資料集，預測測試資料集中的 hours-per-week 欄位值。
   - 第二個實驗從 UCI ML Repository 中，挑選了Accelerometer資料集，其為一個純數值型態的資料集。

3. **特徵重要性分析：**
   - 使用 scikit-learn 的 feature_importance 計算特徵重要性。
   - 對欄位特徵進行篩選，比較特徵欄位刪減前後預測績效的差異。

4. **績效評估：**
   - 使用 MAE（Mean Absolute Error）、RMSE（Root Mean Squared Error）和 MAPE（Mean Absolute Percentage Error）等指標，比較不同演算法的預測績效。

## 專案成果

- 建立並比較三種演算法的數值預測模型。
- 分析資料集特性，進行適當的資料前處理。
- 以視覺化方式呈現特徵重要性。
- 比較特徵欄位刪減前後預測績效的差異。
- 專案報告，包括專案背景、方法、結果和未來工作建議。
