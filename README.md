# farmcast
기후 요인이 농산물 도매가격에 미치는 영향 분석

기후 요소(기온, 강수량 등)가 주요 농산물(배추, 무 등)의 도매가격에 미치는 영향을 분석하고,  
머신러닝 회귀 모델을 통해 가격을 예측하는 Python 기반 데이터 분석 프로젝트입니다.

## 프로젝트 개요

- **주제**: 기후 변화와 농산물 가격 변동의 상관관계 분석 및 예측
- **데이터 출처**:
  - [KAMIS – 농산물유통정보](https://www.kamis.or.kr/customer/price/retail/period.do)
  - [기상청 날씨누리](https://data.kma.go.kr)
- **분석 품목**: 배추, 무 (확장 가능)
- **분석 단위**: 월별 기준

## 📁 프로젝트 구조
```
farmcast/
├── data/                  # 수집한 CSV 데이터
├── notebooks/             # Jupyter 분석 노트북
│   ├── 01_EDA.ipynb
│   ├── 02_Modeling.ipynb
│   └── 03_Visualization.ipynb
├── models/                # 학습된 모델 파일 (선택)
├── output/                # 시각화, 예측 결과 등
├── README.md
└── requirements.txt
```

## 🔍 사용 기술

| 분류 | 사용 도구 |
|------|-----------|
| 데이터 처리 | `pandas`, `numpy` |
| 시각화 | `matplotlib`, `seaborn`, `plotly` |
| 머신러닝 | `scikit-learn`, `xgboost` |
| 웹 대시보드 (선택) | `streamlit` |

## 주요 분석 내용

- 기후 요인별 가격 변화 경향 파악
- 상관관계 히트맵 분석
- 품목별 회귀 예측 모델 구축 (Linear, RF, XGBoost 등)
- 실제값 vs 예측값 시각화

## 향후 계획
- 시계열 예측 기법 추가 (Prophet, LSTM 등)
- 품목/지역 다변화
- Streamlit을 통한 웹 인터페이스 배포
