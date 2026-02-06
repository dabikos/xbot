# Руководство по настройке

## Изменение цветовой схемы

Откройте `styles.css` и измените переменные в разделе `:root`:

```css
:root {
    --primary-color: #6366F1;      /* Основной цвет */
    --secondary-color: #8B5CF6;    /* Вторичный цвет */
    --accent-color: #EC4899;       /* Акцентный цвет */
    --success-color: #10B981;      /* Цвет успеха */
    /* ... остальные переменные ... */
}
```

### Готовые цветовые схемы

#### Синяя схема
```css
--primary-color: #3B82F6;
--secondary-color: #06B6D4;
--accent-color: #8B5CF6;
```

#### Зелёная схема
```css
--primary-color: #10B981;
--secondary-color: #059669;
--accent-color: #14B8A6;
```

#### Оранжевая схема
```css
--primary-color: #F59E0B;
--secondary-color: #EF4444;
--accent-color: #EC4899;
```

## Изменение шрифтов

### Google Fonts

1. Выберите шрифт на https://fonts.google.com
2. Замените в `index.html`:
```html
<link href="https://fonts.googleapis.com/css2?family=ВашШрифт:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

3. Обновите в `styles.css`:
```css
body {
    font-family: 'ВашШрифт', sans-serif;
}
```

### Популярные шрифты

- **Roboto** - универсальный, читаемый
- **Montserrat** - современный, стильный
- **Open Sans** - чистый, профессиональный
- **Poppins** - дружелюбный, округлый
- **Raleway** - элегантный, тонкий

## Изменение контента

### Логотип и название

В файле `index.html` найдите класс `.logo` и измените:
```html
<div class="logo">
    <!-- SVG логотип -->
    <span>Ваше название</span>
</div>
```

### Навигационное меню

Измените пункты меню в `<ul class="nav-menu">`:
```html
<ul class="nav-menu">
    <li><a href="#section1">Раздел 1</a></li>
    <li><a href="#section2">Раздел 2</a></li>
    <!-- Добавьте свои разделы -->
</ul>
```

### Главный заголовок (Hero)

```html
<h1 class="hero-title">
    Ваш заголовок с 
    <span class="gradient-text">градиентом</span>
</h1>
<p class="hero-description">
    Ваше описание проекта
</p>
```

### Статистика

Измените числа и текст в `.hero-stats`:
```html
<div class="stat">
    <div class="stat-number">Ваше число</div>
    <div class="stat-label">Ваша метка</div>
</div>
```

## Добавление новых секций

### Шаблон секции

```html
<section id="my-section" class="section">
    <div class="container">
        <div class="section-header">
            <span class="section-badge">Бейдж</span>
            <h2 class="section-title">Заголовок</h2>
            <p class="section-description">Описание</p>
        </div>
        
        <!-- Ваш контент -->
        
    </div>
</section>
```

### Добавление карточек

```html
<div class="cards-grid">
    <div class="card">
        <div class="card-icon">🎯</div>
        <h3>Заголовок</h3>
        <p>Описание</p>
    </div>
    <!-- Больше карточек -->
</div>
```

CSS для карточек:
```css
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 32px;
}

.card {
    background: white;
    padding: 32px;
    border-radius: 16px;
    box-shadow: var(--shadow-sm);
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-xl);
}
```

## Настройка курсов

### Добавление нового курса

```html
<div class="course-card">
    <div class="course-image">
        <div class="course-category">Категория</div>
        <div class="course-thumbnail" style="background: linear-gradient(135deg, #color1 0%, #color2 100%);"></div>
    </div>
    <div class="course-content">
        <h3>Название курса</h3>
        <p>Описание курса</p>
        <div class="course-meta">
            <span class="course-duration">⏱ 40 часов</span>
            <span class="course-students">👥 5,240 студентов</span>
        </div>
        <div class="course-footer">
            <div class="course-price">
                <span class="price-old">15,000₽</span>
                <span class="price-new">9,990₽</span>
            </div>
            <a href="#" class="btn-primary">Записаться</a>
        </div>
    </div>
