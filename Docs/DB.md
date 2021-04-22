# 데이터베이스

데이터베이스 관련 페이지

## Postgresql
- https://www.postgresql.org/
- 5432, 123456


## 테이블 생성

```
create databsae test;
create table users (
    id,
    email,
    hashed_password
    is_active
);
create table items (
    id,
    title,
    description,
    owner_id
);
```

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


```
CREATE TABLE so_headers (
  id SERIAL NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE so_items (
  item_id INTEGER NOT NULL, 
  so_id int4 REFERENCES so_headers(id) ON DELETE cascade,
  -- 이렇게 설정하면 서로 연결된 데이터는 수정/삭제가 자동으로 이루어진다.
  -- cascade 대신 다른 옵션을 설정할 수도 있다. 다른 옵션에대한 설명은 아래 설명을 참고해주세요.
  product_id INTEGER,
  qty INTEGER,
  net_price numeric,
  PRIMARY KEY (item_id,so_id)
);
```


## 외래키 설정

1. RESTRICT : 개체를 변경/삭제할 때 다른 개체가 변경/삭제할 개체를 참조하고 있을 경우 변경/삭제가 취소됩니다.(제한)
2. CASCADE : 개체를 변경/삭제할 때 다른 개체가 변경/삭제할 개체를 참조하고 있을 경우 함께 변경/삭제됩니다.
3. NO ACTION : MYSQL에서는 RESTRICT와 동일합니다.
4. SET NULL : 개체를 변경/삭제할 때 다른 개체가 변경/삭제할 개체를 참조하고 있을 경우 참조하고 있는 값은 NULL로 세팅됩니다.

CASECADE로 설장한 테이블을 삭제 했는데 삭제가 되지 않고 있음 -> 설정 자체를 잘 못 한게 아닌가 싶음

