# Дипломный проект "Цифровая кафедра при МГТУ"
<div>
<img src="https://img.shields.io/badge/framework-Django-blue.svg" alt="Python Language"> <img src="https://img.shields.io/badge/language-HTML-yellow.svg" alt="HTML Language">  <img src="https://img.shields.io/badge/language-CSS-ff69b4.svg" alt="CSS Language"> <img src="https://img.shields.io/badge/deploy-Docker-blue.svg" alt="Docker">
</div>

Deploy: http://45.8.250.50

### Запуск сайта:
```docker
docker-compose build
docker-compose up -d
```

### Про сайт:
Простой сайт, реализованный на Django. Вёрстка на шаблоннах.

#### Меню:
- Все посты отсортированные по времени публикации. Автор поста может отредактировать или удалить пост. Авторизованные пользователи могут оставить свой комментарий на пост и удалить его(комментарий). У поста есть теги, при нажатии на которые можно увидеть все посты с этими же тегами.
- Авторизованные пользователи. Можно перейти на некий профиль автора, где считается кол-во его постов, ответов и все его посты.
- Создание поста.
- Редактирование профиля (смена имени, фамилии, username, аватарки)
- Поиск по заголовку.

### TODO:
- [ ] CI/CD
- [ ] Редактирование постов
- [ ] Возможность ответа на ответ
- [X] Диплой
- [X] Docker/Docker-compose
- [X] Авторизация, аутентификация 
- [X] Пагинация
- [ ] Лабуда с отчётами и тд