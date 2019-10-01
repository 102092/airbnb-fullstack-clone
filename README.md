# airbnb-fullstack-clone

- visual studio code
- python3.x + django + tailwind..



### 설치

- pinenv사용.
  - 왜? `pip` 은 `install globally` 
  - 그래서 별로임.

```
pipenv --three
code .
//visual studio code에서
pipenv shell
//Launching subshell in virtual environment… 

pipenv install Django==2.2.5

```

- `pipenv shell` --> to inside in bubble.
  - 그다음에 `django` 프레임워크를 설치해야함!!(중요)



#### Django project

`python mange.py runserver`

you have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

- python에서 사용할 sql이 아직 migrate가 안된상태.



`makemigration`

- 데이터의 변경을 감지하는 명령어



`migrate`

- 데이터 베이스에 감지한 변경을 업데이트하는 명령어.



`python mange.py migrate`

- `db.sqlite3` 파일이 변경됨.
- 위 명령어를 통해, `makemigrate, migrate`를 동시에 실행하는 것과 같음.



#### Django Application

- groups of function
  - 만들고자 하는 프로젝트에서 얼마나 많은 group과 function이 있는가?
  - group?  == ex) rooms
  - function == application, .ex) search rooms, book the rooms...
    - 하나의 room 에 얼마나 많은 기능이 들어가는가? 그리고 모든 기능들을 room 폴더에 넣어야할까? 그러면 너무 많은 코드를 작성하는 게 아닌가?
    - 공통된 기능들을 하나에 모아두는게 좋지 않을까? -- > `config` 에 저장하자.

- 하나의 문장으로 표현할 수 있어야한다. 뭐를? rooms이라는 그룹안에는 예약하고, 리스트하고, 수정하고, 삭제하는 기능만 들어가있을것.

- `python mange.py startapp ...` 으로 app을 생성하고, 이렇게 생성된 폴더 안에 있는 .py파일 명은 수정하면 안됨. 
  - 왜? django가 migrate할 때, 해당 이름으로 찾기 때문에. 변경하면 찾을 수 가 없겠지?
- `model.py`
  - Database
- `view.py` 
  - 보이는 쪽
- config
  - `url.py`
  - url을 관리하는  py. `users` 폴더안에 새로 만들어서, 설정을 새롭게 해줄수 있음.