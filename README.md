# 구성이 알찬 팀 기획서
  

## 프로젝트 구성 안내

 
## 1. 프로젝트 소개

사용자가 질병, 통증, 병원 관련한 수화를 배우고, 직접 시연을 통해 학습하는 서비스

- 사용 기술 스택 (Next.js, Django, Python, )



  

## 2. 프로젝트 기획 의도


처음 주제는 청각 장애 어린이 대상으로 수화를 교육하는 것이었으나 
데이터의 범위를 구체화할 필요성을 느껴 서비스 타겟층을 수정하였음.
후천적 요인으로 인해 급하게 수화를 익혀야 되는 사람들(당사자, 당사자의 주변인)에게는 가장 우선적으로 익혀야 할 표현이 건강 상태에 관한 표현임
또한 청각 장애 환자가 의료 기관을 이용하는 경우 의료진과의 소통이 제대로 이뤄지지 않아 중요한 정보를 놓치거나 잘못 전달될 경우가 있어 이러한 경우들을 해결하기 위해 서비스를 기획

## 3. 서비스 주요 기능 설명

  



- 학습된 모델을 이용하여 사용자의 수화 동작을 분석하여 표현하고자 하는 단어와 비교

- 수화 교육 서비스는 대부분 영상이나 이미지 자료 제공으로 그치는데 비해 우리 서비스는 학습된 모델로 사용자의 동작을 교정해주기 때문에 보다 효과적인 학습을 제공

  

## 4. 프로젝트 구성도

- https://www.figma.com/file/Y6gO9S5HQy6o8CboeJMJSh/Untitled?node-id=0%3A1<br>
- https://www.figma.com/file/OensWKNd4JQh1LLIYR9kkx/Untitled?node-id=0%3A1

  


## 5. 프로젝트 팀원 역할 분담

| 이름 | 담당 업무 |
|--|--|
| 김인기 | 팀장/백엔드 개발 / 인공지능 개발|
| 류진식 | 프론트엔드 개발 |
| 노영훈 | 백엔드 개발 / 인공지능 개발 |
| 김채원 | 백엔드 개발 / 프론트엔드 개발|
| 전소희 | 인공지능 개발 |
| 김세현 | 인공지능 개발 |

  

**멤버별 responsibility**

  

1. 김인기: 팀장/백엔드 담당

  

- 기획 단계: 구체적인 설계와 지표에 따른 프로젝트 제안서 작성

- 개발 단계: 팀원간의 일정 등 조율 + 프론트 or 백엔드 or 인공지능 개발

- 수정 단계: 기획, 스크럼 진행, 코치님 피드백 반영해서 수정, 발표 준비

  

2. 김채원,  김인기, 노영훈: 백엔드 담당

  

- 기획 단계: 큰 주제에서 문제 해결 아이디어 도출, 와이어프레임 작성

- 개발 단계: 와이어프레임을 기반으로 API 및 데이터베이스 완성

- 수정 단계: 피드백 반영해서 백엔드 설계 수정

  

3. 김세현, 전소희: 인공지능 담당

  

- 기획 단계: 큰 주제에서 문제 해결 아이디어 도출, 와이어프레임 작성

- 개발 단계: 와이어프레임을 기반으로 인공지능 모델 구현, 모델 학습 진행

- 수정 단계: 피드백 반영해서 모델 정확도 향상


3. 류진식:  프론트 엔드 담당

  

- 기획 단계: 큰 주제에서 문제 해결 아이디어 도출, 와이어프레임 작성

- 개발 단계: 와이어프레임을 기반으로 웹 페이지 디자인 구체화
- 수정 단계: 코치님 피드백 반영하여 프론트 유지 보수


## 6. GitLab 규칙

- master : 최종본
- sprint : 테스트 브랜치
- feature : 기능 브랜치
- fix : 수정 브랜치

- [GitLab사용법](docs/GitDocs.md)
