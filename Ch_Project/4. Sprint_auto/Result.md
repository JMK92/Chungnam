# Sprint
## 주제 : 오픈 소스를 이용한 자율 주행 

![KakaoTalk_20210625_103348084](https://user-images.githubusercontent.com/81665620/123356825-5f49f500-d5a3-11eb-8f1b-b2500bc8e612.png)


## 결과 : 조작 버튼에 따른 주행 모드 변경 및 google assistant을 사용

### 보완 할 점 :  

 1. 긴급 정지의 버튼 수정
 2. 자율주행시 특정 각도에서 에러 생김 
     -> atan일 것이라고 추측 하여 atan2을 변경 하였더니 에러 증폭이 됨
 3. 현재 라이다 각도를 8등분으로 나누어 놓음 -> 360도로 나누는 작업
 4. 원인 모를 segementation fault 오류 -> blynk와 관련이 있을것으로 판단 => blynk와 작동시 blynk가 강제 접속 해제
 5. 오픈 소스의 collision detect 성능이 좋지 못함

#### 참조 : 
https://github.com/planxlabs/toheaven : 주행 소스 사용  
https://spiralmoon.tistory.com/entry/프로그래밍-이론-두-점-사이의-절대각도를-재는-atan2 [Spiral Moon's programming blog]  : atan, atan2 참조

