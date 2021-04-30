# morning_fast_api
fast api 연습

- https://fastapi.tiangolo.com/

## SQL (Relational) Databases
- https://fastapi.tiangolo.com/tutorial/sql-databases/

```bash
uvicorn main:app
```

### 파일 구조
```
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```

생각을 좀 해봐야 될 것 같음. config 설정의 경우 보통 DB의 config 설정을 따라가도록 되어 있을 것.
그럼 결국 database.py에서 config 설정을 불러와야 되고 해당 부분이 문제 없는지에 대한 부분은 판단이 필요할 것으로 보인다.
fastapi의 경우 DI를 손쉽게 지원해주고 있어, 좋은 것 같긴 한데. 내부 로직이 어떻게 돌아가는지 모르는 상태에서 이렇게 사용해도 문제 없는지에 대한 부분은 고려해 봐야 될 것으로 보인다.

env 설정의 경우. 개발 서버와 상용 서버를 구분할 수 있도록 처리.
DI의 경우 조금 더 확인 필요. lur_cache 부분도 확인 필요.