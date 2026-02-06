# Руководство по развертыванию

## Локальный запуск

### Вариант 1: Прямое открытие
Просто откройте файл `index.html` в браузере.

### Вариант 2: Python HTTP Server
```bash
python -m http.server 8000
```
Затем откройте http://localhost:8000

### Вариант 3: Node.js HTTP Server
```bash
npx http-server -p 8000
```

## Развертывание на хостинге

### GitHub Pages

1. Перейдите в настройки репозитория
2. Выберите раздел "Pages"
3. Выберите ветку для развертывания
4. Сохраните изменения

### Netlify

1. Перетащите папку проекта в Netlify Drop
2. Или подключите GitHub репозиторий
3. Настройки сборки не требуются (статический сайт)

### Vercel

```bash
npm i -g vercel
vercel
```

### Обычный хостинг (FTP)

1. Загрузите все файлы в корневую директорию
2. Убедитесь, что `index.html` находится в корне
3. Настройте права доступа (644 для файлов)

## Оптимизация для продакшена

### 1. Минификация CSS
```bash
# Используйте CSS minifier
npx cssnano styles.css styles.min.css
```

### 2. Минификация JavaScript
```bash
# Используйте JS minifier
npx terser script.js -o script.min.js
```

### 3. Оптимизация изображений
- Используйте WebP формат
- Сжимайте изображения
- Добавьте lazy loading

### 4. Настройка .htaccess (Apache)
```apache
# Кэширование
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 year"
  ExpiresByType image/x-icon "access plus 1 year"
</IfModule>

# Сжатие
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript
</IfModule>
```

## Настройка домена

1. Получите домен у регистратора
2. Настройте DNS записи:
   - A запись: IP адрес сервера
   - CNAME запись: www -> основной домен
3. Настройте SSL сертификат (Let's Encrypt бесплатный)

## Мониторинг

- Google Analytics - отслеживание посетителей
- Google Search Console - SEO мониторинг
- Яндекс.Метрика - аналитика для России

## Резервное копирование

Регулярно создавайте бэкапы:
```bash
tar -czf backup-$(date +%Y%m%d).tar.gz *.html *.css *.js
```

## Обновления

1. Вносите изменения локально
2. Тестируйте в браузере
3. Коммитьте в Git
4. Деплойте на хостинг

## Поддержка браузеров

Сайт протестирован и работает в:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ✅ Opera 76+

## Производительность

Целевые показатели PageSpeed Insights:
- Performance: 90+
- Accessibility: 95+
- Best Practices: 90+
- SEO: 95+
