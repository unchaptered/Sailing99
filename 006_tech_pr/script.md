# Technical Presentation

- 서론 
- 본론 
- 결론 

눈높이 : 코딩을 처음 하는 사람
목적 : 객체 리터럴에 대해서 그리고 구조분해 할당에 대해서

## Intro

- 인사 및 소개

    안녕하세요.
    이번 시간 발표를 맡게된 발표자 이민석 입니다.

- 발표 목적

    - `객체리터럴` `구조분해할당`
        - Why ?
        - What ?
        - How ?

## 객체 리터럴, object literal

### ✅ Why : 객체 리터럴을 왜 쓰는가.

- 본론에 앞서, 간단하게 맥락을 짚고 넘어가보도록 하겠습니다.

- 저희는 현재 개발자를 준비하면서 코딩을 처음 배우고 있는데요.

- 코딩이라는 행위가 아주 작게는 `함수` 를 통해서 목적을 달성하고 이 과정에서 많은 `변수` 들이 사용됩니다.

- 그런데 이러한 함수 사이에 `변수` 를 넘겨줄 때, 하나씩 넘겨주면 귀찮고 에러가 날 수 있으니 하나의 `묶음` 으로 사용 하자는 관점이 생겨났습니다.

- 그래서 이러한 변수의 묶음을 Object, 즉 `객체` 라고 부르게 되었습니다.

그렇다면 리터럴은 무엇을 의미할까요?

### ✅ What : 객체 리터럴이 무엇인가.

- 아주 생소한 단어겠지만, 놀랍게도 우리 모두가 이미 사용하고 있는 문법입니다.

- 어떤 변수에 문자열 혹은 숫자를 할당해보신 경험이 있으실 겁니다.

- 아래의 코드를 확인해주세요.

```javascript
const username = 'unchaptered';
const age = 27;
```

그렇다면 객체 리터럴이라는 것은 객체를 작성하는 어떤 약속일 것입니다.

```javascript
const user = {
    username: 'username',
    age: 27
}
```

역시나 배열 리터럴이라는 것도 존재하며, 다음과 같이 작성되어 있을 것입니다.

```javascript
const users = [ 'a', 'b', 'c' ];
```

### ✅ When/How : 객체 리터럴을 언제 쓰는가.

- When : 유저를 소개하는 값들을 묶음으로 넘겨줄때
- How : 객체 리터럴 표기법에 의해서 작성되고 식별자명을 통해 전달될 수 있을 것 같습니다.

```javascript
try_join();

function try_join() {

    const user = {
        username: 'unchaptered',
        age: 27
    }

    return act_join(user);

}
function act_join(user) {

    return user.age + '살의 ' + user.usrename + '님 반갑습니다.';

    // xx 살의 xxxxxx 님 반갑습니다.

}
```

## 구조분해할당, Destructuring

- 아마도 JavaScript 를 사용해보셨던 분이 아니라면 처음 듣는 문법일 거라고 생각합니다.

### ✅ Why : 구조 분해 할당을 왜 쓰는가

- 위에서 언급했던 유저 정보에 더욱 많은 값들이 들어있다고 가정해봅시다.

```javascript
const user = {
    username: 'unchaptered',
    email: 'unchaptered@gmail.com',
    password: 'hello',
    meta: {
        age: 27,
        phone: '010-0000-000',
        hobbies: [ 'a', 'b', 'c' ]
    }
}
```

- 그렇다면 이 변수들을 사용하려고 할 때, 가독성이 아주 안좋아질겁니다.

```javascript
user.username;
user.emial;
user.password;

user.meta.age;
user.meta.phone;
user.meta.hobbies;
```

- 또한 이러한 방식은 매우 불안정한 방식의 호출법입니다.

- 예를 들어, 서버 상에 문제로 meta 안이 텅 빈 객체가 되었다면 가정해보면, user.meta.age 를 호출하는 순간 에러가 발생하여 코드가 중단될 것입니다.

```javascript
const user = {
    /* 기존의 정보들 */
    meta: {}
}

user.meta.age; // Error!
```

- 하지만 지금부터 배울 구조분해할당은 이 문제들을 모두 해결할 수 있습니다.

### ✅ What : 구조분해할당이란 무엇인가.

- `구조`, `분해`, `할당`
    - 객체 구조분해할당
    - 배열 구조분해할당

#### 😀 먼저 객체 구조 분해 할당 부터 설명 드리도록 하겠습니다.

```javascript
try_join()

function try_join() {

    const user = {
        username: 'unchaptered',
        email: 'unchaptered@gmail.com',
        password: 'hello',
        meta: {
            age: 27,
            phone: '010-0000-000',
            hobbies: [ 'a', 'b', 'c' ]
        }
    }

    act_join(user);

}

function act_join(user) {

    const {
        username,
        meta: { age }
    } = user;

    return age + '살의' + username + '님 반갑습니다.'

}
```

- 만약에 username 과 age 만 사용한다면 다음과 같은 방식으로도 작성할 수 있습니다.

```javascript
function act_join({ username, meta: { age }}) {

    return age + '살의' + username + '님 반갑습니다.'

}
```

#### 😀 배열 구조분해할당 에 대해서 설명드리겠습니다.

```javascript
const users = [ 'a', 'b', 'c' ]

users[0]; // 1
users[1]; // 2
users[2]; // 3
```

- 위 중에 0번 항목만 필요할 때, 다음과 같은 사용 사례가 있습니다.

```javascript
const users = [ 'a', 'b', 'c' ];
const [ str, str2, str3 ] = users;

str     // a
str2    // b
str     // c
```

- 역시나 함수의 변수로 배열을 전달할 경우 배열 구조 분해할당을 적용할 수 있습니다.

```javascript
const users = [ 'a', 'b', 'c' ];
console_user(users);

function console_user([ str, str2, str3 ]) {

    return str + '님 환영합니다.';

}
```


### ✅ When : 구조분해할당을 언제 사용하는가.

- When : 거의 모든 순간에 사용될 수 있음을 알게되었습니다.
- How : 아주 편리하게 사용될 수 있습니다.

