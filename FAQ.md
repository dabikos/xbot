# FAQ - Часто задаваемые вопросы

## Общие вопросы

### Что это за проект?
Это современный одностраничный веб-сайт для образовательной платформы. Он включает все необходимые секции: главную страницу, информацию о платформе, каталог курсов, тарифы и форму обратной связи.

### Нужен ли мне хостинг?
Да, для публикации сайта в интернете нужен хостинг. Можно использовать бесплатные варианты (GitHub Pages, Netlify) или платный хостинг.

### Можно ли использовать этот сайт коммерчески?
Да, вы можете использовать и модифицировать этот сайт для любых целей.

## Технические вопросы

### Какие технологии использованы?
- HTML5 для структуры
- CSS3 для стилей
- Vanilla JavaScript для интерактивности
- Google Fonts для шрифтов

### Нужно ли устанавливать зависимости?
Нет, проект не требует установки зависимостей. Все работает на чистом HTML/CSS/JS.

### Как запустить локально?
```bash
# Вариант 1: Откройте index.html в браузере
# Вариант 2: Запустите Python сервер
python -m http.server 8000
```

### Какие браузеры поддерживаются?
Сайт работает во всех современных браузерах:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Адаптивен ли сайт?
Да, сайт полностью адаптивен и отлично выглядит на:
- Desktop (1280px+)
- Tablet (768px-1024px)
- Mobile (320px-767px)

## Настройка

### Как изменить цвета?
Откройте `styles.css` и найдите раздел `:root`:
```css
:root {
    --primary-color: #6366F1;  /* Измените на свой цвет */
}
```

### Как изменить логотип?
В `index.html` найдите класс `.logo` и замените SVG или добавьте свое изображение:
```html
<div class="logo">
    <img src="your-logo.png" alt="Logo">
    <span>Название</span>
</div>
```

### Как добавить свои курсы?
В `index.html` найдите `.courses-grid` и скопируйте блок `.course-card`, изменив содержимое.

### Как настроить форму обратной связи?
В `script.js` найдите функцию отправки формы и замените URL на адрес вашего API:
```javascript
const response = await fetch('https://your-api.com/contact', {
    method: 'POST',
    body: JSON.stringify(data)
});
```

### Как изменить шрифт?
1. Выберите шрифт на Google Fonts
2. Замените ссылку в `index.html`
3. Обновите `font-family` в `styles.css`

## Функциональность

### Работает ли форма без бэкенда?
По умолчанию форма имеет только фронтенд-валидацию. Для реальной отправки данных нужно подключить API или почтовый сервис.

### Как подключить реальную отправку писем?
Используйте сервисы:
- FormSpree
- EmailJS
- SendGrid
- Свой API

Пример с EmailJS доступен в `api-examples.js`.

### Можно ли добавить оплату?
Да, интегрируйте платежную систему:
- ЮKassa
- Stripe
- PayPal
- Робокасса

### Как добавить чат?
Подключите виджет чата перед закрывающим тегом `</body>`:
```html
<script>
  // Код виджета (Jivo, Tawk.to и т.д.)
</script>
```

### Есть ли поддержка нескольких языков?
Нет, но вы можете добавить её, создав версии для разных языков или используя i18n библиотеку.

## Развертывание

### Как опубликовать на GitHub Pages?
1. Загрузите код на GitHub
2. Settings → Pages
3. Выберите ветку main
4. Готово! Сайт будет доступен по адресу `username.github.io/repo-name`

### Как опубликовать на Netlify?
1. Перейдите на netlify.com
2. Перетащите папку проекта в Drop Zone
3. Или подключите GitHub репозиторий

### Нужно ли минифицировать файлы?
Для продакшена рекомендуется:
```bash
# CSS
npx cssnano styles.css styles.min.css

# JavaScript
npx terser script.js -o script.min.js
```

### Как настроить свой домен?
1. Купите домен у регистратора
2. Настройте DNS записи на ваш хостинг
3. Добавьте SSL сертификат (Let's Encrypt бесплатный)

## Производительность

### Как улучшить скорость загрузки?
1. Сжимайте изображения (TinyPNG, WebP)
2. Минифицируйте CSS/JS
3. Используйте CDN
4. Включите кэширование
5. Lazy loading для изображений

### Какой должен быть PageSpeed Score?
Целевые показатели:
- Performance: 90+
- Accessibility: 95+
- Best Practices: 90+
- SEO: 95+

### Как добавить кэширование?
Создайте файл `.htaccess` (для Apache):
```apache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
</IfModule>
```

## SEO

### Как улучшить SEO?
1. Заполните все meta-теги
2. Добавьте structured data (Schema.org)
3. Создайте sitemap.xml
4. Оптимизируйте изображения (alt теги)
5. Используйте семантические HTML теги

### Как добавить Google Analytics?
В `index.html` перед `</head>`:
```html
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

### Как создать sitemap.xml?
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://your-domain.ru/</loc>
    <lastmod>2024-01-01</lastmod>
    <priority>1.0</priority>
  </url>
</urlset>
```

## Безопасность

### Защищена ли форма от спама?
Добавьте Google reCAPTCHA:
```html
<script src="https://www.google.com/recaptcha/api.js"></script>
<div class="g-recaptcha" data-sitekey="your-site-key"></div>
```

### Как защититься от XSS?
- Валидируйте все входные данные
- Используйте Content Security Policy
- Санитизируйте данные перед вставкой в DOM

### Нужен ли HTTPS?
Да, обязательно используйте HTTPS для:
- Безопасности данных
- SEO (Google предпочитает HTTPS)
- Доверия пользователей

## Кастомизация

### Можно ли удалить секции?
Да, просто удалите соответствующий блок `<section>` из `index.html`.

### Как добавить новую секцию?
Скопируйте структуру существующей секции и измените содержимое:
```html
<section id="new-section" class="section">
    <div class="container">
        <!-- Ваш контент -->
    </div>
</section>
```

### Как изменить анимации?
В `styles.css` найдите `@keyframes` и измените параметры или создайте свои.

### Можно ли использовать другие шрифты?
Да, Google Fonts, Adobe Fonts или загрузите свои шрифты.

## Интеграция

### Как подключить базу данных?
Создайте бэкенд (Node.js, PHP, Python) и используйте примеры из `api-examples.js`.

### Как добавить систему регистрации?
1. Создайте бэкенд API
2. Используйте функции из `api-examples.js`
3. Добавьте страницы входа/регистрации

### Можно ли интегрировать с CMS?
Да, можно использовать как фронтенд для:
- WordPress (через REST API)
- Strapi
- Contentful
- Любой headless CMS

## Поддержка

### Где получить помощь?
1. Прочитайте документацию (README.md, CUSTOMIZATION.md)
2. Откройте DevTools (F12) и проверьте консоль
3. Поищите в Google/Stack Overflow
4. Создайте issue в GitHub

### Как сообщить об ошибке?
Создайте issue в GitHub с:
- Описанием проблемы
- Шагами для воспроизведения
- Скриншотами
- Версией браузера

### Можно ли получить коммерческую поддержку?
Это зависит от условий лицензии вашего проекта.

## Обновления

### Как обновить проект?
```bash
git pull origin main
```

### Как сделать резервную копию?
```bash
# Создать архив
tar -czf backup-$(date +%Y%m%d).tar.gz *

# Или используйте Git
git commit -am "Backup before update"
```

### Куда добавлять новые функции?
- HTML изменения → `index.html`
- Стили → `styles.css`
- Логика → `script.js`
- API → `api-examples.js`

---

**Не нашли ответ?** Создайте issue в репозитории или свяжитесь с поддержкой.
