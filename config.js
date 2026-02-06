// config.js - Конфигурация сайта
// Измените эти значения под свой проект

const siteConfig = {
    // Основная информация
    siteName: 'Образование',
    siteDescription: 'Современная платформа онлайн обучения',
    siteUrl: 'https://your-domain.ru',
    
    // Контакты
    contact: {
        email: 'info@obrazovanie.ru',
        phone: '+7 (495) 123-45-67',
        address: 'Москва, ул. Примерная, 123'
    },
    
    // Социальные сети
    social: {
        vk: 'https://vk.com/your-page',
        telegram: 'https://t.me/your-channel',
        youtube: 'https://youtube.com/your-channel',
        instagram: 'https://instagram.com/your-account'
    },
    
    // API настройки
    api: {
        baseUrl: 'https://your-api.com/api',
        timeout: 10000, // 10 секунд
        headers: {
            'Content-Type': 'application/json'
        }
    },
    
    // Аналитика
    analytics: {
        googleAnalytics: 'UA-XXXXXXXXX-X', // Ваш GA ID
        yandexMetrika: 'XXXXXXXX' // Ваш Яндекс.Метрика ID
    },
    
    // Настройки форм
    forms: {
        contactFormEndpoint: '/api/contact',
        newsletterEndpoint: '/api/newsletter',
        // Email для отправки форм (альтернатива API)
        fallbackEmail: 'info@obrazovanie.ru'
    },
    
    // Статистика (для главной страницы)
    stats: {
        students: 50000,
        courses: 200,
        satisfaction: 98
    },
    
    // Настройки тарифов
    pricing: {
        currency: '₽',
        plans: [
            {
                id: 'basic',
                name: 'Базовый',
                price: 990,
                period: 'месяц'
            },
            {
                id: 'pro',
                name: 'Профессионал',
                price: 1990,
                period: 'месяц',
                featured: true
            },
            {
                id: 'enterprise',
                name: 'Корпоративный',
                price: 4990,
                period: 'месяц'
            }
        ]
    },
    
    // Настройки UI
    ui: {
        // Цветовая тема (используется в styles.css)
        theme: {
            primary: '#6366F1',
            secondary: '#8B5CF6',
            accent: '#EC4899',
            success: '#10B981'
        },
        
        // Анимации
        animations: {
            enabled: true,
            duration: 300, // миллисекунды
            easing: 'ease-in-out'
        },
        
        // Настройки навигации
        navigation: {
            sticky: true,
            hideOnScroll: false
        }
    },
    
    // Настройки локализации
    locale: {
        language: 'ru',
        dateFormat: 'DD.MM.YYYY',
        timeFormat: 'HH:mm',
        timezone: 'Europe/Moscow'
    },
    
    // Функциональные флаги
    features: {
        enableCourseSearch: true,
        enableUserReviews: true,
        enableChatWidget: false,
        enableNewsletter: true,
        enableDarkMode: false
    },
    
    // SEO настройки
    seo: {
        keywords: [
            'онлайн обучение',
            'курсы',
            'образование',
            'веб-разработка',
            'программирование',
            'дизайн'
        ],
        ogImage: '/images/og-image.jpg',
        twitterCard: 'summary_large_image'
    },
    
    // Настройки безопасности
    security: {
        enableCORS: true,
        allowedOrigins: ['https://your-domain.ru'],
        enableCSRF: true
    }
};

// Экспорт конфигурации
if (typeof module !== 'undefined' && module.exports) {
    module.exports = siteConfig;
}

// Для использования в браузере
if (typeof window !== 'undefined') {
    window.siteConfig = siteConfig;
}
