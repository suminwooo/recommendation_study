# 추천 알고리즘 정리
- 아래의 결과는 간단한 모델의 결과이며 파라미터 튜닝을 통해 충분한 성능 개선 가능
- 코드 정리 용도로 작성
- 대부분의 모델은 [링크](https://velog.io/@suminwooo/series/%EC%B6%94%EC%B2%9C%EC%8B%9C%EC%8A%A4%ED%85%9C)에 정리
- 참고할만한 링크 : https://github.com/amanjeetsahu/Recommender-Systems-Using-Python
- 프로젝트를 하기 위해 movielens 데이터로 간단히 모델 구현(일부 모델은 평가 기능X)


**++++++++++++++ 간단한 기본 코드 정리 ++++++++++++++**

## 01. 간단한 추천 시스템(기초 통계 활용)

- 랜덤으로 평점 예측 
    - mse :  3.729026180087267
    - rmse :  1.931068662706551
    
- 영화 평균 평점 입력한 예측
    - mse :  1.0589376409868596
    - rmse :  1.0290469576199424
    
- 유저 평균 평점 입력한 예측
    - mse :  0.8905889036428333
    - rmse :  0.9437101798978504
    
- Rule 기반 영화 평점 예측
    1. 유저의 영화 평균 평점과 영화의 장르를 활용하여, 장르별 평균 평점 계산
        - mse :  1.1251906030478547
        - rmse :  1.0607500191128232
    2. 평균 영화 평점을 normalize(min-max scale)해서 확인
        - mse :  1.120579096060227
        - rmse :  1.05857408624065
        
        
## 02. contents-based recommend system(corr)
- 단순 평점의 상관관계를 활용하여 유사한 영화추천(corrwith() 활용) -> RANK 표시

## 03. contents-based recommend system(TF-IDF 추천 알고리즘)
- 영화의 장르를 활용해 코사인 유사도를 활용한 예측
    - mse :  1.40606646706041
    - rmse :  1.1857767357561078
    
## 04. 이웃기반 협업필터링
- Neighborhood-based(코사인 유사도)을 활용한 협업필터링으로 예측
    - item-based 
        - RMSE: 1.6949489761800296
    - user-based
        - RMSE: 0.8145193961484049


## 05. 모델 기반 협업 필터링(Matrix Factorization)
- SVD 활용한 Matrix Factorization
    - RMSE : 0.9041
- ALS 활용한 Matrix Factorization
    - RMSE : 1.0065

## 06. Bayesian Personalized Ranking(BPR) 
- RNAK 표시 -> 실제 결과 나오도록 다시 해보기
- 참고 링크 : https://github.com/shah314/BPR , https://github.com/benfred/implicit

## 07. Neural Collaborative Filtering
- 뉴럴 네트워크를 활용한 협업 필터링(평점 예측)

## 08. Factorization Machine
- 피처 다양하게 추가 가능
- 1. 직접 구현하기 -> 링크활용해 다양한 방법해보기(링크O) ex. binary, regression, rank
- 2. 라이브러리
    - fastFM, xlearn의 경우 윈도우 지원XXX
    - libFM의 경우 윈도우 지원
    
    
## 09. Wide_Deep Learning
- 피처 다양하게 추가 가능
- 코드에는 torch로 훈련까지 구현만 해둔 상태
- tensorflow, torch 활용해 데이터에 맞게 코드 작성 필요(링크O)

## 10. DeepFM
- 피처 다양하게 추가 가능
- 코드에는 torch로 훈련까지 구현만 해둔 상태
- tensorflow, torch 활용해 데이터에 맞게 코드 작성 필요(링크O)


## 11. AutoEncoder
- Collaborative Filtering 활용한 기본 코드
- 피처 다양하게 추가 가능
- 코드에는 torch로 훈련까지 구현만 해둔 상태
- tensorflow, torch 활용해 데이터에 맞게 코드 작성 필요(링크O)


## 12. 텍스트 데이터 활용
- movielens 데이터 대신 아마존 데이터 활용


## 13. 이미지 데이터 활용
- movielens 데이터 대신 아마존 데이터 활용



**++++++++++++++ 추가 예정++++++++++++++**