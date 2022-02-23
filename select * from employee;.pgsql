select * from employee;

select * from order_;

select * from order_content;

select * from product_dj;

select * from role_emp;

select * from price;

select * from product_foto;



insert into role_emp (
    name_role,
    description
) values (
    'стажер',
    'может создавать заказы'
), (
    'менеджер',
    'добавляет фото'
), (
    'старший менеджер',
    'меняет цены'
), (
    'руководитель',
    'админ права'
);

insert into product_dj (
    name_product,
    description,
    date_add,
    time_add
) values (
    'mac_pro 13',
    'еще нет на складе',
    current_date,
    current_time
);



insert into price (
    price,
    product_id
) values (
    100.00,
    1
);



insert into product_foto (
    url,

    product_id
) values (
    '//static/learn/prodject',

    2
);


select p.*, pr.price, f.url from product_dj as p
left join price as pr on p.id_product = pr.product_id
left join product_foto as f on p.id_product = f.product_id;