</div>
```

## Настройка тарифов

### Изменение плана

```html
<div class="pricing-card">
    <div class="pricing-header">
        <h3>Название тарифа</h3>
        <div class="pricing-price">
            <span class="price-currency">₽</span>
            <span class="price-amount">990</span>
            <span class="price-period">/месяц</span>
        </div>
    </div>
    <ul class="pricing-features">
        <li><span class="feature-check">✓</span> Функция 1</li>
        <li><span class="feature-check">✓</span> Функция 2</li>
        <li><span class="feature-disabled">×</span> Функция 3</li>
    </ul>
    <a href="#" class="btn-primary btn-large">Выбрать план</a>
</div>
```

### Выделение популярного плана

Добавьте класс `featured`:
```html
<div class="pricing-card featured">
    <div class="pricing-badge">Популярный</div>
    <!-- остальной контент -->
</div>
```

## Настройка формы

### Добавление полей

```html
<div class="form-group">
    <label for="field-name">Название поля</label>
    <input type="text" id="field-name" name="field-name" required placeholder="Плейсхолдер">
</div>
```

### Типы полей

- `type="text"` - текст
- `type="email"` - email
- `type="tel"` - телефон
- `type="number"` - число
- `type="date"` - дата
- `<textarea>` - многострочный текст

## Настройка анимаций

### Отключение анимаций

Удалите или закомментируйте в `styles.css`:
```css
/* @keyframes float { ... } */
/* @keyframes rotate { ... } */
```

### Изменение скорости анимаций

```css
.hero-card {
    animation: float 3s ease-in-out infinite; /* Измените 3s на нужное значение */
}
```

### Новая анимация

```css
@keyframes myAnimation {
    0% { /* начальное состояние */ }
    50% { /* середина */ }
    100% { /* конечное состояние */ }
}

.my-element {
    animation: myAnimation 2s ease infinite;
}
```

## Настройка адаптивности

### Изменение точек перелома (breakpoints)

В `styles.css`:
```css
@media (max-width: 1024px) {
    /* Планшеты */
}

@media (max-width: 768px) {
    /* Мобильные */
}

@media (max-width: 480px) {
    /* Маленькие мобильные */
}
```

## Интеграция с бэкендом

### Отправка формы на сервер

В `script.js` замените секцию отправки формы:

```javascript
contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData(contactForm);
    const data = Object.fromEntries(formData);
    
    try {
        const response = await fetch('https://your-api.com/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        if (response.ok) {
            showNotification('Заявка отправлена!', 'success');
            contactForm.reset();
        } else {
            throw new Error('Ошибка отправки');
        }
    } catch (error) {
        showNotification('Произошла ошибка', 'error');
    }
});
```

## Подключение аналитики

### Google Analytics

Добавьте перед `</head>`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

### Яндекс.Метрика

Добавьте перед `</head>`:
```html
<!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){
   // код метрики
   })(window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");
</script>
```

## Дополнительные возможности

### Добавление видео фона

```html
<video autoplay muted loop class="bg-video">
    <source src="video.mp4" type="video/mp4">
</video>
```

```css
.bg-video {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
    opacity: 0.3;
}
```

### Добавление чата

```html
<!-- Перед </body> -->
<script>
  // Код виджета чата (Jivosite, Tawk.to и т.д.)
</script>
```

### Добавление cookie banner

```html
<div id="cookie-banner" class="cookie-banner">
    <p>Мы используем cookies для улучшения работы сайта</p>
    <button onclick="acceptCookies()">Принять</button>
</div>
```

## Полезные ресурсы

- [MDN Web Docs](https://developer.mozilla.org) - документация
- [Can I Use](https://caniuse.com) - поддержка браузерами
- [CSS Tricks](https://css-tricks.com) - советы по CSS
- [Google Fonts](https://fonts.google.com) - шрифты
- [Coolors](https://coolors.co) - цветовые палитры
