코딩 테스트에 유용한 파이썬 표준 라이브러리 정리

https://docs.python.org/ko/3/library/

## [내장 함수](https://docs.python.org/ko/3/library/functions.html)

- [abs()](https://docs.python.org/ko/3/library/functions.html#abs) : 절댓값 반환
- [min()](https://docs.python.org/ko/3/library/functions.html#min) : 최솟값 반환
- [max()](https://docs.python.org/ko/3/library/functions.html#max) : 최댓값 반환
- [round()](https://docs.python.org/ko/3/library/functions.html#round) : 반올림 결과 반환
- [eval()](https://docs.python.org/ko/3/library/functions.html#eval) : 문자열 수식을 계산한 결과 반환
- [sorted()](https://docs.python.org/ko/3/library/functions.html#sorted) : 정렬된 결과 반환
- [zip()](https://docs.python.org/ko/3/library/functions.html#zip) : 2개 이상의 iterable 객체들을 병렬로 순회하며, 같은 인덱스의 요소들을 묶어낸 새로운 튜플 객체 반환
- [ord()](https://docs.python.org/ko/3/library/functions.html#ord) : 유니코드 정수값 반환

## [itertools](https://docs.python.org/ko/3/library/itertools.html)

- [permutations()](https://docs.python.org/ko/3/library/itertools.html#itertools.permutations) : 순열
- [combinations()](https://docs.python.org/ko/3/library/itertools.html#itertools.combinations) : 조합
- [product()](https://docs.python.org/ko/3/library/itertools.html#itertools.product) : 중복 순열
- [combinations_with_replacement()](https://docs.python.org/ko/3/library/itertools.html#itertools.combinations_with_replacement) : 중복 조합

## [heapq](https://docs.python.org/ko/3/library/heapq.html)

- 최소 힙(Min Heap)
- 최대 힙(Max Heap)은 원소의 부호를 임시적으로 변경
- **`heappush`**(_heap_, *item*) : *item* 값을 *heap*으로 push
- **`heappop`**(_heap_) : *heap*에서 가장 작은 항목을 pop하고 반환
- **`heapify`**(_x_) : 리스트 *x*를 선형 시간으로 제자리에서 힙으로 변환

## [bisect](https://docs.python.org/ko/3/library/bisect.html)

- 이진 탐색 알고리즘 구현
- **`bisect_left`**(_a_, *x*, *lo=0*) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 반환
- **`bisect_right`**(_a_, *x*, *lo=0*) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 반환

## [collections](https://docs.python.org/ko/3/library/collections.html)

- [deque](https://docs.python.org/ko/3/library/collections.html#collections.deque) : 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너
  - **`append`**(_x_) : 오른쪽에 *x*를 추가
  - **`appendleft`**(_x_) : 왼쪽에 *x*를 추가
  - **`pop`**() : 오른쪽에서 요소를 제거하고 반환
  - **`popleft`**() : 왼쪽에서 요소를 제거하고 반환
- [Counter](https://docs.python.org/ko/3/library/collections.html#collections.Counter) : iterable 객체 내부의 원소가 몇 번 등장했는 지 세는 클래스

## [math](https://docs.python.org/ko/3/library/math.html)

- **`factorial`**(_x_) : *x* 계승(factorial)을 정수로 반환
- **`ceil`**(_x_) : *x*의 천장값(ceiling)을 반환
- **`floor`**(_x_) : *x*의 바닥값(floor)을 반환
- **`sqrt`**(_x_) : *x*의 제곱근을 반환
- **`exp`**(_x_) : *e*의 *x* 거듭제곱을 반환
- **`gcd`**(_integers_) : 지정된 정수 인자의 최대 공약수를 반환
- **`lcm`**(_integers_) : 지정된 정수 인자의 최소 공배수를 반환
- **pi :** 수학 상수 *π* = 3.141592…
- **e :** 수학 상수 *e* = 2.718281…
