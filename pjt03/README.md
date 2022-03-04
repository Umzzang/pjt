# 1. nav&footer

## 목표 

```
상단 고정, 로고 이미지 링크 설정, 네비게이션 바, 리스트 오른쪽 배치, 리스트 각 항목 링크 설정, 
Viewport 가로 크기에 따라 햄버거 버튼 교체, Login 항목 Modal 컴포넌트
```

## 어려운 부분

```
Viewport 가로 크기에 따라 햄버거 버튼 교체, Login 항목 Modal 컴포넌트
```



```html
<body>
  <!-- 01_nav_footer.html -->
  <nav class="navbar navbar-expand-md navbar-dark bg-black sticky-top">
    <div class="container-fluid d-flex justify-content-between align-items-center" >
      <a class="navbar-brand" href="02_home.html">
        <img src="images/logo.png" alt="" style="width: 120px;">    
      </a>
      <div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="02_home.html">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Login</a>
            </li>
          </ul>
        </div>
     </div>
    </div>
  </nav>
```

```markdown
* button 을 div 에 넣지 않고 실행하면 Home Commuity Login 이 끝으로 가지 않음
-> button 은 display가 none 으로 되어있어서 그런듯?
.me-auto {
	margin-right:auto;
}
.ms-auto {
	margin-left:auto;
}
??? mr ml 이랑 뭐가 다른가??

#햄버거
.collapse{
	display:none
}
.navbar-collapse{
	flex-basis: 100%;
    flex-grow: 1;
    align-items: center;
}
.navbar-expand- {
	flex-wrap: nowrap;
    justify-content: flex-start;
}
button 의 data-bs-target 값과
navbar-collapse 의 id 값 일치 시켜야 함.
flex-grow : 할당 받는 비율
https://developer.mozilla.org/ko/docs/Web/CSS/flex-grow

#모달 연결
<a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">

마지막에 modal 작성
data-bs-target 이랑 id 랑 연결

```



# 2. home

## 목표 

```
main 사진 변하게, 가로에 따라 section 변화
```

## 어려운 부분

```
main 사진 변하게
```



```html
<header>
    <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators pb-3">
        <button type="button" data-bs-target="#carouselExample" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExample" data-bs-slide-to="1" aria-label="Slide2"></button>
        <button type="button" data-bs-target="#carouselExample" data-bs-slide-to="2" aria-label="Slide3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="images/header1.jpg" alt="header"  class="d-block w-100">
        </div>
        <div class="carousel-item">
          <img src="images/header2.jpg" alt="header" class="d-block w-100">
        </div>
        <div class="carousel-item">
          <img src="images/header3.jpg" alt="header" class="d-block w-100">
        </div>
      </div>
    </div>
  </header>
```



```markdown
<div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
class에 slide 안 넣으면 효과 없이 변하기만 함.
slide는 효과인듯 ;; 검사로는 안나타나는데 어떻게 확인해야 하는거지?

<div class="carousel-item active">
active 는 item 중 하나에 넣어주어야 함.

container 설정 후에 row col 구분 정확하게 할 것.
```





# 3. community

## 목표 

```
container(list-group, table, article)
```

## 어려운 부분

```
table 사라지게 하기
```



```html
<ul class="list-group">
            <li class="list-unstyled"><a href="#" class="list-group-item text-primary">Boxoffice</a></li>
            <li class="list-unstyled"><a href="#" class="list-group-item text-primary">Movie</a></li>
            <li class="list-unstyled"><a href="#" class="list-group-item text-primary">Genres</a></li>
            <li class="list-unstyled"><a href="#" class="list-group-item text-primary">Actors</a></li>
    
    
<div class="d-none d-lg-block col-lg-12">
    
    
<ul class="pagination justify-content-center mb-5">
            <li class="page-item"><a class="text-primary page-link" href="#">Previous</a></li>
            <li class="page-item"><a class="text-primary page-link" href="#">1</a></li>
            <li class="page-item"><a class="text-primary page-link" href="#">2</a></li>
            <li class="page-item"><a class="text-primary page-link" href="#">3</a></li>
            <li class="page-item"><a class="text-primary page-link" href="#">Next</a></li>
```



```
list-group, pagination 사용하면 알아서 해줌.
table 사라지는 방법: d-none d-lg-block
                   lg 이상이면 블록으로  ->d-none 없이 col-0 해도 안사라짐.
                   
```





### 의문점

```
carousel-item 혹은 carousel-inner 이러한 다양한 클래스들을 어떻게 다외워야 하는지 모르겠다.
그 다양한 클래스들의 속성들도 외울 자신이 없다.
부트스트랩 사용하다 보면 css작성능력이 떨어질 듯..
03_community.html 에서 열었는데 home 도 동작을 함. 이유는 모르겠음.
```



### 주의

``` 
항상 부모 자식 관계를 잘 살펴야 할 것.
코드가 원하는 대로 안돌아가면 속성 잘 파악할 것.
```



### Tip

```html
div>table>(thead>tr>th*1td*3)*3

<div>
    <table>
        <thead>
            <tr>
                <th></th>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </thead>
        <thead>
            <tr>
                <th></th>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </thead>
        <thead>
            <tr>
                <th></th>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </thead>
    </table>
</div>

안되면 3 지웠다가 다시 작성

```

